def myfunction(num):
    if num <=1:
        print(False)
    else:
        for i in range(2,num):
            if (num%i) == 0:
                print(False)
                break
            else:
                print(True)
                break