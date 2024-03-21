def m2n_sum(m, n):
    if m > n:
        m, n = n, m
    return sum(range(m, n + 1))

m = int(input("정수1 : "))
n = int(input("정수2 : "))
print(m, n, m2n_sum(m, n))
        
