from handlers import HTMLRenderer
import re
handler = HTMLRenderer()

# print(handler.sub('emphasis'))
#re.sub得到的东西将传递给handler.substitution(match) 其中会调用HTMLRenderer.sub_emphasis(match),可见函数的适配器是为了统一格式，却能够实现调用不同参数的作用　start 0，sub１
print(re.sub(r'\*(.+?)\*',handler.sub('emphasis'),'this *是 *a test'))
#子类需要满足父类的函数规范，即只传入一个参数（子类函数名字），且会返回一个需要一个参数的函数其中接着调用子类的函数,子类的函数会接住参数，所以子类接口需要设计成(self,arg) 不同的子类都需要这个条件
# 这里及对正则得到的字串matchObj进行相应的处理，也就是统一的接口handler.bbb('xxx')可以当作无参数函数也可当作有参数的函数，用起来统一