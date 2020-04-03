from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.



class UploadFileModel(models.Model):
    file = models.ImageField(null=True)
    filename=models.CharField('파일명',max_length=200,default='')
    user_id= models.CharField('등록자',max_length=100,default='')
    trader_id=models.CharField('거래자',max_length=100,default='')
    material_name=models.CharField('이름',max_length=100,default='')
    price= models.IntegerField('가격',default=0)
    explain=models.CharField('제품설명',max_length=400,default='')
    inputmoney=models.BooleanField('입금여부',default=False)
    delivery=models.BooleanField('배송여부',default=False)
    ontrade=models.BooleanField('거래여부',default=False)
    trade_date=models.DateTimeField('거래 시작일',default=timezone.now, blank=True)
    success=models.BooleanField('거래 성사여부',default=True)
    finish=models.BooleanField('거래 완료 여부',default=False)



class Money(models.Model):
    num= models.IntegerField('번호',default=0)
    account= models.IntegerField('계좌',default=0)

class info(models.Model):
    receiver = models.CharField('받을 사람',max_length=100,default='',blank=True)
    phone = models.CharField('휴대폰 번호',max_length=100,default='',blank=True)
    addressnum= models.TextField('우편번호',null=True,blank=True)
    address = models.TextField('주소',null=True,blank=True)
    detailaddress = models.TextField('상세주소',null=True,blank=True)
    addition = models.TextField('참고목록',null=True,blank=True)
    request = models.TextField('주의 사항',null=True,blank=True)
    num=models.IntegerField('거래항목',null=True,blank=True)

class check(models.Model):
    photo = models.ImageField('배송사진',null=True)
    photoname=models.CharField('파일명',max_length=200,default='')
    num = models.IntegerField('번호',default=0)