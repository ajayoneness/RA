from django.shortcuts import render
from .models import category,quotes,contactform


def index(request):

    if request.method == "POST":
        try:
            name= request.POST['ra']
            request.session['stored_text'] = name
        except:
            form_name = request.POST['name']
            form_email = request.POST['email']
            form_message = request.POST['message']

            contactform(name=form_name,email=form_email, message=form_message).save()





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



