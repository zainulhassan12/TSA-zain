from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from InterviewPanel.models import Quiz

alphabatic = RegexValidator(r'^[a-zA-z]+([\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')
phone = RegexValidator(r'^((\+92)|(0092))-{0,9}\d{3}-{0,9}\d{7}$|^\d{11}$|^\d{4}-\d{7}$')
# landline = RegexValidator(r'^((\+92)|(0092))-{0,9}\d{2}-{0,9}\d{7}$|^\d{10}$|^\d{3}-\d{7}$')
cnic = RegexValidator(r'^[0-9]{5}-[0-9]{7}-[0-9]{1}$')

GENDER_CHOICES = [
    ('female', 'Female'),
    ('male', 'Male'),
    ('other', 'Other'),
]
SPECLIZATION_CHOICES = [
    {'please select', 'Please Select'},
    {'networking', 'Networking'},
    {'database', 'Database'},
    {'programming', 'Programming'},
]
QUALIFICATION_CHOICES = [
    {'phd', 'PHD'},
    {'master', 'Master'},
    {'bachlor', 'Bachlor'},
]
INTEREST_CHOICES = [
    {'please select', 'Please Select'},
    {'networking', 'Networking'},
    {'database', 'Database'},
    {'programming', 'Programming'},
]
MASTER_CHOICES = [
    {'please select', 'Please Select'},
    {'cs', 'CS'},
    {'se', 'SE'},
    {'it', 'IT'},
]


class UserApplication(models.Model):
    First_Name = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
    Last_Name = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
    First_NameF = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
    Last_NameF = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
    Age = models.IntegerField()
    Date_of_Birth = models.DateField(editable=True)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Experience = models.CharField(max_length=20)
    Qualify = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES)
    Speclization = models.CharField(max_length=30, choices=SPECLIZATION_CHOICES)
    Image = models.ImageField()
    cv = models.FileField()


class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabatic])
    Last_Name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabatic])
    Father_Name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabatic])
    Email = models.EmailField(max_length=254, verbose_name="Email", blank=False)
    Domicile = models.CharField(max_length=15, blank=False, null=True, validators=[alphabatic])
    Age = models.IntegerField()
    Date_of_Birth = models.DateField(editable=True)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Phone_no = models.IntegerField()
    Land_Line = models.IntegerField()
    # Matric = models.CharField(max_length=10, default="Result of 10th class")
    #  Intermediate = models.CharField(max_length=10, default="Result of 12th class")
    # Graduation = models.CharField(max_length=10, default="Result of 16th class")
    MatricTotal = models.IntegerField(null=False, blank=False)
    MatricObtain = models.IntegerField(null=False, blank=False)
    MatricSubject = models.CharField(max_length=50, blank=False, null=False)
    MatricPercentage = models.FloatField(max_length=None, blank=False, default=0.0, )
    MatricGrades = models.CharField(max_length=5, blank=False, null=True, )
    MatricYear = models.CharField(max_length=20, blank=False)
    IntermediateTotal = models.IntegerField(null=False, blank=False)
    IntermediateObtain = models.IntegerField(null=False, blank=False)
    IntermediateSubject = models.CharField(max_length=50, blank=False, null=False)
    IntermediatePercentage = models.FloatField(blank=False, default="0.0")
    IntermediateGrades = models.CharField(max_length=5, blank=False, null=True)
    IntermediateYear = models.CharField(max_length=20, blank=False)
    GraduationTotal = models.IntegerField(null=False, blank=False)
    GraduationObtain = models.IntegerField(null=False, blank=False)
    GraduationSubject = models.CharField(max_length=50, blank=False, null=False)
    GraduationPercentage = models.FloatField(blank=False, max_length=None, default='0.0')
    GraduationGrades = models.CharField(max_length=5, blank=False, null=True)
    GraduationYear = models.CharField(max_length=20, blank=False)
    Matrics_Result = models.FileField(verbose_name="Matric Result", blank=False, upload_to='Results/')
    Graduations_result = models.FileField(verbose_name="Graduations_result", blank=False, upload_to='Results/')
    Intermediate_result = models.FileField(verbose_name="Intermediate Result", blank=False, upload_to='Results/')
    Image = models.ImageField(upload_to='images/')
    Qualify = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES)
    Speclization = models.CharField(max_length=30, choices=INTEREST_CHOICES)
    Experience = models.FileField(default="Upload your CV", upload_to='CVs/')
    Master_Specialization = models.CharField(max_length=15, choices=MASTER_CHOICES)

    def __str__(self):
        return "{0} {1}".format(self.First_Name, self.Last_Name)

    def get_absolute_url(self):
        return reverse("UserViews:detail", kwargs={"id": self.id})


# class UserInformation(models.Model):


class test1(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)


class grades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class canAccess(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    QuizName = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.QuizName
