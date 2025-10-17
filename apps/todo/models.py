from django.db import models


# Create your models here.
class Todo(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


# class TodoItem(models.Model):
#     todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="items")

# def __str__(self):
#     return self.title
