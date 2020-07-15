from django.db import models



class School(models.Model):
    school_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.school_name


class Class(models.Model):
    class_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    std = models.ForeignKey(Class, related_name='student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ['first_name', 'last_name']
        ordering = ['first_name']

    def __str__(self):
        return '%s: %s' % (self.first_name, self.last_name)


class Subject(models.Model):
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    subject_name = models.ManyToManyField(Subject)
    class_name = models.ManyToManyField(Class)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # class Meta:
    #     unique_together = ['teacher_name', 'subject_name', 'class_name']
    #     ordering = ['teacher_name']
    #
    # def __str__(self):
    #     return '%s:' % (self.teacher_name )

    def __str__(self):
        return self.teacher_name
