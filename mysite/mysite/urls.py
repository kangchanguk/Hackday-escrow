"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from user.views import UserRegistrationView
from user.views import UserLoginView
from blog.views import refund,person,incount,confirm, upload_file,show,trade, delete,detail,ProductListView,upload_info,deliver,sendmoney
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('up/',upload_file),
    path('<product_id>/', detail,name='detail'),

    path('<product_id>/delete/',delete,name='delete'),
    path('',show,name="show"),
    path('1/p/',person,name="person"),
    path('user/create/', UserRegistrationView.as_view(),name="create"),
    path('user/login/', UserLoginView.as_view(),name="login"),
    path('user/logout/',LogoutView.as_view(),name="logout"),
    path('<product_id>/trade/',trade,name="info"),
    path('<product_id>/deliver/',deliver, name="deliver"),
    path('<product_id>/check/',sendmoney,name="sendmoney"),
    path('<product_id>/confirm/',confirm,name="confirm"),
    path('<product_id>/confirm/refund/',refund,name="refund"),
    path('<product_id>/confirm/incount/',incount,name="incount")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)