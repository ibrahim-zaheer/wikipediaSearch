from django.shortcuts import render,HttpResponse
import wikipedia
# Create your views here.
def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        try:
            result = wikipedia.summary(search,sentences = 5)
        except:
            return HttpResponse("wrong input")    
        return render(request,'index.html',{"result":result})
    return render(request,'index.html')