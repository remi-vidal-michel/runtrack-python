w = (int(input("largeur ? : ")))
h = (int(input("hauteur ? : ")))
print("|", "-"*(w-2), "|")
for i in range(h-2):
    print("|", " "*(w-2), "|")
print("|", "-"*(w-2), "|")