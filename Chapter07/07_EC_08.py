def rectangle_area(col, row):
    return col * row
col = int(input("가로 : "))
row = int(input("세로 : "))

area = rectangle_area(col, row)
print("사각형의 넓이: ", area)
