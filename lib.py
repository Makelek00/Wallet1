import numpy as np
import matplotlib.pyplot as plt
import pickle

class Stock:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price
    def value(self):
        return self.quantity*self.price
    def show_value(self):
        print(self.value())

    def show_details(self):
        print("Name: ",self.name,"\n", "Quantity: ",self.quantity,"\n","Price: ",self.price,"\n","Sum: ", self.value(),"\n")


class Wallet:
    stocks=[]
    size=len(stocks)
    def __init__(self,name):
        self.name=name
    def add_stock(self,stock):
        self.stocks.append(stock)
    def
    def value(self):
        sum=0
        for stock in self.stocks:
            sum+=stock.value()
        return sum

    def part(self):
        part=[]
        for stock in self.stocks:
            part.append(stock.value()/self.value())
            print(self.size)
        return part

    def show_wallet(self):
        for Stock in self.stocks:
            Stock.show_value()
            Stock.show_details()
    def show_chart(self):
        sizes=self.part()
        labels=[]
        for Stock in self.stocks:
            labels.append(Stock.name)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        print("labels:",labels,"sizes:",sizes)
        plt.show()

def Create_Wallet(x):
    wallet=Wallet(1)
    name="Wallets/Wallet"+str(x)+".txt"
    return wallet



def New_Stock(wallet):
    print("Type name of stock:\n")
    name=input()
    print("Quantity:\n")
    quantity=int(input())
    print("Price:\n")
    price=int(input())
    print(name,quantity,price)
    stock=Stock(name,quantity,price)
    wallet.add_stock(stock)
    print("If you want to add next stock? Yes-1 No-2")
    decision=input()
    if decision== "1":
        New_Stock(wallet)
    else:
        pass
def save_wallet(wallet):
    path="Wallets/Wallet"+str(wallet.name)
    with open(path, 'wb') as config_wallet_file:
        pickle.dump(wallet, config_wallet_file)






