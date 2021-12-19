import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User,Question,History,Category
from django.db.models import Q
import random

def show(request,name1):
    db_dict_kol={}
    id=User.objects.filter(name=name1).values_list("id",flat=True)
    obj=History.objects.all()
    for j in Category.objects.all():
        result=j.Questocat.all()       
        result=list(result)
        sample=random.sample(result,4)
        for i in sample:
            db_dict={}
            db_dict["question"]=i.title
            db_dict["A)"]=i.cs1
            db_dict["B)"]=i.cs2
            db_dict["C)"]=i.cs3
            db_dict["D)"]=i.cs4
            db_dict_kol[i.id]=db_dict


    for i in obj:
        if i.user==id[0]:
            if i.quiz == db_dict_kol:
                show(request,name1) 
            else:
                obj_H=History.objects.create(quiz=db_dict_kol,user=id[0]) 
                return JsonResponse({obj_H.id:db_dict_kol})

    else:

        obj_H=History.objects.create(quiz=db_dict_kol,user=id[0]) 
        return JsonResponse({obj_H.id:db_dict_kol})

        
    

         


@csrf_exempt
def check(request,name,id_az):
    count=0
    javab=json.loads(request.body)
    obj=Question.objects.all()
    for i in javab:
        for j in obj:
            if j.id==int(i):
                if j.select==javab[i]:
                    count+=1

    id=User.objects.filter(name=name).values_list("id",flat=True)
    History.objects.filter(Q(user=id[0])&Q(id=id_az)).update(point=count)
    return HttpResponse(str(count))
