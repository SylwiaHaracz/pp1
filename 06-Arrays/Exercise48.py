def create_2d_arr(x,y):
    return[[0 for i in range(y)] for i in range(x)]

my_2d_arr=create_2d_arr(3,5)

for row in my_2d_arr:
    print(row)