# Generated by Django 4.2 on 2024-11-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bookdetails",
            fields=[
                ("bookid", models.IntegerField(primary_key=True, serialize=False)),
                ("bookname", models.CharField(max_length=100)),
                ("authorname", models.CharField(max_length=100)),
                ("currentlycheckedout", models.BooleanField()),
                ("numberoftimescheckedout", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Studentdetails",
            fields=[
                ("studentid", models.IntegerField(primary_key=True, serialize=False)),
                ("firstname", models.CharField(max_length=100)),
                ("lastname", models.CharField(max_length=100)),
                ("major", models.CharField(max_length=100)),
                ("year", models.CharField(max_length=100)),
                ("gpa", models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]