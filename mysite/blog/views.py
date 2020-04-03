from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from blog.models import UploadFileModel,Money,info,check
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from blog.forms import UploadFileForm,arbitary,tradeinfo,checkform
from django.contrib import messages
from user.models import User
import os
import shutil
from PIL import Image
from django.utils import timezone

def upload_info(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        form1= tradeinfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = tradeinfo()
    return render(request, 'blog/trade.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        form1= arbitary(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.filename=request.FILES['file'].name
            post.user_id=request.user.get_username()
            post.save()
            post1= form1.save(commit=False)
            post1.num=post.id
            post1.account=0
            post1.save()
            
            return redirect('show')
    else:
        form = UploadFileForm()
    return render(request, 'blog/uploaded.html', {'form': form})

def ProductListView(request):         # 게시글 목록
    queryset = UploadFileModel.objects.all()  
    return render(request,'blog/home.html',{'products': queryset})


def detail(request, product_id):
    memo = UploadFileModel.objects.get(pk = product_id)
    day=(timezone.localtime() - memo.trade_date).days
    if memo.ontrade == True and memo.delivery == True:
        note=check.objects.get(num=product_id)
        return render(request,'blog/detail.html',{'memo': memo,'photo':'blog/images/'+str(memo.file),'photo1':'blog/images/'+str(note.photo)})
    else:
        chang=str(memo.file)
        shutil.copy('media/'+str(memo.file),'blog/static/blog/images')
        im = Image.open('blog/static/blog/images/'+str(memo.file))
        width,height = im.size
        resize_image = im.resize((int(height*1.6),height))
        resize_image.save('blog/static/blog/images/'+str(memo.file))
        
        return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})


def delete(request, product_id):
    memo = UploadFileModel.objects.get(pk = product_id)
    
    if memo.user_id == request.user.get_username() and memo.ontrade == False:
        money = Money.objects.get(num= product_id)
        memo.delete()
        money.delete()
        messages.add_message(request, messages.INFO, '삭제되었습니다')
        return redirect('show')
    else:
        messages.error(request, 'YOU CANT DELETE SECTION')
        day=(timezone.localtime()-memo.trade_date).days
        return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})


def show(request):
    queryset = UploadFileModel.objects.all()  
    if request.user.get_username() != '':
        
        us = User.objects.get(email=request.user.get_username())
        day=timezone.localtime()
        return render(request,'blog/home.html',{'products': queryset,'use':us,'time':day})
    else:
        return render(request,'blog/home.html',{'products': queryset})

def trade(request, product_id):
    memo= UploadFileModel.objects.get(pk=product_id)
    if request.user.get_username() != "":
        person=User.objects.get(email=request.user.get_username())
        mom= Money.objects.get(num=product_id)
        if person.point >= memo.price and memo.ontrade == False:
            if request.method == 'POST':
                form= tradeinfo(request.POST)
                if form.is_valid():
                    post=form.save(commit=False)
                    post.receiver=request.user.get_username()
                    post.num=product_id
                    post.save()
                    mom.account=memo.price
                    mom.save()
                    memo.ontrade=True
                    memo.trade_date=timezone.localtime()
                    memo.trader_id=request.user.get_username()
                    memo.save()
                    person.point=person.point-memo.price
                    person.save()
                    day=(timezone.localtime()-memo.trade_date).days
                    return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})
                else:
                    print(form.errors)
            else:
                form = tradeinfo()
            return render(request, 'blog/trade.html', {'form': form})
        else:

            messages.add_message(request,messages.INFO,'거래가 불가 하십니다')
            day=(timezone.localtime()-memo.trade_date).days
            return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})
    else:
        messages.add_message(request,messages.INFO,'로그인 후 이용해주시기 바랍니다')
        day=(timezone.localtime()-memo.trade_date).days
        return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})
        


