```python
        bs = BeautifulSoup(html, 'lxml')
        for i in bs.find_all('a'):
            print i
```
可见find_all可以直接定位到标签<a>
```html
<a href="https://blog.csdn.net/adlatereturn/article/details/108889759">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/108732422">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/108502385">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/108356380">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/108046579">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107753159">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107335130">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107335130#comments" target="_blank">查看评论</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107286812">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107585630">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107586703">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107445014">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/107281562">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/106845518">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/106293203">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/106167280">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/105897403">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/105780480">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/105691795">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/105586921">原文链接</a>
<a href="https://blog.csdn.net/adlatereturn/article/details/105452737">原文链接</a>
```
```python
        for article in bs.findAll('a'):
           if 'href' in article.attrs:
              print(article['href'])
```        
通过　　`article['href']`可获得正确的url 
注意　使用`article.get_text()能得到后面的“原文链接”`

```
https://blog.csdn.net/adlatereturn/article/details/108889759
https://blog.csdn.net/adlatereturn/article/details/108732422
https://blog.csdn.net/adlatereturn/article/details/108502385
https://blog.csdn.net/adlatereturn/article/details/108356380
https://blog.csdn.net/adlatereturn/article/details/108046579
https://blog.csdn.net/adlatereturn/article/details/107753159
https://blog.csdn.net/adlatereturn/article/details/107335130
https://blog.csdn.net/adlatereturn/article/details/107335130#comments
https://blog.csdn.net/adlatereturn/article/details/107286812
https://blog.csdn.net/adlatereturn/article/details/107585630
https://blog.csdn.net/adlatereturn/article/details/107586703
https://blog.csdn.net/adlatereturn/article/details/107445014
https://blog.csdn.net/adlatereturn/article/details/107281562
https://blog.csdn.net/adlatereturn/article/details/106845518
https://blog.csdn.net/adlatereturn/article/details/106293203
https://blog.csdn.net/adlatereturn/article/details/106167280
https://blog.csdn.net/adlatereturn/article/details/105897403
https://blog.csdn.net/adlatereturn/article/details/105780480
https://blog.csdn.net/adlatereturn/article/details/105691795
https://blog.csdn.net/adlatereturn/article/details/105586921
https://blog.csdn.net/adlatereturn/article/details/105452737
```

中间有个很唐突的查看评论
因此我们使用
```python
        for article in bs.findAll('a',text='原文链接'):
```
排除掉查看评论

获得正确的url
```
https://blog.csdn.net/adlatereturn/article/details/108889759
https://blog.csdn.net/adlatereturn/article/details/108732422
https://blog.csdn.net/adlatereturn/article/details/108502385
https://blog.csdn.net/adlatereturn/article/details/108356380
https://blog.csdn.net/adlatereturn/article/details/108046579
https://blog.csdn.net/adlatereturn/article/details/107753159
https://blog.csdn.net/adlatereturn/article/details/107335130
https://blog.csdn.net/adlatereturn/article/details/107286812
https://blog.csdn.net/adlatereturn/article/details/107585630
https://blog.csdn.net/adlatereturn/article/details/107586703
https://blog.csdn.net/adlatereturn/article/details/107445014
https://blog.csdn.net/adlatereturn/article/details/107281562
https://blog.csdn.net/adlatereturn/article/details/106845518
https://blog.csdn.net/adlatereturn/article/details/106293203
https://blog.csdn.net/adlatereturn/article/details/106167280
https://blog.csdn.net/adlatereturn/article/details/105897403
https://blog.csdn.net/adlatereturn/article/details/105780480
https://blog.csdn.net/adlatereturn/article/details/105691795
https://blog.csdn.net/adlatereturn/article/details/105586921
https://blog.csdn.net/adlatereturn/article/details/105452737
```