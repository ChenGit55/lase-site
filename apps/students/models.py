from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import date
from .utils import slugify_instances

now = timezone.now()
today = now.strftime("%Y-%m-%d")

class Student(models.Model):

    #return a detail url with the right slug
    def get_absolute_url(self):
        return reverse('details', kwargs={"slug" : self.slug})

    #calc and retur the age
    def age_calc(self):
        age = (date.today() - self.birth_date).days // 365
        return age

    def __str__(self):
        return f'{self.id} {self.student_fname} {self.student_lname}'

    #creating gender options
    GENDER_CHOICES =[
        ('Boy', 'Boy'),
        ("Girl", 'Girl'),
    ]

    #creating a programs options
    PROGRAMS_CHOICES =[
        ('Lion Cubs', 'Lion Cubs'),
        ('Evolution Academy', 'Evolution Academy'),
        ('Evolution Fusal Club', 'Evolution Futsal Club'),
    ]

    #phone validator
    phone_ragex = RegexValidator(
        regex=r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$',
        message="'(999) 999-9999'."
    )

    #studnet info
    slug = models.SlugField(unique=True, max_length=50, blank=True, null=True)

    #link with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    student_fname = models.CharField(max_length=50)
    student_lname = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=8, default=today, null=True, blank=True)
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, null=True, blank=True)
    program = models.CharField(max_length=50, choices=PROGRAMS_CHOICES, null=True, blank=True)
    additional_info = models.TextField(max_length=1000, null=True, blank=True)

    #address info
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(
        max_length=2, null=True, blank=True,
        choices=(
            ('AL', 'Alabama'),
            ('AK', 'Alaska'),
            ('AZ', 'Arizona'),
            ('AR', 'Arkansas'),
            ('CA', 'California'),
            ('CO', 'Colorado'),
            ('CT', 'Connecticut'),
            ('DE', 'Delaware'),
            ('FL', 'Florida'),
            ('GA', 'Georgia'),
            ('HI', 'Hawaii'),
            ('ID', 'Idaho'),
            ('IL', 'Illinois'),
            ('IN', 'Indiana'),
            ('IA', 'Iowa'),
            ('KS', 'Kansas'),
            ('KY', 'Kentucky'),
            ('LA', 'Louisiana'),
            ('ME', 'Maine'),
            ('MD', 'Maryland'),
            ('MA', 'Massachusetts'),
            ('MI', 'Michigan'),
            ('MN', 'Minnesota'),
            ('MS', 'Mississippi'),
            ('MO', 'Missouri'),
            ('MT', 'Montana'),
            ('NE', 'Nebraska'),
            ('NV', 'Nevada'),
            ('NH', 'New Hampshire'),
            ('NJ', 'New Jersey'),
            ('NM', 'New Mexico'),
            ('NY', 'New York'),
            ('NC', 'North Carolina'),
            ('ND', 'North Dakota'),
            ('OH', 'Ohio'),
            ('OK', 'Oklahoma'),
            ('OR', 'Oregon'),
            ('PA', 'Pennsylvania'),
            ('RI', 'Rhode Island'),
            ('SC', 'South Carolina'),
            ('SD', 'South Dakota'),
            ('TN', 'Tennessee'),
            ('TX', 'Texas'),
            ('UT', 'Utah'),
            ('VT', 'Vermont'),
            ('VA', 'Virginia'),
            ('WA', 'Washington'),
            ('WV', 'West Virginia'),
            ('WI', 'Wisconsin'),
            ('WY', 'Wyoming')
        )
    )

    #parent info
    parent_fname = models.CharField(max_length=50, default='', null=True, blank=True)
    parent_lname = models.CharField(max_length=50, default='', null=True, blank=True)
    parent_email = models.EmailField(max_length=300, default='', null=True, blank=True)
    parent_phone = models.CharField(validators=[phone_ragex], max_length=14, null=True, blank=True)

    #emergency contatct info
    emergency_fname = models.CharField(max_length=50, null=True, blank=True)
    emergency_lname = models.CharField(max_length=50, null=True, blank=True)
    emergency_phone = models.CharField(validators=[phone_ragex], max_length=14, null=True, blank=True)

    #who filled out the form
    filled_out_fname = models.CharField(max_length=50, null=True, blank=True)
    filled_out_lname = models.CharField(max_length=50, null=True, blank=True)

def student_pre_save(sender, instance,*args, **kwargs):
    if instance.slug is None:
        slugify_instances(instance, save=False)

pre_save.connect(student_pre_save, sender=Student)

def student_post_save(sender, instance, created,*args,**kwargs):
    if created:
        slugify_instances(instance, save=True)
        Statistic.objects.create(student=instance)

post_save.connect(student_post_save, sender=Student)

class Statistic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    agility = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
    physical = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = [['student']]
