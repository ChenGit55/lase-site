from django.db import models


class Program(models.Model):

    PROGRAMS_CHOICES =[
        ('lion cubs', 'Lion Cubs'),
        ('evolution academy', 'Evolution Academy'),
        ('evolution fusal club', 'Evolution Futsal Club'),
    ]


    name = models.CharField(max_length=50, choices=PROGRAMS_CHOICES)

class Activity(models.Model): 
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
