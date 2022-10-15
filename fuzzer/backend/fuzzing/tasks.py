from time import sleep
import os
import subprocess
from pathlib import Path
import datetime
import shutil

from celery import shared_task
from .models import Task

# https://docs.celeryq.dev/en/stable/userguide/tasks.html
# https://github.com/stuartmaxwell/django-celery-example
# https://django.fun/ru/articles/tutorials/django-i-celery-1-ustanovka/
# !!!https://www.section.io/engineering-education/django-celery-tasks/#creating-a-celery-task

# https://github.com/microsoft/restler-fuzzer/blob/main/docs/user-guide/TutorialDemoServer.md

def getPaths(base_dir):
    compile_dir = os.path.join(base_dir, 'Compile')
    fuzz_lean_dir = os.path.join(base_dir, 'FuzzLean')
    result = {
        'restler_path' : os.path.join(base_dir, 'restler-fuzzer/restler_bin/restler/Restler'),
        'compile_dir' : compile_dir,
        'fuzz_lean_dir': fuzz_lean_dir,
        'grammar_path' : os.path.join(compile_dir, 'grammar.py'),
        'dict_path' : os.path.join(compile_dir, 'dict.json'),
        'engine_settings_path' : os.path.join(compile_dir, 'engine_settings.json')
    }
    return result

def startCompile(paths, openapi_json_path):
    # command = f"{paths['restler_path']} compile --api_spec {openapi_json_path}"
    
    process = subprocess.Popen([paths['restler_path'], 'compile', '--api_spec', openapi_json_path])
    print("process.stderr = ", process.stderr)
    print("process.stdout = ", process.stdout)
    print("process.communicate()[0] = ", process.communicate()[0])
    process.wait()
    
    ret_str = ""
    try:
        ret_str = subprocess.check_output([
            paths['restler_path'],
            'compile',
            '--api_spec',
            openapi_json_path])
    except subprocess.CalledProcessError as e:
        return False
    print("startCompile(): ", ret_str)
    return True

def startFuzzingLean(paths):
    # command = f"{paths['restler_path']} fuzz-lean --grammar_file {paths['grammar_path']} --dictionary_file {paths['dict_path']} --settings {paths['engine_settings_path']} --no_ssl"
    # restler-fuzzer/restler_bin/restler/Restler fuzz-lean --grammar_file Compile/grammar.py --dictionary_file Compile/dict.json --settings Compile/engine_settings.json --no_ssl
    
    # process = subprocess.Popen([
    #     paths[
    #         'restler_path'],
    #         'fuzz-lean',
    #         '--grammar_file',
    #         paths["grammar_path"],
    #         '--dictionary_file',
    #         paths['dict_path'],
    #         '--settings',
    #         paths['engine_settings_path'],
    #         '--no_ssl'
    #     ],
    #     shell = True, stdout = subprocess.PIPE,
    #     stderr = subprocess.PIPE)
    # print("process.stderr = ", process.stderr)
    # print("process.stdout = ", process.stdout)
    # print("process.communicate() = ", process.communicate())
    # process.wait()
    
    ret_str = ""
    try:
        ret_str = subprocess.check_output([
            paths[
                'restler_path'],
                'fuzz-lean',
                '--grammar_file',
                paths["grammar_path"],
                '--dictionary_file',
                paths['dict_path'],
                '--settings',
                paths['engine_settings_path'],
                '--no_ssl'
            ])
    except subprocess.CalledProcessError as e:
        return False
    
    print("startFuzzingLean(): ", ret_str)
    
    # print("process.stderr = ", process.stderr)
    # print("process.stdout = ", process.stdout)
    # print("process.communicate() = ", process.communicate()[0])
    return True

def save_fuzz_result(base_dir, paths):
    date_time_str = datetime.datetime.today().isoformat().split(".")[0].replace(":", "_")
    result_dir = paths["fuzz_lean_dir"]
    new_path = os.path.join(base_dir,
                            "media",
                            f"{os.path.basename(paths['fuzz_lean_dir'])}_{date_time_str}")
    result = None
    try:
        result = shutil.copytree(result_dir, new_path)
    except:
        return None
    return result

@shared_task
def test_task(id):
    print("*** started task with id = ", id)
    sleep(5)
    print("*** sleep end")
    model = Task.objects.get(id=id)
    print("*** model = ", model)
    model.status = 2
    model.save()
    return
    

@shared_task
def do_fuzzing(base_dir, openapi_json_path, id):
    
    paths = getPaths(base_dir)
    
    compile_result = startCompile(paths, openapi_json_path)
    if not compile_result:
        print("startCompile() = false")
        return
    print("startCompile() = true")
    # print("isCompileSuccessfull() = ", isCompileSuccessfull(paths))
    
    fuzzlean_result = startFuzzingLean(paths)
    if not fuzzlean_result:
        print("startFuzzingLean() = false")
        return
    print("startFuzzingLean() = true")
    # print("isFuzzingLeanDone() = ", isFuzzingLeanDone(paths))
    save_dir = save_fuzz_result(base_dir, paths)
    model = Task.objects.get(id=id)
    if save_dir is None:
        model.status = 2 # ошибка
    else:
        model.result_dir = os.path.join(*save_dir.split("/")[2:])
        model.status = 1 # выполнено
    model.save()
    return