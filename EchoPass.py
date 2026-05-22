import tkinter as tk
from tkinter import tkk, filedialog, messagebox
import hashlib

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EchoPass by S-AI")
        self.root.geometry("500x650")

    # tab control
        self.notebook = tkk.Notebook(root)
    # tab 1 - generator
        self.tab1 = tkk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Genarate Password")
    # tab 2 - search
        self.tab2 = tkk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Search/Retrieve Password")

        self.notebook.pack(expand=True, fill="both")
    # ui for tabs
        self.tab1_input = self.build_ui(self.tab1, "Generate Password", self.generate_password)
        self.tab2_input = self.build_ui(self.tab2, "Search/Retrieve Password", self.search_password)
        


    def build_ui(self, parent, button_text, command_func):
    # frame for form
    frame = ttk.Frame(parent, padding="20")
    frame.pack(fill="x")