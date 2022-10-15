import os
import subprocess
from pathlib import Path

BASE_DIR = '/mnt/c/D/Apps/Hack/2022.10_VTB_API/VTB_API_hack2022/experiment/backend'

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

def isCompileSuccessfull(paths):
    # фраза "Task Compile succeeded"
    result = (os.path.exists(paths['compile_dir'])
              and os.path.exists(paths['grammar_path'])
              and os.path.exists(paths['dict_path'])
              and os.path.exists(paths['engine_settings_path']))
    return result

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

def isFuzzingLeanDone(paths):
    # created_dir = 
    
    # errorBuckets = 'ResponseBuckets/errorBuckets.json'
    # runSummary = 'ResponseBuckets/runSummary.json'
    # фраза в std output "Task FuzzLean succeeded", в противном случае "ERROR"
    result = False
    return result

def save_fuzzing_result():
    
    pass

def fuzz_task(base_dir, openapi_json_path):
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
    save_fuzzing_result(paths)

if __name__ == "__main__":
    fuzz_task(BASE_DIR, 'swagger.json')
    
    
