while(1):

    id, hours = eval(input("输入工号，工时\n"))

    sum = 0
    if hours > 120:
        sum += 80 * 120 + 1.15 * (hours - 120)
    elif hours < 60:
        sum += 80 * hours - 60
    else:
        sum+=80*hours
    print("你的工资是%.2f"%sum)