a = int(input("시작 값 = "))
b = int(input("종료 값 = "))

c = 0
for i in range(a, b+1) :
    if i % 6 == 0 :
        c = c+1
print("6의 배수 개수 =", c)