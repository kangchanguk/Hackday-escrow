from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.http import HttpResponse
from user.forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages

class UserRegistrationView(CreateView):
    template_name="user/user_form.html"
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/'

class UserLoginView(LoginView):           # 로그인
    template_name = 'user/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다. id,pw를 확인해주세요', extra_tags='danger')
        return super().form_invalid(form)    



