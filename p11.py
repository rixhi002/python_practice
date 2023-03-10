print("Enter cost price: ")
cp=int(input())
print("Enter selling price: ")
sp=int(input())
if cp>sp:
    loss=cp-sp
    loss_per= (loss/cp) * 100
    print("loss :",loss)
    print("loss percentage :",loss_per)
elif sp>cp:
    profit=sp-cp
    profit_per= (profit/sp) * 100
    print("profit :",profit)
    print("profit percentage :",profit_per)
elif sp==cp:
    print("Neither profit nor loss")
else:
    print('Invalid')
    
