#__anthor:  "xuchen:
#date:   2018/2/6
import hashlib
import time
import random
import collections


def random_code():
    code=''
    for i in range(4):
        current=random.randrange(0,4)
        if current!=1:
            temp=chr(random.randint(65,90))
        else:
            temp=random.randint(0,9)
        code+=str(temp)
    return  code