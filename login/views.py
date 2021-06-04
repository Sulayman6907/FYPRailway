import matlab.engine
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


 





def loginPage(request):
    return render(request, 'login/login.html')

def home(request):
    
    return render(request, 'Home/home.html')

def run(request):
    eng = matlab.engine.start_matlab()
    eng.schedule(nargout=0)
    cols=['Station 1','Station 1','Station 2','Station 2','Station 3','Station 3','Station 4','Station 4','Station 5','Station 5','Station 6','Station 6','Station 7','Station 7','Station 8','Station 8','Station 9','Station 9','Station 10','Station 10']
    df = pd.read_excel (r"C:\Users\M Salman\Desktop\Final Year web app\railway\login\Schedule.xlsx",dtype=str)
    df = df.fillna("")
    
    print(df)
    html = df.to_html()
    
    # print(html.tr)
    # return JsonResponse(html)
    return HttpResponse(html)

def check(request):
    return render(request,'Table/table.html')

# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)

def change(request):
    file = "C:\\Users\\M Salman\\Desktop\\Final Year web app\\railway\\login\\Input.xlsx"
    

    os.startfile(file)
    return render(request,'Table/table.html')

@csrf_exempt
def saveFile(request):
    filename = request.POST.get('f_name')
    xls_file = request.FILES.get('xls_file')
    with open("login/Input.xlsx", 'wb') as file_writer:
        f = xls_file.read()
        file_writer.write(f)
    return HttpResponse("File uploaded sucessfully")    


def getData(request):
    df = pd.read_excel (r"C:\Users\M Salman\Desktop\Final Year web app\railway\login\Schedule.xlsx",sheet_name=1)
    print(df)
    html=df.to_html()
    array=df.to_numpy()
    print(df)
    return HttpResponse(array)