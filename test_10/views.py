from rest_framework.response import Response
from .serializers import SchoolSerializer, ClassSerializer, TeacherSerializer, StudentSerializer, SubjectSerializer,\
    TeachersSerializer, ClassStudentSerializer, UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import School, Class, Teacher, Student, Subject
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework import status, generics
from django.contrib.auth.models import User, Group




from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# first we define the serializers

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SchoolAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassSearchAPIView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassStudentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('ClassName', )
    search_fields = ('ClassName',)


class SearchAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('Class', 'TeacherName')
    # search_fields = ('id'.'Class', 'TeacherName')


class ClassAPIView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        Clas = Class.objects.all()
        serializer = ClassSerializer(Clas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassStudentAPIView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        Clas = Class.objects.all()
        serializer = ClassStudentSerializer(Clas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassStudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherAPIView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectAPIView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolUpdateAPIView(APIView):

    def get_object(self, id):
        try:
            return School.objects.get(id=id)

        except School.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        school = self.get_object(id)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, id):
        school = self.get_object(id)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        school = self.get_object(id)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassUpdateAPIView(APIView):

    def get_object(self, id):
        try:
            return Class.objects.get(id=id)

        except Class.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        Clas = self.get_object(id)
        serializer = ClassSerializer(Clas)
        return Response(serializer.data)

    def put(self, request, id):
        Clas = self.get_object(id)
        serializer = ClassSerializer(Clas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Class = self.get_object(id)
        Class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherUpdateAPIView(APIView):

    def get_object(self, id):
        try:
            return Teacher.objects.get(id=id)

        except Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        teacher = self.get_object(id)
        serializer = TeachersSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = self.get_object(id)
        serializer = TeachersSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentUpdateAPIView(APIView):

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)

        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubjectUpdateAPIView(APIView):

    def get_object(self, id):
        try:
            return Subject.objects.get(id=id)

        except Subject.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        teacher = self.get_object(id)
        serializer = SubjectSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = self.get_object(id)
        serializer = SubjectSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



