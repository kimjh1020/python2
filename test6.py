def read_num(num):
    if num ==0 : return 'zero'
    elif num == 1 :return 'one'
    elif num == 2: return 'two'
    elif num == 3: return 'three'
    elif num == 4: return 'four'
    elif num == 5: return 'five'
    elif num == 6: return 'six'
    elif num == 7: return 'seven'
    elif num == 8: return 'eight'
    elif num == 9: return 'nine'
    elif num == 10: return 'ten'

read_num(1)

print(read_num(5))

def tri(a):
    return a*3
print(tri(2))
print(tri('x'))