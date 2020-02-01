from django.shortcuts import render
from django.http import HttpResponse
import operator


def index(request):
    return render(request, 'index.html')

def count(request):
    textadd = request.GET['textadd']

    wordlist = textadd.split()

   

    return render(request, 'count.html', {'textadd':textadd,'counter':len(wordlist)} )