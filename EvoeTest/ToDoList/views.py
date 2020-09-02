from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from ToDoList.models import Task
import json
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

class TaskView(APIView):
    permission_classes = (IsAuthenticated,)
    
    @csrf_exempt
    @api_view(['POST'])
    def Create(request):
    
        if not request.user.is_authenticated:
            
            return HttpResponse("User not authenticated.", content_type="text/plain")
        
        else:
        
            received_json_data = json.loads(request.body)
    
            new_task = Task()
    
            new_task.task_text = received_json_data["task_text"]
    
            current_user = request.user

            new_task.user_id = current_user.id
    
            new_task.save()
    
            return HttpResponse("Task saved.", content_type="text/plain")
    
    @csrf_exempt
    @api_view(['GET'])
    def Read(request):
    
        if not request.user.is_authenticated:
            
            return HttpResponse("User not authenticated.", content_type="text/plain")
        
        else:
        
            current_user = request.user

            _id = current_user.id
            
            allData = Task.objects.all().filter(user_id=_id)
    
            response = serializers.serialize('json', allData)
    
            return HttpResponse(response, content_type="text/json-comment-filtered")
    
    @csrf_exempt
    @api_view(['POST'])
    def Delete(request,_id):
    
        if not request.user.is_authenticated:
            
            return HttpResponse("User not authenticated.", content_type="text/plain")
        
        else:
        
            current_user = request.user

            user_id = current_user.id
            
            task = Task.objects.all().filter(id=_id)

            response = serializers.serialize('json', task)
            
            json_data = json.loads(response)[0]

            task_user_id = json_data['fields']['user_id']
            
            if (task_user_id == user_id):

                task.delete()
                
                return HttpResponse("Task deleted.", content_type="text/plain")
            
            else:
    
                return HttpResponse("User not allowed to delete this task.", content_type="text/plain")
