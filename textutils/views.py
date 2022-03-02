# I have created this file - Shlok

from django.http import HttpResponse
from django.shortcuts import render

def index(request) :
    return render(request, 'index.html')

def analyze(request) :
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check box values
    removepunc = request.POST.get('removepunc','off')
    captext = request.POST.get('captext','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount', 'off')
    purpose = ""
    analyzed = djtext
    if removepunc == 'on' :
        tempanalyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in analyzed :
            if char not in punctuations :
                tempanalyzed+= char
        purpose += "| Remove Puntuations |"
        analyzed = tempanalyzed
    if captext== 'on' :
        analyzed = analyzed.upper()
        purpose += "| Capitalize text |"
    if newlineremover =="on" :
        tempanalyzed =""
        for char in analyzed:
            if char != '\n' and char != '\r':
                tempanalyzed += char
        purpose += "| Remove new line |"
        analyzed = tempanalyzed
    if spaceremover == "on" :
        tempanalyzed = ""
        for char in analyzed:
            if char!= " " :
                tempanalyzed += char
        purpose += "| Remove spaces |"
        analyzed = tempanalyzed
    if extraspaceremover == "on" :
        tempanalyzed = ""
        for index,char in enumerate(analyzed) :
            if not(analyzed[index] ==" " and analyzed[index+1] == " ") :
                tempanalyzed+= char
        purpose += "| Remove Extra spaces |"
        analyzed = tempanalyzed
    if charcount == "on" :
        count = len(djtext)
        print(count)
        return render(request,"analyze.html", params)
    params = {'purpose' : purpose , 'analyzed_text' : analyzed}
    if removepunc == 'on' or captext== 'on' or newlineremover =="on" or spaceremover == "on" or extraspaceremover == "on" or charcount == "on" :
        return render(request, "analyze.html",params)
    else :
        return HttpResponse("Error")



