A = input()
A = int(A)
if (A%4==0 and A%400==0) or (A%4==0 and A%100!=0):
    print(1)
else:
    print(0)
