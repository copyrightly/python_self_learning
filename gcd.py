a = int(input("enter the 1st integer:"))
b = int(input("enter the 2nd integer:"))

x_array = [1,0]
y_array = [0,1]

m = a
n = b
if m < n:
    u = m
    m = n
    n = u
    
i = 0
while m % n > 0:
    q = m//n
    r = m % n
    x_array.append(x_array[i] - x_array[i + 1] * q)
    y_array.append(y_array[i] - y_array[i + 1] * q)
    m = n
    n = r
    i = i + 1

x = x_array[len(x_array) - 1]
y = y_array[len(y_array) - 1]

if a < b:
    h = x
    x = y
    y = h
    
print("x=",x, "y=",y, "gcd=", a * x + b * y)
