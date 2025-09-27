def computepay(h, r):
    
    if hr > 40: 
        overtime = (h - 40)*(r*0.5)
        regular = h*r 
        total = regular + overtime
    else:
        total = h * r
    print("Return", total)
    return total

h = input("Enter Hours:")
r = input("Enter Rate:")
hr = float (h)
rt = float (r)
p = computepay(hr, rt)
print("Pay", p)
    