def deliver(request, product_id):
    memo=UploadFileModel.objects.get(pk=product_id)
    if request.user.get_username() != "":
        add=info.objects.get(num=product_id)
        if memo.ontrade==True and request.user.get_username()==memo.user_id and memo.delivery==False:
            if request.method == 'POST':
                form = checkform(request.POST,request.FILES)
                if form.is_valid():
                    post=form.save(commit=False)
                    post.photoname=request.FILES['photo']
                    post.num=memo.pk
                    memo.delivery=True
                    memo.save()
                    post.save()
                    note=check.objects.get(num=product_id)
                    shutil.copy('media/'+str(note.photo),'blog/static/blog/images')
                    im = Image.open('blog/static/blog/images/'+str(note.photo))
                    width,height = im.size
                    resize_image = im.resize((int(height*1.6),height))
                    resize_image.save('blog/static/blog/images/'+str(note.photo))
                    return render(request,'blog/detail.html',{'memo': memo,'photo':'blog/images/'+str(memo.file),'photo1':'blog/images/'+str(note.photo)})
            else:
                form=checkform()
            return render(request, 'blog/deliver.html',{'form':form , 'add':add})        
        elif memo.ontrade==True and request.user.get_username()==memo.user_id and memo.delivery==True:
            note=check.objects.get(num=product_id)
            day=(timezone.localtime()-memo.trade_date).days
            return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file),'photo1':'blog/images/'+str(note.photo)})
        else:
            messages.add_message(request,messages.INFO,'배송이 불가 하십니다')
            day=(timezone.localtime()-memo.trade_date).days
            return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})
    else:
        messages.add_message(request,messages.INFO,'로그인 후 이용해주시기 바랍니다')
        day=(timezone.localtime()-memo.trade_date).days
        return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)});


def sendmoney(request, product_id):
    try:
        note=check.objects.get(num=product_id)
        mom=Money.objects.get(num=product_id)
        memo=UploadFileModel.objects.get(pk=product_id)
        reg=User.objects.get(email=memo.user_id)
        ifm=info.objects.get(num=product_id)
        if memo.trader_id==request.user.get_username():
            reg.point=reg.point+mom.account
            reg.save()
            memo.finish=True
            memo.save()
            messages.add_message(request,messages.INFO,'거래가 완료되었습니다.')
            return redirect('show')
        else:
            messages.add_message(request,messages.INFO,'권한이 없으십니다')
            day=(timezone.localtime()-memo.trade_date).days
            return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})
    except:
        memo=UploadFileModel.objects.get(pk=product_id)
        day=(timezone.localtime()-memo.trade_date).days
        messages.add_message(request,messages.INFO,'다시 확인하시고 입금하시기 바랍니다')
        return render(request,'blog/detail.html',{'day':day, 'memo': memo,'photo':'blog/images/'+str(memo.file)})

def confirm(request,product_id):
    memo=UploadFileModel.objects.get(pk=product_id)
    note=check.objects.get(num=product_id)
    us=User.objects.get(email=request.user.get_username())
    day=(timezone.localtime()-memo.trade_date).days
    if us.is_staff==True:
        if day >=0:
            return render(request,'blog/confirm.html',{'memo': memo,'photo':'blog/images/'+str(memo.file),'photo1':'blog/images/'+str(note.photo)})
        else:
            messages.add_message(request,messages.INFO,'배송 허용 기간을 넘지 않았습니다.')
            day=(timezone.localtime()-memo.trade_date).days
            return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})

    else:
        messages.add_message(request,messages.INFO,'권한이 없으십니다')
        day=(timezone.localtime()-memo.trade_date).days
        return render(request,'blog/detail.html',{'day':day,'memo': memo,'photo':'blog/images/'+str(memo.file)})

def refund(request,product_id):
    memo=UploadFileModel.objects.get(pk=product_id)
    us=User.objects.get(email=memo.trader_id)
    mom=Money.objects.get(num=product_id)
    us.point=us.point+mom.account
    mom.account=0
    us.save()
    mom.delete()
    memo.finish=True
    memo.save()
    messages.add_message(request,messages.INFO,'환급 조치 되었습니다')
    return redirect('show')

def incount(request,product_id):
    memo=UploadFileModel.objects.get(pk=product_id)
    us=User.objects.get(email=memo.user_id)
    mom=Money.objects.get(num=product_id)
    us.point=us.point+mom.account
    us.save
    memo.finish=True
    memo.success=False
    memo.save()
    messages.add_message(request,messages.INFO,'입금 조치 되었습니다')
    return redirect('show')

def person(request):
    queryset = UploadFileModel.objects.all()
    us=User.objects.get(email=request.user.get_username())
    use=us.email
    return render(request,'blog/person.html',{'products': queryset,'us':us,'use':use})

