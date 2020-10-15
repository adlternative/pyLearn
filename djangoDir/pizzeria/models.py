from django.db import models

# Create your models here.
class Pizza(models.Model):
    """批萨"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.name

class Topping(models.Model):
    """配料"""
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'toppings'
    def __str__(self):
        """ 返回模型的字符串表示 """
        if len(self.name)>50:
            return self.name[:50] + "..."
        else:
            return self.name

