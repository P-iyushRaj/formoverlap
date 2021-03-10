from django.db import models

Gender = (
    ("M", "male"),
    ("F", "Female"),
    ("o", "Other")
)

day_choice = ( ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),
('6','6'),('7','7'),('8','8'),('9','9'),('10','10')
)
month_choice = (('1','january'),('2','february'),('3','march'),
('4','april'),)
year_choice = (('1990','1990'),('1991','1991'),('1992','1992'),
('1993','1993'),('1994','1994'),('1995','1995'),
)
# Create your models here.
class Patient(models.Model):
    gender = models.CharField(choices=Gender, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null = True, blank=True)
    #dae of berth
    dob_month = models.IntegerField(choices=month_choice)
    dob_day = models.IntegerField(choices=day_choice)
    dob_year = models.IntegerField(choices=year_choice)
    height = models.IntegerField()
    weight = models.IntegerField()
