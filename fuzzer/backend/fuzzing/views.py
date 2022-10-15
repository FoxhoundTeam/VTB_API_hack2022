from django.shortcuts import render

from django.core.files.base import File, ContentFile
from django.conf import settings

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView, exception_handler
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from rest_framework import authentication
from rest_framework import permissions


from .tasks import *
from .models import *
from .serializers import *

import json
import datetime
import os
import threading

from multiprocessing import Process, Queue, Pool

fuzzing_queue = Queue()

class StartView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        apis = request.data.get("apis")
        
        # открыть базовый полный swagger
        print("basedir = ", str(settings.BASE_DIR / "swagger_test.json"))
        swaggerfile = open(settings.BASE_DIR / "swagger_test.json","r")
        swagger_dict = json.load(swaggerfile)
        swaggerfile.close()
        
        # выделить из него зарпошенные API
        for path in swagger_dict["paths"]:
            if path not in apis:
                del swagger_dict["paths"][path]
        
        # сохранить во временный файл
        # new_swagger_file_name = str(settings.BASE_DIR / f"media/swagger_{datetime.datetime.today().isoformat()}.json")
        datetimestr = datetime.datetime.today().isoformat().split('.')[0].replace(':','-')
        new_swagger_file_name = f"swagger_{datetimestr}.json"
        new_swagger_file = open(f"media/{new_swagger_file_name}","w+")
        json.dump(swagger_dict, new_swagger_file)
        new_swagger_file.close()
        
        new_task = Task()
        # new_task.swagger_file.save(name=f"media/swagger_{datetime.date.today().isoformat()}.json",
        #                            content=ContentFile(json.dumps(swagger_dict))
        new_task.swagger_file.name = new_swagger_file_name
        new_task.name = datetimestr
        new_task.status = 0 # "передано на запуск"
        new_task.save()
        
        # переделано на Celery вместо пула процессов
        # do_fuzzing.delay(apis, new_swagger_file_name) #TODO отладка celery/redis
        # fuzz_thread = Process(target=do_fuzzing_simple, args=(apis, new_swagger_file_name))
        # fuzz_thread = threading.Thread(target=do_fuzzing_simple(apis, new_swagger_file_name), args=(1,))
        # fuzz_thread.start()
        # new_task.pid = fuzz_thread.pid
        
        # ТЕСТ просто задача с таймером, без реального фаззинга
        # test_task.delay(id = int(new_task.id)) # просто задача с таймером, без реального фаззинга
        # return(Response({"status":"ok", "id":int(new_task.id)}))
    
        do_fuzzing.delay(base_dir=str(settings.BASE_DIR),
                   openapi_json_path=f"media/{new_swagger_file_name}",
                   id = new_task.id)
        return(Response({"status":"ok", "id":new_task.id}))
    
        # new_task = Task.objects.get(id = new_task.id)
        
        # result_dir = new_task.result_dir
        # if result_dir is None:
        #     new_task.status = 2 # ошибка
        #     new_task.save()
        #     return Response({"status":"error"})
        # # open(os.listdir(os.path.join(result_dir, "RestlerResults")[0]) # каталог с логами
        
        # errorBucketsFileName = os.path.join(result_dir, "ResponseBuckets", "errorBuckets.json")
        # errorBucketsFile = open(errorBucketsFileName, "r")
        # errorBuckets = json.load(errorBucketsFile)
        # errorBucketsFile.close()
        
        # runSummaryFileName = os.path.join(result_dir, "ResponseBuckets", "runSummary.json")
        # runSummaryFile = open(runSummaryFileName, "r")
        # runSummary = json.load(runSummaryFile)
        # runSummaryFile.close()
        
        # return Response({"status":"ok", "errorBuckets":errorBuckets, "runSummary":runSummary})

class StopView(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        return Response({"status":"ok"})
    
class UpdateTasks(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({"status":"ok"})

class ReportsView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    
    def list(self, request, *args, **kwargs):
        result =  super().list(request, *args, **kwargs)
        return result
    
    def retrieve(self, request, *args, **kwargs):
        result = super().retrieve(request, *args, **kwargs)
        return result
    

class ProgressView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        return Response({"status":"ok"})