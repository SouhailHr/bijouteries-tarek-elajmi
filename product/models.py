from django.db import models

# Create your models here.

category_choices = (

    ('Bracelets', 'Bracelets'),
    ('Ensembles', 'Ensembles'),
    ('Bagues', 'Bagues'),
    ('Sollitaire', 'Sollitaire'),
    ('Serie', 'Serie'),
    ('Chichkhane', 'Chichkhane'),
)

class Product(models.Model):
    category = models.CharField(max_length=50, choices=category_choices, default='')
    image = models.ImageField(upload_to='images/%y/%m/%d/', max_length=255, null=True, blank=True)
    imagebig = models.ImageField(upload_to='images/%y/%m/%d/', max_length=255, null=True, blank=True)
    imageside = models.ImageField(upload_to='images/%y/%m/%d/', max_length=255, null=True, blank=True)
    name = models.CharField(max_length=254, default='')
    desciption = models.CharField(max_length=254, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
            ordering = ['-created']
            ordering = ['-updated']