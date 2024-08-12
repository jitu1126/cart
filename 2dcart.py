cart=[]
c=0
while(1):
    print("1.. add Item")
    print("2.. show All Item")
    print("3.. serching")
    print("4.. delete")
    print("5.. Edit")
    print("6.. break")

    ch=int(input("choice user = "))
    if(ch==1):
        name=input("enter item name = ")
        qnt=int(input("enter quantity = "))
        price=float(input("enter price = "))
        tot=qnt*price
        item=[name,qnt,price,tot]
        c=c+1
        cart.append(item)
    
    if(ch==2):
        gt=0
        print("total item purchase : ",c)
        print("NAME________QUANTITY________PRICE________TOTAL")
        for row in cart:
            print(row[0],"_______",row[1],"__________",row[2],"_______",row[3])
            gt+=row[3]
        print("Grade Total : ","__________________________",gt)
           
    if(ch==3):
        item=input("enter item to search = ")
        for i in range(0,len(cart)):
            if item==cart[i][0]:
                print(item)
                break
            else:
                print('item not found')
                break
    if(ch==4):
        item=input("enter item to remove = ")
        for i in range(0,len(cart)):
            if item==cart[i][0]:
                break
        cart.pop(i)
        c=c-1

    if(ch==5):
        item=input("search item in cart = ")
        for i in range(0,len(cart)):
            if item==cart[i][0]:
                name=input("enter item name = ")
                qnt=int(input("enter quantity = "))
                price=float(input("enter price = "))
                tot=qnt*price
                cart[i][0]=name
                cart[i][1]=qnt
                cart[i][2]=price
                cart[i][3]=tot

    if(ch==6):
        break
            
    
        
                
            
