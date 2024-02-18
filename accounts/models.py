from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from course.models import Course
from school.models import School
from type.models import Type
from faculty.models import Faculty


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email





class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=15)
    level = models.CharField(max_length=15, choices=LevelChoices, help_text='your student level', default=1, blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name='students_course', blank=True, null=True)


    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, related_name="Staff_faculty")


    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class UserAgentInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.user_agent}"