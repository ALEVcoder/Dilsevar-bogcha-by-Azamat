from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def HomeContact(request):
    if request.method == 'POST':
        ism = request.POST['name']
        familya = request.POST['fname']
        xabar = request.POST['mess']
        tel = request.POST['tel']
        title=ism
        msg='Sizga '+familya+' '+ism+'dan xabar bor'+'\nTelefon nomeri: '+tel+'\nXabari:\n'+xabar

        print(ism, xabar, tel)
        send_mail(
            ism,
            msg,
            tel,
            ['malikaegamquluva@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Gallery(request):
    return render(request, 'galery.html')

def News(request):
    return render(request, 'news.html')

def Contact(request):
    if request.method == 'POST':
        ism = request.POST['name']
        familya = request.POST['fname']
        xabar = request.POST['mess']
        tel = request.POST['tel']
        title=ism
        msg='Sizga '+familya+' '+ism+'dan xabar bor'+'\nTelefon nomeri: '+tel+'\nXabari:\n'+xabar

        print(ism, xabar, tel)
        send_mail(
            ism,
            msg,
            tel,
            ['malikaegamquluva@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'contact.html')