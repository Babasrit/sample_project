'''def first():
    print("Hello")

a=first
a()

def second(msg):
    message=msg
    def third(t):
        
        print(message)
        print(t+3)
    return third
b=second("Python")
b(3)'''

'''def square(x):
    return x*x
a=square
def cube(a):
    return a*a*a
b=cube
def result(z,func):
    return func(z)
res=result(3,a)
res1=result(res,b)
print(res1)'''

'''def bigboss():
    print("I am in")
    print("And started")
def maa(arg):
    print("contenst")
    arg()
maa(bigboss)'''

'''def first(original):
    print("First")
    def second(*args,**kwargs):
        first.__call__+=1
        print(f"This function is executed before {original.__name__}")
        return original(*args,**kwargs)
    first.__call__=0
    #print("Total calls",first.__call__)
    return second
@first
def dispaly(name,age):
    c=0
    print("Total calls",first.__call__)
    print(f'My name is {name} and my age is {age}')
@first
def Employee(name,company,salary):
    print(f'My name is {name} i am working in {company} and my salary is {salary}')
    
    
dispaly('Babu',25)
dispaly('dfakru',24)
dispaly('dude',26)
#func=first(dispaly)
#func('dfakru',24)
print("Total",first.__call__)

Employee('Baba','Wipro',30000)'''

'''def first():
    message="complete"
    def second(t):
        print(t+3)
        print(message)
    return second()
a=first()
a(3)'''
#a()
'''def first(original):
    print("complete")
    def second(*args,**kwargs):
        
        print(f"This function is executed before {original.__name__}")
        return original(*args,**kwargs)
    
    #print("Total calls",first.__call__)
    return second
@first
def func():
    print("I am excuting")
@first
def sample(name,age,company):
    print(f'My name is {name} and my age is {age}. I am working in {company}')
#a=first(func)
#a()
func()
sample('Babu',25,'Wipro')
sample('dfakru',24,'Accenture')
sample('Baba',26,'Infosys')'''

class decorator_sample:
    c=0
    def __init__(self,original):
        self.original=original
    def __call__(self,*args,**kwargs):
        print(decorator_sample.c)
        print(f'wrapper function executed before {self.original.__name__}')
        decorator_sample.c+=1
        return self.original(*args,**kwargs)

@decorator_sample
def display(name,age,salary):
    print(f'My name is {name} and my age is {age}. I am working in {salary}')

display('babu',25,30000)
display('dfakru',24,35000)
print("total count",decorator_sample.c)
        
        
       

