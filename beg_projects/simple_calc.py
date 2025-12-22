
try:

    a= int(input("Enter 1st number :"))
    b= int(input("Enter 2st number :"))

    # o = input("Enter operation:")

    # print("1.addition\n2.subtraction\n3.multiplication\n4.division")
    while(True):
        o = input("Enter operation:")
        print("1.addition\n2.subtraction\n3.multiplication\n4.division")
        match o:
            case "1":
                print (f"the result is :{a+b}")
            case "2":
                print (f"the result is :{a-b}")
            case"3" :
                print (f"the result is :{a*b}")
            case"4":
                print (f"the result is :{a/b}")
            case default:
                print(f"there was an error")
                break
        cond=input("Enter Y to continue or S to stop: ")
        if(cond=="S"):
            break
        else:
            continue
        
                
except Exception as e:
    print("Enter a valid value of number a and b")