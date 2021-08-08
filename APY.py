import tkinter as tk
import lib



def conf_wallet(previous):
    previous.destroy()
    global conf
    conf = tk.Frame(Portfel)

    label_create = tk.Label(conf, text="Do you want to add stock?", width='100', font=('Arial', 20))
    label_create.pack()
    yes_button = tk.Button(conf, text="Yes", command=lambda: New_Stock())
    yes_button.pack()
    show_wallet = tk.Button(conf, text="Show wallet", command=lambda: Show_wallet())
    show_wallet.pack()
    no_button = tk.Button(conf, text="Exit", command=exit)
    no_button.pack()
    conf.pack()
def Menu(previous=None):
    global Menu
    global Portfel
    if previous!=None:
        previous.destroy()
    Portfel=tk.Tk()
    Portfel.title("Portfel")
    Portfel.geometry("1000x800")
    Menu=tk.LabelFrame(Portfel)
    label_menu = tk.Label(Menu, text="Menu", width='100',font=('Arial',20))
    label_menu.pack()
    create_button = tk.Button(Menu, text="Create new wallet", command=lambda: conf_wallet(Menu))
    create_button.pack()
    close_button = tk.Button(Menu, text="Close", command=quit)
    close_button.pack()
    Menu.pack()
    Portfel.mainloop()

def New_Stock():
    global wallet
    wallet=lib.Wallet()
    conf.destroy()

    frame_new=tk.Frame()
    label_type = tk.Label(frame_new, text="Type name of stock",width='100',font=('Arial',20))
    label_type.pack()
    entry_type=tk.Entry(frame_new,width='10')
    entry_type.pack()
    label_qua = tk.Label(frame_new, text="Quantity",width='100',font=('Arial',20))
    label_qua.pack()
    entry_qua=tk.Entry(frame_new,width='10')
    entry_qua.pack()
    label_price = tk.Label(frame_new, text="Price",width='100',font=('Arial',20))
    label_price.pack()
    entry_price=tk.Entry(frame_new,width='10')
    entry_price.pack()
    def do():
        name = entry_type.get()
        quantity = entry_qua.get()
        price = entry_price.get()
        stock=lib.Stock(name,quantity,price)
        wallet.add_stock(stock)

    Ok_button = tk.Button(frame_new, text="Ok", command=do())
    Ok_button.pack()
    close_button = tk.Button(frame_new, text="Back", command= lambda: conf_wallet(frame_new))
    close_button.pack()
    frame_new.pack()


def Show_wallet():
    wallet.show_wallet()

Menu()