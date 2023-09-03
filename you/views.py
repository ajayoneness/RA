from django.shortcuts import render
from .models import category,quotes


def index(request):

    if request.method == "POST":
        name= request.POST['ra']
        print(name)
        request.session['stored_text'] = name

    if request.session.get('stored_text', '') == 'radha':
        cat = category.objects.all()
        return render(request, 'index.html', {'category': cat})
    else:
        return render(request,'test.html')





def singlepost(request,slug):
    cat = category.objects.get(slug=slug)
    quo = quotes.objects.filter(category=cat)
    allcat = category.objects.all()
    print(quo)
    return render(request,'single-post.html', {'quotes':quo,'categories':allcat})



