
def smart(func):
    def inner(a,b):
        if a < b :
            a,b = b, a 
        return func(a, b)

    return inner

@smart
def  div(a, b):
    print(a/b)


div(2, 4)