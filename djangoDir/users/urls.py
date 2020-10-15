from django.conf.urls import url
from django.contrib.auth import login
urlpatterns = [
    # 主页
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
]

app_name = 'users'
