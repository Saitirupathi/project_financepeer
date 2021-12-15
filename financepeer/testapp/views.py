from django.shortcuts import render
from testapp.forms import UploadForm
from testapp.models import Upload,DisplayItems
import json
# Create your views here.
def home_view(request):
    return render(request,'testapp/base.html')

def upload_view(request):
    if request.method == 'POST':
        form=UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('record inserted successfully')
            a=Upload.objects.all()[0]
            with open(a.file.path, 'r') as openfile:
                json_object=json.load(openfile)
                json_obj=[{k: v for k, v in d.items() if k !='id'} for d in json_object]
                for each_obj in json_obj:
                    DisplayItems.objects.create(**each_obj)
    else:
        form=UploadForm()
    return render(request,'testapp/home.html',{'form':form})

def logout_view(request):
    return render(request,'testapp/logout.html')

def display_view(request):
    a=DisplayItems.objects.all()
    return render(request,'testapp/display.html',{'a':a})
