from django.shortcuts import render, HttpResponse #(1)
from django.shortcuts import render, redirect
from django.http import JsonResponse    #(15)
from .forms import ContactForm  #(15)

# Create your views here.
def home(request): #(1)
    #return HttpResponse("Hello World!") #(1)
    return render(request, "index.html") #(2)

def aboutme(request): #(3)
    return render(request, "aboutme.html") #(3)

def childCounselling(request): #(4)
    return render(request, "1child.html") #(4)

def coupleCounselling(request): #(5)
    return render(request, "2couple.html") #(5)

def groupCounselling(request): #(6)
    return render(request, "3group.html") #(6)

def narcissm(request): #(7)
    return render(request, "4narcissm.html") #(7)

def selfFree(request): #(8)
    return render(request, "5selffree.html") #(8)

def breakTrauma(request): #(3)
    return render(request, "6breaktrauma.html") #(9)

def detachment(request): #(9)
    return render(request, "7detachment.html") #(3)

def parentNarcisst(request): #(10)
    return render(request, "8parentnarcist.html") #(10)

def gut(request): #(11)
    return render(request, "9gut.html") #(11)

def anxiety(request): #(12)
    return render(request, "10anxiety.html") #(12)

def toxic(request): #(13)
    return render(request, "11toxic.html") #(13)

def selfEsteem(request): #(14)
    return render(request, "12esteem.html") #(14)


# user details submission block-CODE (15)

def home(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})

def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('counApp:contact_thanks') # Redirect to thanks page (you can show a success message instead)
        else:
            return render(request, 'index.html', {'form': form})# re-render the form with errors
    return redirect('counApp:home')

# def submit_contact_ajax(request):
#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             obj = form.save()
#             return JsonResponse({'status': 'ok', 'id': obj.id})
#         return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=405)

def contact_thanks(request):
    return render(request, 'thanks.html')
