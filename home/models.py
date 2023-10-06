# Import necessary modules
from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    createAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)

class TimingTodo(BaseModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timing = models.DateTimeField()

