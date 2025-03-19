def create_array(a,b,c,n):
    return [ n for _ in range(a) for _ in range(b) for _ in range(c) ]

arr = create_array(4,5,6,17)
print(arr)