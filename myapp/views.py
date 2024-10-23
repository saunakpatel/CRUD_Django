from django.shortcuts import render,HttpResponse,redirect
from .models import*    

# Create your views here.
print("hello")
print("123")

def crud(request):
    return render(request,"crud.html")
    # return HttpResponse("hellooo")


    
def Create(request):
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"]
        address=request.POST["address"]
        phone=request.POST["phone"]

        Contact.objects.create(name=name,email=email,address=address,phone=phone)

        return redirect("read")
    else:
        return render(request,"crud.html")


def read(request):
    uid=Contact.objects.all()
    context={"uid":uid}
    return render(request,"crud.html",context)



def update(request,id):
    uid=Contact.objects.get(id=id)
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"]
        address=request.POST["address"]
        phone=request.POST["phone"]

        uid.name=name
        uid.email=email
        uid.address=address
        uid.phone=phone
        uid.save()
        return redirect("read")
    else:
        return render(request,"crud.html")

def Delete(request,id):
    uid=Contact.objects.get(id=id)
    uid.delete()
    return redirect("read")

