def printnumber(n):
    i = 2
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                break
            j+=1
        else:
            print(i)
        i+=1
printnumber(1000)