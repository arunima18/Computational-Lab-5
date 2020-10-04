import math

#input function 1 
def fxn_1(x):
    f=math.log(x,10)-math.sin(x)
    return f 


#input function 2
def fxn_2(x):
    f=-x-math.cos(x)
    return f


#Bracketing  
def bracket(f_a,f_b,a,b):
    c=0
    y1=f_a
    y2=f_b
    if (y1*y2)>0:
        if abs(y1)<abs(y2):
            a=a-(0.5*(b-a))
        else:
            b=b+(0.5*(b-a))
    else:
        print("Bracketing already done!")
    return a,b
    
    
#bisection method for fxn 1 
def bisection(a,b):
    arr=[(b-a)]
    index=[1]
    c=(a+b)/2
    i=0
    y1=fxn_1(a)
    y2=fxn_1(b)
    y3=fxn_1(c)
    if (b-a)>0.0001:
        while i<=100:
            c=(a+b)/2
            y1=fxn_1(a)
            y2=fxn_1(b)
            y3=fxn_1(c)
            #print(c)
            if y1*y3<0:
                b=c
                #print(b)
                i=i+1
            else:
                a=c
                #print(a)
                i=i+1
            arr.append(a-b)
            index.append(i)
        
    else:
        print("Root found! ")
        
    #print(arr)
    #print(index)
    print('Table 1 showing iteration number against the absolute values for logx-sinx by bisection method : ')
    names = ['index']
    values = ['error']
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
    
    names = index
    values = arr
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
    
    #print(*values, sep = "\n")
    
    return a,b
    
    
#Regula falsi for fxn 1 
def reg_falsi(a,b):
    index=[1]
    i=0
    y1=fxn_1(a)
    y2=fxn_1(b)
    c=b-(y2*(b-a)/(y2-y1))
    y3=fxn_1(c)
    arr=[y3]
    if abs(y3)>0.000001:
        while i<=20:
            y1=fxn_1(a)
            y2=fxn_1(b)
            c=b-(y2*(b-a)/(y2-y1))
            y3=fxn_1(c)
            if y1*y3<0:
                b=c
                i=i+1
            else:
                a=c
                i=i+1
            arr.append(abs(y3))
            index.append(i)
    else:
        print('Root found! ')
    
    #print(arr)
    #print(index)
    print('Table 2 showing iteration number against the absolute values for logx-sinx by regula falsi method: ')
    names = ['index']
    values = ['error']
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
    
    names = index
    values = arr
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
        
    #print(*values, sep = "\n")
    return c
    
    
#bisection method for fxn 2 
def bisection1(a,b):
    arr=[(b-a)]
    index=[1]
    c=(a+b)/2
    i=0
    y1=fxn_2(a)
    y2=fxn_2(b)
    y3=fxn_2(c)
    if (b-a)>0.0001:
        while i<=100:
            c=(a+b)/2
            y1=fxn_2(a)
            y2=fxn_2(b)
            y3=fxn_2(c)
            #print(c)
            if y1*y3<0:
                b=c
                #print(b)
                i=i+1
            else:
                a=c
                #print(a)
                i=i+1
            arr.append(abs(a-b))
            index.append(i)
        
    else:
        print("Root found! ")
        
    #print(arr)
    #print(index)
    print('Table 3 showing iteration number against the absolute values for -x-cosx by bisection method: ')
    names = ['index']
    values = ['error']
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
    
    names = index
    values = arr
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
        
    #print(*values, sep = "\n")
    return a,b
    
    
#Regula falsi for fxn2
def reg_falsi1(a,b):
    index=[1]
    i=0
    y1=fxn_2(a)
    y2=fxn_2(b)
    c=b-(y2*(b-a)/(y2-y1))
    y3=fxn_2(c)
    arr=[y3]
    if abs(y3)>0.000001:
        while i<=20:
            y1=fxn_2(a)
            y2=fxn_2(b)
            c=b-(y2*(b-a)/(y2-y1))
            y3=fxn_2(c)
            if y1*y3<0:
                b=c
                i=i+1
            else:
                a=c
                i=i+1
            arr.append(abs(y3))
            index.append(i)
    else:
        print('Root found! ')
    
    #print(arr)
    #print(index)
    print('Table 4 showing iteration number against the absolute values for -x-cosx by regula falsi method: ')
    names = ['index']
    values = ['error']
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
    
    names = index
    values = arr
    for n, v in zip(names, values):
        print("{} = {}".format(n, v))
        
    #print(*values, sep = "\n")  
    return c
    

    
    
    
   
    
#Main function  

#Bracketing for function 1 
a,b=bracket(fxn_1(1.5),fxn_1(2.5),1.5,2.5)
print('The bracketed values for logx-sinx are: ')
print(a)
print(b)
#Bisection for function 1 
c,d=bisection(a,b)
print('Root of the function logx-sinx came out to be: ')
print(c)
print(d)
print('The functional value of logx-sinx calculated at the root is: ')
print(fxn_1(c))
print(fxn_1(d))
#Regula falsi for function 1 
e=reg_falsi(a,b)
print('The root of log-sinx using regula falsi came out to be: ')
print(e)
f=fxn_1(e)
print('The functional value of logx-sinx at the calculated root is: ')
print(f)

