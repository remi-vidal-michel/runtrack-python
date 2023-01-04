def printnumber(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i+=1
printnumber(100)