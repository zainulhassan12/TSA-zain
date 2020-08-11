from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from InterviewPanel.models import Quiz

alphabatic = RegexValidator(r'^[a-zA-z]+([\s][a-zA-Z]+)*$', 'Only alpbetic characters are allowed', code='Invalid name')
phone = RegexValidator(r'^((\+92)|(0092))-{0,9}\d{3}-{0,9}\d{7}$|^\d{11}$|^\d{4}-\d{7}$')
# landline = RegexValidator(r'^((\+92)|(0092))-{0,9}\d{2}-{0,9}\d{7}$|^\d{10}$|^\d{3}-\d{7}$')
cnic = RegexValidator(r'^[0-9]{5}-[0-9]{7}-[0-9]{1}$')
#
GENDER_CHOICES = [
    ('female', 'Female'),
    ('male', 'Male'),
    ('other', 'Other'),
]
SPECIALIZATION_CHOICES = [
    {'please select', 'Please Select'},
    {'networking', 'Networking'},
    {'database', 'Database'},
    {'programming', 'Programming'},
]
QUALIFICATION_CHOICES = [
    {'phd', 'PHD'},
    {'master', 'Master'},
    {'bachelor', 'Bachelor'},
]
# # INTEREST_CHOICES = [
# #     {'please select', 'Please Select'},
# #     {'networking', 'Networking'},
# #     {'database', 'Database'},
# #     {'programming', 'Programming'},
# #     {'Web', 'Web'},
# # ]


# class UserApplication(models.Model):
#     First_Name = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
#     Last_Name = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
#     First_NameF = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
#     Last_NameF = models.CharField(max_length=20, blank=True, null=True, validators=[alphabatic])
#     Age = models.IntegerField()
#     Date_of_Birth = models.DateField(editable=True)
#     Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#     Experience = models.CharField(max_length=20)
#     Qualify = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES)
#     Speclization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES)
#     Image = models.ImageField()
#     cv = models.FileField()

MASTER_CHOICES = [
    {'please select', 'Please Select'},
    {'networking', 'Networking'},
    {'databaseSystems', 'DatabaseSystems'},
    {'information technology', 'Information Technology'},
    {'machine learning', 'Machine Learning'},
    {'dataScience', 'DataScience'},
    {'cyber security', 'Cyber Security'},
    {'it security management', 'It Security Management'},
    {'cyber security and data governance', 'Cyber Security And Data Governance'},
    {'data analytics and it security management', ' Data Analytics and it Security Management'},
    {'big data and business intelligence', ' Big Data and Business Intelligence'},
    {'digital product management', ' Digital Product Management'},
    {'information security', ' Information Security'},
    {'master in information and security', ' Master In Information and Security'},
    {'big data', 'Big Data'},
    {'computer security', 'Computer Security'},
    {'digitization', 'Digitization'},
    {'it security', 'It security'},
    {'networks', 'Networks'},
    {'virtualization', 'Virtualization'},
    {'cryptography', 'Cryptography'},
    {'media engineering', 'Media Engineering'},
    {'cloud computing', 'Cloud Computing'},
    {'none from this list', 'None From This List'}

]


class Application(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabatic])
    Last_Name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabatic])
    Father_Name = models.CharField(max_length=20, blank=False, null=False, validators=[alphabatic])
    Email = models.EmailField(max_length=254, verbose_name="Email", blank=False)
    Domicile = models.CharField(max_length=15, blank=False, null=True, validators=[alphabatic])
    Age = models.IntegerField(
        help_text="Age According to Date_of_Birth it will be checked in case of wrong input your application will not"
                  " be worthy.")
    Date_of_Birth = models.DateField(editable=True, help_text="Select Month Date And Year.")
    Gender = models.CharField(max_length=10,
                              help_text="Select Your Gender", choices=GENDER_CHOICES)
    Phone_no = models.IntegerField(help_text="Enter Your Phone no")
    Land_Line = models.IntegerField(help_text="Enter Your Land Line")
    # Matric = models.CharField(max_length=10, default="Result of 10th class")
    #  Intermediate = models.CharField(max_length=10, default="Result of 12th class")
    # Graduation = models.CharField(max_length=10, default="Result of 16th class")
    MatricTotal = models.IntegerField(help_text="", null=False, blank=False)
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
    Matrics_Result = models.FileField(verbose_name="Matric Result", blank=False, upload_to='Results/',
                                      help_text="Paste the PDF file of your DMC/Result card for best practices ")
    Graduations_result = models.FileField(verbose_name="Graduations_result", blank=False, upload_to='Results/',
                                          help_text="Paste the PDF file of your DMC/Result card for best practices ")
    Intermediate_result = models.FileField(verbose_name="Intermediate Result", blank=False, upload_to='Results/',
                                           help_text="Paste the PDF file of your DMC/Result card for best practices ")
    Image = models.ImageField(upload_to='images/',
                              help_text="Try to Use an Image with .JPG extension for best practices")

    Qualify = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES,
                               help_text="Select Level of your Education from Available Choices.")
    Speclization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES,
                                    help_text="Your Specialization or Field of Expertise.")
    Experience = models.FileField(default="Upload your CV", upload_to='CVs/',
                                  help_text="Paste the PDF file of your CV/ExperienceLetters for best practices ")
    Master_Specialization = models.CharField(help_text="Selct Specialization From List", max_length=50,
                                             choices=MASTER_CHOICES)

    def __str__(self):
        return "{0} {1}".format(self.First_Name, self.Last_Name)

    def get_absolute_url(self):
        return reverse("UserViews:detail", kwargs={"id": self.id})


class ApplicantGradesInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=False)
    Speciality = models.CharField(max_length=1000,
                                  help_text="Already set You have entered in the Application..Now Enter Grades",
                                  blank=True, null=False)
    ProgrammingFundamentals = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                          verbose_name="Programming Fundamentals")
    ObjectOrientedProgramming = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                            verbose_name="Object oriented programming", )

    DataStructuresAndAlgorithms = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                              verbose_name="Data structures & algorithms")
    VisualProgramming = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                    verbose_name="Visual Programming")
    WebSystemAndTechnologies = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                           verbose_name="Web Systems & Technologies")
    MobileApplicationDevelopment = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                               verbose_name="Mobile Application Development")
    DataCommunicationAndComputerNetworks = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                                       verbose_name="Data Communication & Computer"
                                                                                    " Networks")
    NetworkSecurity = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                  verbose_name="Network Security")

    WirelessAndMobileCommunication = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                                 verbose_name="Wireless & Mobile Communication")

    InternetArchitectureAndProtocol = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                                  verbose_name="Internet Architecture & Protocol")

    CloudComputing = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                 verbose_name="Cloud Computing")

    ArtificialIntelligence = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                         verbose_name="Artificial Intelligence")

    DataMining = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                             verbose_name="Data Mining")

    CalculusAndAnalyticalGeometry = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                                verbose_name="Calculus & Analytical Geometry")

    LinearAlgebra = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                verbose_name="Linear Algebra")

    DiscreteStructures = models.PositiveIntegerField(help_text="Select Grade you have obtained",
                                                     verbose_name="Discrete Structures")

    class Meta:
        verbose_name = "Grade Of Applicant"
        verbose_name_plural = "Grades Of Applicants"

    def __str__(self):
        return self.Speciality


class grades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField(editable=False)
    percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quiz_Grade"
        verbose_name_plural = "Quizzes_Grades"

    def __str__(self):
        return self.name


class canAccess(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    QuizName = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name = "Quiz_Access"
        verbose_name_plural = "Quizzes_Access"

    def __str__(self):
        return self.QuizName

