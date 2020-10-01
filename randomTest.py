from random import * 
from time import *
from pprint import pprint
""" date1 = (2016,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
date2 = (2017,1,1,0,0,0,-1,-1,-1)
time2 = mktime(date2)
random_time =uniform(time1,time2)	
print(asctime(localtime(random_time)))
 """
values =list(range(1,11))+'Jack Queen King'.split()
suits = 'diamands clubs hearts spades'.split()
deck =['{}of{}'.format(v,s)for v in values for s in suits]	
shuffle(deck)
pprint(deck[:12])

while deck: input(deck.pop())
