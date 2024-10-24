price=50
accepted_coin=[25,10,5]# accepted coin to machine
total_inserted=0
while total_inserted<price:# amount inserted is lower than price of cocacola
    amount_due=price-total_inserted # amoujnt remain to buy cocacola 
    print(f"your amount due is:",amount_due)
    coin=int (input("insert coin in (25,10,5): ")) # prompt the insert of coin 
    if coin in accepted_coin:
        total_inserted+=coin # total inserterd is equal to sum of coin entered
        print (f"your total amount is : ",total_inserted )
        if total_inserted==50:
            print("take 1 bottle of cocacola ")
    else:
        print("please insert valid coin ")  
change=total_inserted-price 
if change>0: # 

    print(f"your change is:",change)
else:
    print("no change owed")
                    
        