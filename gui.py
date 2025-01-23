# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from block import Block

def create_gui(root, blocks):
    """GUI-dı quralap, bloktardı tізip, qate habarların körsetedi."""
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Bloktardı tізip körsetw
    listbox = tk.Listbox(frame, width=80, height=20)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Scrollbar qosw
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Bloktardı tізimge qosw
    for block in blocks:
        if block.is_valid():
            listbox.insert(tk.END, f"Address: {block.address}, Timestamp: {block.timestamp}, Data: {block.data}")
        else:
            listbox.insert(tk.END, f"Invalid Block: {block.address}")

    # Qate habarın ko'rsatw
    def show_invalid_block_error():
        invalid_blocks = [block for block in blocks if not block.is_valid()]
        if invalid_blocks:
            messagebox.showwarning("Invalid Blocks", f"Jaramsyz bloktar bar: {len(invalid_blocks)}")

    # Qate habarına basqan vaqtımen
    button = tk.Button(root, text="Show Invalid Blocks", command=show_invalid_block_error)
    button.pack(pady=10)


