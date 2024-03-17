def minnum(m, n):
    if m < n:
        return m
    else:
        return n

m = int(input("숫자 1: "))
n = int(input("숫자 2: "))
smaller_number = minnum(m, n)
print("작은 수 = ", smaller_number)
