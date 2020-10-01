import fileinput                                  #1
import sys  # 1                                   #2
a = fileinput.input(sys.argv, inplace=True)  # 2  #3
for line in a:  # 3                               #4
    line = line.rstrip()  # 4                     #5
    num = fileinput.filelineno()  # 5             #6
    print('{:<50}#{:1d}'.format(line, num))  # 6  #7
    # 7                                           #8
# import webbrowser                               #8#9
# webbrowser.open("http://www.baidu.com")         #9#10
