from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher, Student, School, Subject, Class
from rest_framework.serializers import ValidationError

from django.contrib.auth.models import User, Group



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )




class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_name', 'created_at', 'updated_at']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name', 'subject_name', 'class_name']
        depth = 2


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject']

    def validate_Subject(self, data):
        subject = data['Subject']
        query = Subject.object.filter(class_name=subject)
        if query.exists():
            raise ValidationError()
        return data


class ClassStudentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=True)

    class Meta:
        model = Class
        fields = ['id', 'class_name', 'student']

    def validate_class_name(self, data):
        class_name = data['class_name']
        query = Class.object.filter(class_name=class_name)
        if query.exists():
            raise ValidationError()
        return data


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ['id', 'class_name', 'student']

    def validate_class_name(self, data):
        class_name = data['class_name']
        query = Class.object.filter(class_name=class_name)
        if query.exists():
            raise ValidationError()
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']

    def validate_first_name(self, data):
        first_name = data['first_name']
        query = Student.object.filter(first_name=first_name)
        if query.exists():
            raise ValidationError()
        return data

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        obj_data = Student(first_name=first_name,
                           last_name=last_name,
                           )
        obj_data.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
