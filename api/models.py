from django.db import models
from django.urls import reverse
# Create your models here.
class Baptism(models.Model):
    name = models.CharField(max_length=100)
    date_of_baptism = models.DateField()
    place_of_baptism = models.CharField(max_length=100)
    baptismal_name = models.CharField(max_length=100)
    other_names =models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    name_of_parents = models.CharField(max_length=100)
    solenm_or_private = models.CharField(max_length=100)
    name_of_God_parents = models.CharField(max_length=100)
    name_of_minister = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "baptism"
    def get_baptism_url(self):
        return reverse('alvan:baptism_details', kwargs={"id":self.id})

class Marriage(models.Model):
    no = models.IntegerField()
    name_of_groom = models.CharField(max_length=100)
    name_of_bride = models.CharField(max_length=100)
    groom_Town = models.CharField(max_length=100)
    bride_Town = models.CharField(max_length=100)
    groom_parent =models.CharField(max_length=200)
    bride_parent = models.CharField(max_length=200)
    assisting_priest = models.CharField(max_length=100)
    groom_witnesses = models.CharField(max_length=100)
    bride_witnesses = models.CharField(max_length=100)
    date_of_marriage = models.DateField()
    remark = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name_of_groom

    class Meta:
        verbose_name_plural = "marriages"

    def get_marriage_url(self):
        return reverse('alvan:marriage_details', kwargs={"id": self.id})

class Annoucement(models.Model):
    date  = models.DateField()
    body = models.TextField()


    class Meta:
        verbose_name_plural = "Annoucement"

    def get_announcement_url(self):
        return  reverse('alvan:announcement_details', kwargs={"id":self.id})



class Reading(models.Model):

    date = models.DateField()
    title = models.CharField(max_length=200)
    entrace_antiphon = models.TextField()
    opening_prayers =  models.TextField()
    first_reading_title = models.CharField(max_length=200)
    first_reading_subtitle = models.CharField(max_length=200)
    first_reading_body = models.TextField()
    responsorial_psalm_title = models.CharField(max_length=200)
    responsorial_psalm_subtitle = models.CharField(max_length=200)
    responsorial_psalm_body = models.TextField()
    second_reading_title = models.CharField(max_length=200)
    second_reading_subtitle = models.CharField(max_length=200)
    second_reading_body = models.TextField()
    gospel_acclamation_title  = models.CharField(max_length=200)
    gospel_acclamation_body = models.TextField()
    gospel_title = models.CharField(max_length=200)
    gospel_subtitle = models.CharField(max_length=200)
    gospel = models.TextField()
    prayer_over_the_offerings = models.TextField()
    communion_antiphon  = models.TextField()
    prayer_after_communion = models.TextField()
    def __str__(self):
        return  self.title
    class Meta:
        verbose_name_plural = "Reading"

    def get_readings_url(self):
        return reverse('alvan:readings_details', kwargs={"id":self.id})