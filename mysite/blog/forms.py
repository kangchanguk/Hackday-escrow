from django import forms

from .models import UploadFileModel, Money, info, check


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('material_name', 'file','price','explain')

class arbitary(forms.ModelForm):
    class Meta:
        model = Money
        fields = ()

class tradeinfo(forms.ModelForm):
    class Meta:
        model = info
        fields = ('phone','addressnum','address','detailaddress','addition','request')

class checkform(forms.ModelForm):
    class Meta:
        model = check
        fields = ('photo',)