from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView, exception_handler
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from rest_framework import authentication
from rest_framework import permissions

from .tasks import do_fuzzing



class StartView(APIView):
    def post(self, request):
        apis = request.data.get("apis")
        do_fuzzing.delay(apis)
        return Response({"status":"ok"})

class StopView(APIView):
    def get(self, request):
        return Response({"status":"ok"})

class ReportsView(APIView):
    def get(self, request):
        return Response({"status":"ok"})

class ProgressView(APIView):
    def get(self, request):
        return Response({"status":"ok"})