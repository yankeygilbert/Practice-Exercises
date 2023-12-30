from collections import deque
import math
import json
"""
def my_function():
     '''home homie\n
        we  are happy here'''
print(my_function.__doc__)


def functon( prompt= input("enter a number \n"), home='shit'):
   return lambda: print(home+" "+value)
 
a,b=2,3
lambda a,b: print(a+b)

fruits =['home','shit','gate','steve']
stack=[1,2,3,4]

queue = deque(stack)
print(queue.popleft())
squares = list(map(lambda x: x**2,range(10)))
qr = [(x,y) for x in[1,2,3] for y in[3,1,4] if x==y]
print(squares)
print(qr)

vec = [-4, 0]

vec= [x for x in vec if x>=0]
print (vec)

tel = {'jack':42,'mate':75,'doc':66}
tel['home']=100
print(tel)
print(sorted(tel))

suss = dict([(4,2),(2,100)])

print(suss)
v = set('adbcdde')
qt= set('abufusein')

print(sorted(v|qt))
"""
dicta = {x: x**2 for x in range(10)}
print(dicta)
'''
print(dict(sape=14,magor=74))

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1,11)):
    print (i)
val,vex =2,3

string=['happy me','house']
print(f'shit{val},shit2{vex}')
print('shit{0} shir2{1}'.format(val,vex))

print(repr((qt,('home','steve'))))



with open('file.txt','w') as file:
    json.dump(string,file)

file.close() 

file =  open('file.txt','r')
#json.load(file)
#print(f' {json.load(file)}')

for i in enumerate(json.load(file)):
    print('{}'.format(str(i)))

file.close()

hope ='svare'
print('{!r}'.format(hope))'''