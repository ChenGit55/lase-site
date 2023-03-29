from django.db import models


class Program(models.Model):

    PROGRAMS_CHOICES =[
        ('lion cubs', 'Lion Cubs'),
        ('evolution academy', 'Evolution Academy'),
        ('evolution fusal club', 'Evolution Futsal Club'),
    ]


    name = models.CharField(max_length=50, choices=PROGRAMS_CHOICES)
