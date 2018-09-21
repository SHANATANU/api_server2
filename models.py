from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings



fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Bus(models.Model):
    name=models.CharField(max_length=100)
    liceno=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    image=models.FileField(storage=fs)
    def __str__(self):
        return self.name

    class Meta:
        db_table="inotrcks"

class Address(models.Model):
    building_no=models.CharField(max_length=100)
    street=models.CharField(max_length=250)
    landmark=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode=models.IntegerField()

    def __str__(self):
        return self.building_no



class imageModel(models.Model):
    Name=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    longitute=models.CharField(max_length=100)
    latitute=models.CharField(max_length=150)
    location=models.CharField(max_length=250)
    other=models.CharField(max_length=500)
    image=models.FileField(storage=fs)
    address=models.OneToOneField(Address,on_delete=models.CASCADE )
    pincode=models.IntegerField()

    def __str__(self):
        return str(self.longitute+"/"+self.latitute+"/"+str(self.image))


class Pincode(models.Model):
    pincode=models.IntegerField(primary_key=True)

    def __str__(self):
         return str(self.pincode)