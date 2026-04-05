while True:
    print("===calculator===")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. power")
    print("6.  exit")
    a=int(input("enter first no."))
    b=int(input("enter second no."))
    choice=int(input("enter your choice"))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        if b>0:
            print(a/b)
    elif choice==5:
        print(a**b)
    elif choice==6:
        break
    else:
        print("invalid choice")
        break