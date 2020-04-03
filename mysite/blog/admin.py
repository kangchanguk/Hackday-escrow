from django.contrib import admin
from .models import UploadFileModel,Money, info, check


admin.site.register(UploadFileModel)
admin.site.register(Money)
admin.site.register(info)
admin.site.register(check)