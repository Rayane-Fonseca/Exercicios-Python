def maior (a, b, c):

    if a >= b and a >= c:
        print (a)
    elif b >= a and b >= c:
        print (b)
    else:
        print (c)

maior (8, 5, 2)

#####################################

def maior(a, b, c):

    if a > b and a > b:
        return f"O maior número é {a}"
    elif b > a and b > c:
        return f"O maior número é {b}"
    else:
        return f"o maior número é {c}"
    
print(maior(10, 20, 30))

#####################################

def maior(primeiro, *restantes):
    return max(primeiro, *restantes)

print(maior(10, 20, 30, 40, 50, 60))
print(maior(10, 20, 30))