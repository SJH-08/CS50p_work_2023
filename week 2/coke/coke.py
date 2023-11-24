# Induce infinite loop: ask for user's input until payment is done
coke = 50
while coke > 0:
    print("Amount Due:", coke)
    coin = int(input("Insert Coin:"))
# Accepted coin only
    if coin == 25 or coin == 10 or coin == 5:
        coke -= coin
# Payment is complete and rest money
        print("Change Owed:", abs(coke))
# Coin inserted not accepted
    else:
        print("Amount Due:", coke)
