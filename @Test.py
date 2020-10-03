def funA(desA):
 print("It's funA")

 print('---')
 print(desA)
 desA()
 print('---')

def funB(desB):
 print("It's funB")


# def funC():
#  print("It's funC")
#  return funC
# funA(funC())
@funB
@funA
def funC():
 print("It's funC")
