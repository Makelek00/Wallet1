import tkinter as tk
import numpy as np
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import pickle

with open('Wallets/Wallet1', 'rb') as config_file:
    Wallet = pickle.load(config_file)

    # After config_dictionary is read from file
    print(Wallet)
    Wallet.show_wallet()


#plt.savefig('books_read.png')
