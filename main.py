# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import json
from block import Block
from gui import create_gui

def load_blocks_from_file():
    try:
        with open('blockchain_data.json', 'r') as file:
            blocks_data = json.load(file)
            blocks = [Block(block['address'], block['timestamp'], block['data']) for block in blocks_data]
            return blocks
    except Exception as e:
        show_error_message(f"Error loading blocks from file: {str(e)}")
        return []

def show_error_message(message):
    messagebox.showerror("Error", message)

def main():
    # GUI ornatu
    root = tk.Tk()
    root.title("Block Explorer")

    # GUI ekran?n qural?q
    blocks = load_blocks_from_file()
    create_gui(root, blocks)

    root.mainloop()

if __name__ == "__main__":
    main()
