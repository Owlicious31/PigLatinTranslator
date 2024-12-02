from customtkinter import *
from tkinter import Canvas,PhotoImage,messagebox
from translator import *
import pyperclip

FONT:str = "Courier"
SYSTEM_BG_COLOR:str = "#242424"
WINDOW_HEIGHT:int = 500
WINDOW_WIDTH:int = 900


class App(CTk):

    def __init__(self):
        super().__init__()

        self.title("Pig Latin Translator")
        self.config(pady=50, padx=50)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.grid_columnconfigure(0, weight=2)  # First column
        self.grid_columnconfigure(1, weight=1)  # Second column
        self.grid_columnconfigure(2, weight=2)  # Third column

        self.grid_rowconfigure(0, weight=1)  # First row (title)
        self.grid_rowconfigure(1, weight=1)  # Second row (labels)
        self.grid_rowconfigure(2, weight=2)  # Third row (text boxes)
        self.grid_rowconfigure(3, weight=1)  # Fourth row (buttons)


        #Title
        self.title_label = CTkLabel(master=self,text="Pig Latin Translator",font=(FONT,24,"bold"))
        self.title_label.grid(column=1,row=0)

        #Original and translated text boxes and labels
        self.original_text_label = CTkLabel(master=self,text="Original Text",font=(FONT,24,"bold"))
        self.original_text_label.grid(column=0,row=1)

        self.original_text_textbox = CTkTextbox(master=self, height=250, width=250)
        self.original_text_textbox.grid(column=0, row=2)

        self.translated_text_label = CTkLabel(master=self, text="Translated Text", font=(FONT, 24, "bold"))
        self.translated_text_label.grid(column=2,row=1)

        self.translated_text_textbox = CTkTextbox(master=self, height=250, width=250)
        self.translated_text_textbox.grid(column=2,row=2)

        #Translate Button
        self.translate_button = CTkButton(master=self,text="Translate",command=self.translate_user_input)
        self.translate_button.grid(column=1,row=3)

        #Copy button
        self.copy_button = CTkButton(master=self,text="Copy",command=self.copy_text,height=10,fg_color="grey")

        self.copy_button.grid(column=1,row=4)
        #Background image
        self.canvas = Canvas(bg=SYSTEM_BG_COLOR,width=200,height=200,highlightthickness=0)
        self.image = PhotoImage(file="assets/translate-logo.png")
        self.canvas.create_image(100,100,image=self.image)
        self.canvas.grid(column=1,row=2)


    def translate_user_input(self):
        original_text = self.original_text_textbox.get("0.0","end").strip()
        if original_text == "":
            messagebox.showinfo(title="Pig Latin Translator",message="You did not enter any text")
        else:
            self.translated_text_textbox.delete("0.0", "end")
            self.translated_text_textbox.insert("0.0", translate(original_text))

    def copy_text(self):
        pyperclip.copy(text=self.translated_text_textbox.get("0.0","end").strip())