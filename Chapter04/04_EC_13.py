opnd1 = int(input("피연산자1 : "))
opnd2 = int(input("피연산자2 : "))
v3 = opnd1 // 100
v2 = opnd1 // 10 % 10
v1 = opnd1 % 10
print(opnd1, "*", opnd2)
print("=", "(", v3, "+", v2, "+", v1, ")", "*", opnd2)
print("=", v3, "*", opnd2, "+", v2, "*", opnd2, "+", v1, "*", opnd2)
print("=", v3*opnd2, "+", v2*opnd2, "+", v1*opnd2)
print("=", opnd1*opnd2)
