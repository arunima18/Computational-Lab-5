# First Derivative of a Function
def d1(f, x):
    h = 10 ** (-5)
    return (f(x + h) - f(x - h)) / (2 * h)

# Second Derivative of a Function
def d2(f, x):
    h = 10 ** (-5)
    return (f(x + h) + f(x - h) - 2 * f(x)) / (h ** 2)


# Create a ploynomial from an array
def poly(pol_coeffs):
    n = len(pol_coeffs) - 1

    def pol(x):
        p = 0
        for i in range(n+1):
            p += pol_coeffs[i] * (x ** (n - i))
        return p

    return pol


# Laguerre's Method for finding roots of a polynomial
def laguerre(pol_coeffs, x):
    roots = []
    p = poly(pol_coeffs)
    n = len(pol_coeffs) - 1
    while n > 0:
        # if guess is the root
        if p(x) == 0:
            roots.append(x)
            pol_coeffs = synth_div(pol_coeffs, x, n)  
            p = poly(pol_coeffs)              
            n -= 1                                    
        else:
            a = 1
            while a > 10 ** (-5):
                G = d1(p, x) / p(x)
                H = (G * G) - (d2(p, x) / p(x))
                deno_plus = G + ((n - 1) * (n * H - G * G)) ** 0.5
                deno_mnus = G - ((n - 1) * (n * H - G * G)) ** 0.5
                if abs(deno_plus) > abs(deno_mnus):
                    a = n / deno_plus
                else:
                    a = n / deno_mnus
                x -= a

            roots.append(x)
            pol_coeffs = synth_div(pol_coeffs, x, n)    
            p = poly(pol_coeffs)                    
            n -= 1                                          
    return roots


# Synthetic Division method
def synth_div(p, a, n):
    q = [p[0]]
    for i in range(1, n):
        b = p[i] + a * q[-1]
        q.append(b)

    return q



# Main function
pol_coeffs = [1, -3, -7, 27, -18]

print("Roots of the given polynomial are: ")
roots = laguerre(pol_coeffs, 3)
for i in range(len(roots)):
    print(roots[i])
   
   
   
'''Roots of the given polynomial are:
3
2.0
1.0
-3.0'''



