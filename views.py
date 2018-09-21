from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import PIL
import numpy
from PIL import Image
from PIL import ImageOps
from time import time
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


from .models import *
import os


def index(request):
    #return HttpResponse("<h1> jai api </h1>")
    return render(request,'API/saveImg.html')


@csrf_exempt
def update_location(request):
   response_data = {"om": "omjk"}
   try:
    if request.method == "POST":
      id = request.POST['id']
      name=request.POST['name']
      print(id)
      print(name)


   except Exception as e:
      response_data["status"] = str(e)
      print(e)

   return HttpResponse(json.dumps(response_data),content_type="application/json")


#its convert image into array and then convert it into buffer and then convert into string:
def convertImageArr(img):
    img = PIL.Image.open(img).convert("RGB")
    imgarr = numpy.array(img)
    print(img)
    imgR = Image.fromarray(imgarr)
    ltrb_border = (0, 0, 0, 10)
    imgR_with_border = ImageOps.expand(imgR, border=ltrb_border, fill='white')
    buffer = BytesIO()
    imgR_with_border.save(fp=buffer, format='JPEG')
    buff_val = buffer.getvalue()
    image_file = InMemoryUploadedFile(ContentFile(buff_val), None, 'inno.jpg', 'image/jpeg', ContentFile(buff_val).tell, None)
    return image_file






@csrf_exempt
def image_Save(request):
    response_data = {}
    try:

     for i in range(0,500):
      if request.method=="POST":
         image = request.FILES['File']

         image_file=convertImageArr(image)
         # imagemodel objects creation
         im=imageModel()
         im.longitute=request.POST['longitute']
         im.latitute=request.POST['latitute']
         im.location=request.POST['longitute']+"/"+request.POST['latitute']
         im.Name=request.POST['name']
         im.type=request.POST['type']
         im.image=request.FILES['File']
         im.pincode=request.POST['pincode']
        # address object creation
         add=Address()
         add.building_no=request.POST['building_no']
         add.street=request.POST['street']
         add.landmark=request.POST['landmark']
         add.city=request.POST['city']
         add.state=request.POST['state']
         add.country=request.POST['country']
         add.pincode=request.POST['pincode']
         # save address data
         add.save()
         # imageMddel address consist address model objects
         im.address=add
         # save image data
         im.save()

         #pincode record
         ip=Pincode()
         ip.pincode=request.POST['pincode']
         ip.save()



         response_data['longitute'] =request.POST['longitute']
         response_data['latitute'] = request.POST['latitute']
         response_data['image'] = str(image)
         response_data['name']=request.POST['name']
         response_data['type']=request.POST['type']
         response_data['building_no']=request.POST['building_no']
         response_data['street']=request.POST['street']
         response_data['landmark']=request.POST['landmark']
         response_data['city']=request.POST['city']
         response_data['state']=request.POST['state']
         response_data['country']=request.POST['country']
         response_data['pincode']=request.POST['pincode']
         response_data['status']="successful"
    except Exception as e:
      response_data["status"]=str(e)
      print(e)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def getLocation(request):
    start = time()
    response_data={"om":"nhnng"}
    try:
       if request.method=="POST":
          for loc in imageModel.objects.filter(pincode=int(request.POST['pincode'])):
              print(loc.location)





    except Exception as e:
        response_data['status']=str(e)
        print(e)
    elapsed = time() - start
    print(elapsed)
    return HttpResponse(json.dumps(response_data), content_type="application/json")