from django.shortcuts import render

def calculator(requests):
    return render(requests,"index.html")