def maxnum(m, n):
    if m > n:
        return m
    else:
        return n

m = int(input("숫자1:"))
n = int(input("숫자2:"))

largest_number = maxnum(m, n)
print("큰 수= ", largest_number)
          
