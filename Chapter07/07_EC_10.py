def one2n_sum1(n):
    if n < 1:
        return "입력된 수가 1보다 작습니다."
    s = 0
    for i in range(1, n+1):
        s += i
    return s

n = int(input("자연수: "))
result = one2n_sum1(n)
print(n, result)

    