#Bracketing for function 2
g,h=bracket(fxn_2(-2),fxn_2(-1),-2,-1)
print('The bracketed values for -x-cosx are: ')
print(g)
print(h)

#Bisection for function 2 
i,j=bisection1(g,h)
print('The root of -x-cosx using bisection method came out to be: ')
print(i)
print(j)
print('The functional value of -x-cosx at the calculated roots is:')
print(fxn_2(i))
print(fxn_2(j))
#regula falsi for function 2 
k=reg_falsi1(g,h)
print('The root of -x-cosx using regula falsi came out to be: ')
print(k)
print('The functional value of -x-cosx at the calculated root is: ')
print(fxn_2(k))






'''The bracketed values for logx-sinx are: 
1.5
3.0
Table 1 showing iteration number against the absolute values for logx-sinx by bisection method : 
index = error
1 = 1.5
1 = -0.75
2 = -0.375
3 = -0.1875
4 = -0.09375
5 = -0.046875
6 = -0.0234375
7 = -0.01171875
8 = -0.005859375
9 = -0.0029296875
10 = -0.00146484375
11 = -0.000732421875
12 = -0.0003662109375
13 = -0.00018310546875
14 = -9.1552734375e-05
15 = -4.57763671875e-05
16 = -2.288818359375e-05
17 = -1.1444091796875e-05
18 = -5.7220458984375e-06
19 = -2.86102294921875e-06
20 = -1.430511474609375e-06
21 = -7.152557373046875e-07
22 = -3.5762786865234375e-07
23 = -1.7881393432617188e-07
24 = -8.940696716308594e-08
25 = -4.470348358154297e-08
26 = -2.2351741790771484e-08
27 = -1.1175870895385742e-08
28 = -5.587935447692871e-09
29 = -2.7939677238464355e-09
30 = -1.3969838619232178e-09
31 = -6.984919309616089e-10
32 = -3.4924596548080444e-10
33 = -1.7462298274040222e-10
34 = -8.731149137020111e-11
35 = -4.3655745685100555e-11
36 = -2.1827872842550278e-11
37 = -1.0913936421275139e-11
38 = -5.4569682106375694e-12
39 = -2.7284841053187847e-12
40 = -1.3642420526593924e-12
41 = -6.821210263296962e-13
42 = -3.410605131648481e-13
43 = -1.7053025658242404e-13
44 = -8.526512829121202e-14
45 = -4.263256414560601e-14
46 = -2.1316282072803006e-14
47 = -1.0658141036401503e-14
48 = -5.329070518200751e-15
49 = -2.6645352591003757e-15
50 = -1.3322676295501878e-15
51 = -4.440892098500626e-16
52 = -4.440892098500626e-16
53 = -4.440892098500626e-16
54 = -4.440892098500626e-16
55 = -4.440892098500626e-16
56 = -4.440892098500626e-16
57 = -4.440892098500626e-16
58 = -4.440892098500626e-16
59 = -4.440892098500626e-16
60 = -4.440892098500626e-16
61 = -4.440892098500626e-16
62 = -4.440892098500626e-16
63 = -4.440892098500626e-16
64 = -4.440892098500626e-16
65 = -4.440892098500626e-16
66 = -4.440892098500626e-16
67 = -4.440892098500626e-16
68 = -4.440892098500626e-16
69 = -4.440892098500626e-16
70 = -4.440892098500626e-16
71 = -4.440892098500626e-16
72 = -4.440892098500626e-16
73 = -4.440892098500626e-16
74 = -4.440892098500626e-16
75 = -4.440892098500626e-16
76 = -4.440892098500626e-16
77 = -4.440892098500626e-16
78 = -4.440892098500626e-16
79 = -4.440892098500626e-16
80 = -4.440892098500626e-16
81 = -4.440892098500626e-16
82 = -4.440892098500626e-16
83 = -4.440892098500626e-16
84 = -4.440892098500626e-16
85 = -4.440892098500626e-16
86 = -4.440892098500626e-16
87 = -4.440892098500626e-16
88 = -4.440892098500626e-16
89 = -4.440892098500626e-16
90 = -4.440892098500626e-16
91 = -4.440892098500626e-16
92 = -4.440892098500626e-16
93 = -4.440892098500626e-16
94 = -4.440892098500626e-16
95 = -4.440892098500626e-16
96 = -4.440892098500626e-16
97 = -4.440892098500626e-16
98 = -4.440892098500626e-16
99 = -4.440892098500626e-16
100 = -4.440892098500626e-16
101 = -4.440892098500626e-16
Root of the function logx-sinx came out to be: 
2.696256562717602
2.6962565627176023
The functional value of logx-sinx calculated at the root is: 
-2.220446049250313e-16
2.7755575615628914e-16
Table 2 showing iteration number against the absolute values for logx-sinx by regula falsi method: 
index = error
1 = -0.13654525780927884
1 = 0.13654525780927884
2 = 0.006254210986216535
3 = 0.00024312237060686304
4 = 9.37915997228922e-06
5 = 3.61721259223291e-07
6 = 1.3950158750386521e-08
7 = 5.380023093692898e-10
8 = 2.0748625040312163e-11
9 = 8.003042673010441e-13
10 = 3.091971123581061e-14
11 = 1.1657341758564144e-15
12 = 2.220446049250313e-16
13 = 2.220446049250313e-16
14 = 2.220446049250313e-16
15 = 2.220446049250313e-16
16 = 2.220446049250313e-16
17 = 2.220446049250313e-16
18 = 2.220446049250313e-16
19 = 2.220446049250313e-16
20 = 2.220446049250313e-16
21 = 2.220446049250313e-16
The root of log-sinx using regula falsi came out to be: 
2.696256562717602
The functional value of logx-sinx at the calculated root is: 
-2.220446049250313e-16
The bracketed values for -x-cosx are: 
-2
-0.5
Table 3 showing iteration number against the absolute values for -x-cosx by bisection method: 
index = error
1 = 1.5
1 = 0.75
2 = 0.375
3 = 0.1875
4 = 0.09375
5 = 0.046875
6 = 0.0234375
7 = 0.01171875
8 = 0.005859375
9 = 0.0029296875
10 = 0.00146484375
11 = 0.000732421875
12 = 0.0003662109375
13 = 0.00018310546875
14 = 9.1552734375e-05
15 = 4.57763671875e-05
16 = 2.288818359375e-05
17 = 1.1444091796875e-05
18 = 5.7220458984375e-06
19 = 2.86102294921875e-06
20 = 1.430511474609375e-06
21 = 7.152557373046875e-07
22 = 3.5762786865234375e-07
23 = 1.7881393432617188e-07
24 = 8.940696716308594e-08
25 = 4.470348358154297e-08
26 = 2.2351741790771484e-08
27 = 1.1175870895385742e-08
28 = 5.587935447692871e-09
29 = 2.7939677238464355e-09
30 = 1.3969838619232178e-09
31 = 6.984919309616089e-10
32 = 3.4924596548080444e-10
33 = 1.7462298274040222e-10
34 = 8.731149137020111e-11
35 = 4.3655745685100555e-11
36 = 2.1827872842550278e-11
37 = 1.0913936421275139e-11
38 = 5.4569682106375694e-12
39 = 2.7284841053187847e-12
40 = 1.3642420526593924e-12
41 = 6.821210263296962e-13
42 = 3.410605131648481e-13
43 = 1.7053025658242404e-13
44 = 8.526512829121202e-14
45 = 4.263256414560601e-14
46 = 2.1316282072803006e-14
47 = 1.0658141036401503e-14
48 = 5.329070518200751e-15
49 = 2.6645352591003757e-15
50 = 1.3322676295501878e-15
51 = 6.661338147750939e-16
52 = 3.3306690738754696e-16
53 = 2.220446049250313e-16
54 = 1.1102230246251565e-16
55 = 0.0
56 = 0.0
57 = 0.0
58 = 0.0
59 = 0.0
60 = 0.0
61 = 0.0
62 = 0.0
63 = 0.0
64 = 0.0
65 = 0.0
66 = 0.0
67 = 0.0
68 = 0.0
69 = 0.0
70 = 0.0
71 = 0.0
72 = 0.0
73 = 0.0
74 = 0.0
75 = 0.0
76 = 0.0
77 = 0.0
78 = 0.0
79 = 0.0
80 = 0.0
81 = 0.0
82 = 0.0
83 = 0.0
84 = 0.0
85 = 0.0
86 = 0.0
87 = 0.0
88 = 0.0
89 = 0.0
90 = 0.0
91 = 0.0
92 = 0.0
93 = 0.0
94 = 0.0
95 = 0.0
96 = 0.0
97 = 0.0
98 = 0.0
99 = 0.0
100 = 0.0
101 = 0.0
The root of -x-cosx using bisection method came out to be: 
-0.7390851332151605
-0.7390851332151605
The functional value of -x-cosx at the calculated roots is:
-3.3306690738754696e-16
-3.3306690738754696e-16
Table 4 showing iteration number against the absolute values for -x-cosx by regula falsi method: 
index = error
1 = -0.06034998749653775
1 = 0.06034998749653775
2 = 0.00792704291316415
3 = 0.0010083759935594072
4 = 0.0001277309545272276
5 = 1.617096372197313e-05
6 = 2.047132794058548e-06
7 = 2.5915069423732007e-07
8 = 3.280637639324624e-08
9 = 4.15302059408873e-09
10 = 5.257386748169779e-10
11 = 6.655420659029687e-11
12 = 8.425260489275388e-12
13 = 1.0664802374549254e-12
14 = 1.3500311979441904e-13
15 = 1.709743457922741e-14
16 = 2.220446049250313e-15
17 = 3.3306690738754696e-16
18 = 0.0
19 = 0.0
20 = 0.0
21 = 0.0
The root of -x-cosx using regula falsi came out to be: 
-0.7390851332151607
The functional value of -x-cosx at the calculated root is: 
0.0





'''
   