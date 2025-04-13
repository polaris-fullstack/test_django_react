from django.db import models

# Create your models here.

PROPERTY_TYPE_CHOICES = [
    (0, 'Single Line Input'),
    (1, 'Multi Line Input'),
    (2, 'Checkbox'),
    (3, 'Dropdown'),
    (4, 'Radio'),
    (5, 'Date'),
    (6, 'Time'),
    (7, 'Date and Time'),
    (8, 'Number')
]

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']

class Object(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
class Property(models.Model):
    name = models.CharField(max_length=100)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    type = models.IntegerField(choices=PROPERTY_TYPE_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
