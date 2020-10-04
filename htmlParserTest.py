from html.parser import  HTMLParser

def decodeHtml(input):
    h = HTMLParser()
    s = h.unescape(input)
    return s
if __name__ == '__main__':
  print(decodeHtml('asd&#20013;&#21320;'))
