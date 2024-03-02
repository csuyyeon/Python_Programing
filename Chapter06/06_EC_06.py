s = 0
z = 0
for i in range(1,101):
    if i % 2 == 0:
        s = s + i
    else:
        z = z + i
    print("짝수 합:",s)
    print("홀수 합:",z)
