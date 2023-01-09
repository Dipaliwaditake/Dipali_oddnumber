# a=("red","orange","blue","white")
# print(len(a))

# a=(14,54,76,51)
# print(a)
#
# a=tuple((124,552,5855))
# print(a[2])

x=("red","orange","gray","white")
y=list(x)
y[2]="black"
x=tuple(y)
print(x)