from collections import deque
def my_function():
     '''home homie\n
        we  are happy here'''
#print(my_function.__doc__)

def functon(prompt, home="shit"):
    value = input(prompt)
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

vec = [-4, -2, 0, 2, 4]

vec= [x for x in vec if x>=0]
print (vec)

tupes = ('home',)
print(len(tupes))