d = {1:'amazon',2:'flipkart',3:'snapdeal',4:'myntra'}
print(d)
print(d[1])
del d[4]
print(d)
print("list of value pairs ",d.items())
print("list of keys  ",d.keys())
print("list of value  ",d.values())
e = d.copy()
print("shallow copy of the dictonary d",e)
d.clear()
print("trying to print dictonary ",d)
