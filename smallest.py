smallest =  None
intervar = [78,89,65,33,11,7,5,4,3,2,1]
for i in intervar:
    if smallest is None or i < smallest:
        smallest = i
        print('Smallest: ', smallest)
print('Smallest Value is: ', smallest)
print(min(intervar), max(intervar))
