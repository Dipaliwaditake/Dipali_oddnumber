
# find a min no using lambda fun from takeing input from user

a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))
min=lambda a,b,c:a if a<b and a<c else b if b<c else c
print(min(a,b,c))
