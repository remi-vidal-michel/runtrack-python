w = (int(input("taile ? : ")))
h = w
j = 0
print("+", "-"*(w+1), "+")
for i in range(h+1):
    print("|", "#"*(w-j), "#"*j, "|")
    j+=1
print("+", "-"*(w+1), "+")