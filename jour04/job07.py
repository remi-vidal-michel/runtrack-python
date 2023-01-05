L = [8, 24, 48, 2, 16]
multi = 0
for i in L:
    if i % 3 == 0:
        multi += 1
        print(i)
print("Il y a "+str(multi)+" multiples de 3 dans la liste")