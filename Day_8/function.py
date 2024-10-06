a = 5
b = 9

def calc(a, b):
    c = a + b
    print("inside function")
    return c

################

val = calc(5,6)
print(val)

val = calc(50,6)
print(val)

val = calc(a,b)
print(val)