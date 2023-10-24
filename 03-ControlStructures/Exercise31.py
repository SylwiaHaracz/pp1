x = int(input('Enter X: '))
y = int(input('Enteer Y: '))
if x>0 and y>0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x<0 and y>0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x<0 and y<0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
elif x>0 and y<0:
    print(f'Point P({x},{y}) is in the forth quadrant of the coordinate system')
elif x==0 and y==0:
    print(f"That's the point P({x},{y})!")