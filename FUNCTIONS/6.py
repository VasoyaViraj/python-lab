def create_list(x):
    return [(i, i*i, i*i*i) for i in range(1,x+1) ]

print(create_list(5))
