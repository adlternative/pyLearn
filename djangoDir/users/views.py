import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
import logging,time
def logout_view(request):
    """ 注销用户 """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """ 注册新用户 """
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)  # Log等级总开关
        # # 第二步，创建一个handler，用于写入日志文件
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        # log_name = log_path + rq + '.log'
        # logfile = log_name
        # fh = logging.FileHandler(logfile, mode='w+')
        # fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # # 第三步，定义handler的输出格式
        # formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        # fh.setFormatter(formatter)
        # # 第四步，将logger添加到handler里面
        # logger.addHandler(fh)
        # logger.debug("this is a this")
        # # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录,再重定向到主页
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

