from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = ""

#show chat page
def chat(request):
    return render(request, "index.html")

#API to return JSON response
def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST["prompt"]
        # response = {"postTest" : "test"}
        # print(prompt)
        
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        # print(response)

        return JsonResponse(response)
    
    return HttpResponse("Bad request!")
