from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item, Contact, Object, Property
from .serializers import ItemSerializer, ContactSerializer, ObjectSerializer, PropertySerializer
from django.db import connection
import logging

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.create_new_table(serializer.data['name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_new_table(self, obj_name):
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE TABLE dynamic_{obj_name.lower()} (id SERIAL PRIMARY KEY)")
        return

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        object_id = request.query_params.get('object', None)
        if object_id:
            queryset = self.queryset.filter(object=object_id)
        else:
            queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if self.create_new_column(serializer.data['object'], serializer.data['name'], serializer.data['type']):                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(serializer.errors);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_new_column(self, object_id, col_name, type):
        col_type = "VARCHAR(255)"
        col_name_conv = col_name
        col_name_conv = col_name_conv.strip().lower()
        match type:
            case 0:
                col_type = "VARCHAR(255)"
            case 1:
                col_type = "TEXT"
            case 2:
                col_type = "INTEGER"
            case 3:
                col_type = "INTEGER"
            case 4:
                col_type = "DATE"
            case 5:
                col_type = "TIME"
            case 6:
                col_type = "DATETIME"
            case 7:
                col_type = "INTEGER"
        table_name = ""
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM myapp_object WHERE id = '{object_id}'")
            table_name = cursor.fetchone()[0]

        try:
            with connection.cursor() as cursor:
                cursor.execute(f"ALTER TABLE dynamic_{table_name.lower()} ADD COLUMN {col_name_conv} {col_type}")            
            return True
        except Exception as e:
            logging.error(f"Error creating new column {col_name_conv} with type {type}: {e}")
            return False
        

