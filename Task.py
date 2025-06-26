Item1_price: int = 50
Item2_price: int = 100
Item3_price: int = 150
Total_Cost: int = 300
Total_Budget: int = 1000
print (Item1_price + Item2_price + Item3_price)
if Total_Budget > Total_Cost:
    print ('You have bought these items')
else:
    print('Sorry You dont have enough money to buy these items, PLEASE GET OUT')
print (Total_Budget - Total_Cost)