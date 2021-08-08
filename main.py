import lib
Wallet1 = lib.Create_Wallet(1)
def Menu():
    print("Hi, If you want add Stock click- 1")
    print("If you want to see your wallet click- 2")
    first=input()
    if first=="1":
        lib.New_Stock(Wallet1)
        lib.save_wallet(Wallet1)

        Menu()
    if first=="2":
        Wallet1.show_wallet()
        Wallet1.show_chart()
        Menu()
Menu()






