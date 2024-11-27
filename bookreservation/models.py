from django.db import models

# Create your models here.

class Bookdetails(models.Model):
    bookid = models.IntegerField(primary_key=True)
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    currentlycheckedout = models.BooleanField()
    numberoftimescheckedout = models.IntegerField()

class Studentdetails(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

class Reservationinformation(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)