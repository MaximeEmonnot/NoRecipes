from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from utils import RunCypher, GetDataFromNode

# Create your views here.

def data_list(request):
    if request.method == "GET":
        answer, summary, keys = RunCypher("MATCH (n:Person) RETURN n")
        
        data = [GetDataFromNode(record) for record in answer]
               
        return JsonResponse({"answer" : data})
    elif request.method == "POST":
        return JsonResponse({"answer" : "TO BE IMPLEMENTED"})
    elif request.method == "PUT":
        return JsonResponse({"answer" : "TO BE IMPLEMENTED"})
    elif request.methode == "DELETE":
        return JsonResponse({"answer" : "TO BE IMPLEMENTED"})