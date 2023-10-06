from rest_framework import serializers
from home.models import TimingTodo, Todo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField()

    class Meta:
        model= Todo
        fields = ['todo_title','todo_description','slug']
   #    exclude=['todo_title']

    def get_slug(self,obj):
         return slugify(obj.todo_description)    

    # Field validate with different functions --->
    def validate_todo_title(self, data):
       errors = []
       if len(data)<3:
              errors.append('todo title must be more then 3 characters')
       
       regex_title = re.compile("[@_!#$%^&*()<>?/|}{~:]")
       if regex_title.search(data):
                errors.append('Cannot include these characters in todo_title')
       if errors:
            raise serializers.ValidationError(errors)    
           
       return data
    
    def validate_todo_description(self, data):
       errors = []
       max_length = 50
       if len(data) > max_length:
              errors.append('Todo description cannot exceed `{max_length}` characters')

       if errors:
            raise serializers.ValidationError(errors)
       return data    
    
    # Field validate in one function--->

    # def validate(self, validated_Data):
    #    todo_title = validated_Data.get('todo_title')
    #    todo_description = validated_Data.get('todo_description')
    #    errors = []
    #    if todo_title:
            
    #         if len(todo_title)<3:
    #           errors.append('todo title must be more then 3 characters')   

    #         regex_title = re.compile("[@_!#$%^&*()<>?/|}{~:]")
    #         if regex_title.search(todo_title):
    #             errors.append('Cannot include these characters in todo_title')

    #    if todo_description:
    #         regex_description = re.compile("[0123456789]")
    #         if regex_description.search(todo_description):
    #             errors.append('Cannot include 0123456789 in todo_description') 
    #    if errors:
    #         raise serializers.ValidationError(errors)

    #    return validated_Data

class TimingTodoSerializer(serializers.ModelSerializer):

     todo = TodoSerializer()
     class Meta:
          model = TimingTodo
          exclude = ['createAt','updatedAt']
          # depth = 1



