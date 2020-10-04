#Newton Raphson
import math

#input function 1
def fxn_1(x):
    f=math.log(abs(x),10)-math.sin(x)
    return f
   
#input function 2
def fxn_2(x):
    f=-x-math.cos(x)
    return f
   
#first derivative for fxn 2
def derivative1(x):
    d=-1+(math.sin(x))
    return d
   
   
#first derivative for fxn 1
def derivative(x):
    d=(1/x)-(math.cos(x))
    return d
   
   
#Newton raphson for fxn 1
def newton_raphson(a):
    i=0
    arr1=[]
    index=[]
    if abs(fxn_1(a)/derivative(a))>0.00001:
        while i<6:
            index.append(i)
            arr1.append(abs(fxn_1(a)/derivative(a)))
            a=a-(fxn_1(a)/derivative(a))
           
            i=i+1
    else:
        print('Root found')
   
    #print(arr1)
    names = ['index']
    values = ['value']
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
   
    names = index
    values = arr1
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
        
    #print(*values, sep = "\n")
        
   
   
    return a
   
#Newton raphson for fxn 2
def newton_raphson1(a):
    i=0
    index=[]
    arr2=[]
    if abs(fxn_2(a)/derivative1(a))>0.00001:
        while i<3:
            index.append(i)
            arr2.append(abs(fxn_2(a)/derivative1(a)))
            a=a-(fxn_2(a)/derivative1(a))
           
            i=i+1
    else:
        print('Root found')
       
    #print(arr2)
    names = ['index']
    values = ['value']
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
   
    names = index
    values = arr2
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
        
        
    #print(*arr2, sep = "\n")
   
   
    return a
       
       

#Newton Raphson for fxn 1, guess=3.5
c=newton_raphson(1.5)
print('The root of the given function logx-sinx is: ')
print(c)

#Newton Raphson for fxn 2, guess=-2
d=newton_raphson1(-2)
print('The root of the given function -x-cosx is: ')
print(d)


'''
index = value
0 = 1.3783572986272823
1 = 0.15151781705124492
2 = 0.02550471390725489
3 = 0.004240281606685617
4 = 0.0006998250854078958
5 = 0.0001153427583110593
The root of the given function logx-sinx is: 
2.6962793182183775
index = value
0 = 1.2654638311455368
1 = 0.004553555350906221
2 = 4.5909855547866925e-06
The root of the given function -x-cosx is: 
-0.7390851332198145



 
 '''

