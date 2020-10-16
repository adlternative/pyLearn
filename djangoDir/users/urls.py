from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    # 主页
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),name = 'login'),
    # url(r'^logout/$', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^register/$', views.register, name='register'),
]

app_name = 'users'
