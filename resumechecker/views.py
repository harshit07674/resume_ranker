from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import JobDescriptionSerializer,Jobs,ResumeSerializer,Resume
from .analyzer import process_resume
# Create your views here.

class JobDescriptionAPi(APIView):
    def get(self, request):
        queryset=Jobs.objects.all()
        serializer=JobDescriptionSerializer(queryset,many=True)
        return Response({
            'status':True,
            'data':serializer.data
        })
    
class AnalyzeResumeAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            if not data.get('job_description'):
                return Response({
                    'status':False,
                    'message':'job_description is required',
                    'data':{}
                })
            serializer = ResumeSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'status':False,
                    'message':'errors',
                    'data':serializer.errors
            }) 
            serializer.save()
            _data=serializer.data
            resume_instance=Resume.objects.get(id=_data['id'])
            resume_path=resume_instance.resume.path
            data=process_resume(resume_path,Jobs.objects.get(id=data.get('job_description')).job_description)
            print(data)
            return Response({
                    'status':True,
                    'message':'resume analyzed',
                    'data':data
            })
        except Exception as e:
            print(e)
            return Response({
                'data':False,
            })
        

