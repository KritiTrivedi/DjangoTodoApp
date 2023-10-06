from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializer import TimingTodoSerializer, TodoSerializer
from home.models import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action


# Create your views here.

# Function Base Api's ----->

@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message':'yess!! django is working. This is GET API. '
        })
    elif request.method == 'POST':
         return Response({
            'status':200,
            'message':'yess!! django is working. This is POST API.'
        })
    else :
         return Response({
            'status':200,
            'message':'Invalid Api !!!!'
        })
    
@api_view(['GET'])
def get_todo(request):
      try:
            
            getObject = Todo.objects.all()
            serializer = TodoSerializer(getObject, many=True)
            return Response({
                  'status':True,
                  'message':'fatched data',
                  'data':serializer.data
                })
      except Exception as e:
            print("error===>",e)
            return Response({
                  'status':False,
                  'message':'Something went wrong'
            })          
    
@api_view(['POST'])    
def create_todo(request):
     try:
          data = request.data
          print('data====>',data)
          serializer = TodoSerializer(data=request.data)
          if serializer.is_valid():
            print('serializer.data==>',serializer.validated_data)
            serializer.save()
            return Response({
                         'status': True,
                         'message':'Success Todo Created',
                         'data':serializer.data
                   })
          return Response({
                         'status': False,
                         'message':'Invalid Data',
                         'data':serializer.errors
                   })  
     except Exception as e:
                   print("error===>",e)
                   return Response({
                         'status': False,
                         'message':'Something went Wrong'
                   })
     
@api_view(['DELETE'])     
def delete_all_timing_todos(request):
      try:
        # Delete all records in TimingTodo
        TimingTodo.objects.all().delete()
        return Response({'message': 'All TimingTodo records deleted successfully.'})
      except Exception as e:
        return Response({'message': f'An error occurred: {str(e)}'}, status=500)   
      
@api_view(['PATCH'])
def update_todo(request):
      try:
           data = request.data 
           if not data.get('id'):
                 return Response({
                         'status': False,
                         'message':'Id is required'
                   }) 
           obj = Todo.objects.get(id= data.get('id'))
           serializer = TodoSerializer(obj, data=data, partial=True)
           if serializer.is_valid():
                 serializer.save()
                 return Response({
                         'status': True,
                         'message':'Updated Successfully',
                         'data':serializer.data
                   })
      except Exception as e:
                print("error===>",e)
                return Response({
                         'status': False,
                         'message':'Something went Wrong'
                   }) 
      
# Class Base Api --->

class TodoView(APIView):

      def get(self, request):
           try:
            getObject = Todo.objects.all()
            serializer = TodoSerializer(getObject, many=True)
            return Response({
                  'status':True,
                  'message':'fatched data',
                  'data':serializer.data
                })
           except Exception as e:
            print("error===>",e)
            return Response({
                  'status':False,
                  'message':'Something went wrong'
            })  
           
      def post(self,request):
       try:
          data = request.data
          print('data====>',data)
          serializer = TodoSerializer(data=request.data)
          if serializer.is_valid():
            print('serializer.data==>',serializer.validated_data)
            serializer.save()
            return Response({
                         'status': True,
                         'message':'Success Todo Created',
                         'data':serializer.data
                   })
          return Response({
                         'status': False,
                         'message':'Invalid Data',
                         'data':serializer.errors
                   })  
       except Exception as e:
                   print("error===>",e)
                   return Response({
                         'status': False,
                         'message':'Something went Wrong'
                   })        
      

#ViewSet --->  

class TodoViewSet(viewsets.ModelViewSet):
     queryset = Todo.objects.all()
     serializer_class = TodoSerializer 
  

     @action(detail=False,methods=['GET'])
     def get_timing_todo(self,request):
          obj = TimingTodo.objects.all()
          serializer = TimingTodoSerializer(obj, many=True)
          return Response({
                         'status': True,
                         'message':'Get TodoTiming Success',
                         'data':serializer.data
                   })

     @action(detail=False,methods=['POST'])
     def add_date_to_todo(self,request):
          try:
               data = request.data
               serializer = TimingTodoSerializer(data=data)
               if serializer.is_valid():
                    serializer.save()
                    return Response({
                         'status': True,
                         'message':'Success Todo Created',
                         'data':serializer.data
                   })
               return Response({
                         'status': False,
                         'message':'Invalid Data',
                         'data':serializer.errors
                   }) 
          except Exception as e:
                   print("error===>",e)
                   return Response({
                         'status': False,
                         'message':'Something went Wrong'
                   }) 