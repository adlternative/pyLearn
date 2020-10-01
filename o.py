print('age', 42, 'asad', 'sdasd', sep='!')
print('age', 42, 'asad', 'sdasd', end='!')
print('hello', end='')
print('sad')
papa = {'sad': 1, 'sda': '3'}
a, b, *rest = [1, 2, 3, 3, 3]
a, *rest, b = (1, 2, 3, 3, 3)
print(rest)
name = "say good bye sadjlasd adsjlsk ja"
asd, casc, *c, sca = name.split(' ')
print(c)
# print(() == False)
print(() == {})
print(() == '')
a = list("['bye', 'sadjlasd', 'adsjlsk']")
print(a)

# while True:
# 	word = input("please input a word:")
# 	if not word :break
#  	print("the word is :",word)
for n in range(99, 81, -1):
    if(n % 2 == 0):
        print(1)

        # break
else:
    print("so cute so sad")


girls = ['ads', 'a', 'asdas']
boys = ['ads', 'aas', 'asdas']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])
