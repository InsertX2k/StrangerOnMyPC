# imports.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class WelcomeWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello and Welcome Guest!")
        self.geometry('900x450')
        self.resizable(False, False)
        self.minsize(900, 450)
        self.maxsize(900, 450)
        self.image_src = Image.open("img4k.png")
        try:
            self.iconbitmap("icon0.ico")
        except Exception as exception_for_not_loading_iconbitmap:
            print(f"{exception_for_not_loading_iconbitmap}")
            messagebox.showerror("Unable to load the icon for the window", f"{exception_for_not_loading_iconbitmap}")
        
        def continue_button_function():
            """
            A function used to close this window.
            """
            raise SystemExit(0)
        
        def disable_event():
            messagebox.showwarning("Info", "You can't close this window unless you agree the terms shown in this window.")
            return None

        self.image_resized = self.image_src.resize((100, 100), Image.ANTIALIAS)
        self.image_fortk_widgets = ImageTk.PhotoImage(self.image_resized)
        self.mrx_logo_img = Label(self, image=self.image_fortk_widgets)
        self.mrx_logo_img.image = self.image_fortk_widgets
        self.mrx_logo_img.place(x=30, y=25)
        self.info0_lbl = Label(self, text="This PC is not yours", font=("Arial Bold", 25), foreground='black')
        self.info0_lbl.place(x=170, y=25)
        self.info1_lbl = Label(self, text="This means that this PC's owner has put some restrictions to your session and your session is temporary.", font=("Arial", 11), foreground='black')
        self.info1_lbl.place(x=170, y=70)
        self.info2_lbl = Label(self, text="For Example, this PC's owner might have put some or all of these restrictions:", font=("Arial", 11), foreground='black')
        self.info2_lbl.place(x=170, y=90)
        self.info3_lbl = Label(self, text="• You can't install or modify or uninstall programs", font=("Arial", 11), foreground='black')
        self.info3_lbl.place(x=170, y=110)
        self.info4_lbl = Label(self, text="• You can't assign a password to your profile", font=("Arial", 11), foreground='black')
        self.info4_lbl.place(x=170, y=130)
        self.info5_lbl = Label(self, text="• You can't access some (or all) of this PC's disks", font=("Arial", 11), foreground='black')
        self.info5_lbl.place(x=170, y=150)
        self.info6_lbl = Label(self, text="• You can't access other user's files", font=("Arial", 11), foreground='black')
        self.info6_lbl.place(x=170, y=170)
        self.info7_lbl = Label(self, text="• You can't run programs that require Administrative privileges", font=("Arial", 11), foreground='black')
        self.info7_lbl.place(x=170, y=190)
        self.info8_lbl = Label(self, text="• You can't make any changes to this PC's settings", font=("Arial", 11), foreground='black')
        self.info8_lbl.place(x=170, y=210)
        self.info9_lbl = Label(self, text="• You can't create users nor manage them.", font=("Arial", 11), foreground='black')
        self.info9_lbl.place(x=170, y=230)
        self.info10_lbl = Label(self, text="By clicking Continue, you agree to the following terms and you also agree with your restricted computing session.", font=("Arial", 10), foreground='black')
        self.info10_lbl.place(x=170, y=320)
        self.info11_lbl = Label(self, text="If you don't want to continue using a restricted computing session, Please contact This PC's owner as\n soon as possible.", font=("Arial", 11), foreground='black', justify='left')
        self.info11_lbl.place(x=170, y=250)
        self.continue_btn = ttk.Button(self, text="Continue", command=continue_button_function)
        self.continue_btn.place(x=280, y=350, relwidth=0.50, relheight=0.20)

        # declaring a wm_protocol for disabling the close button.
        self.protocol("WM_DELETE_WINDOW", disable_event)



if __name__ == '__main__':
    process = WelcomeWindow()
    process.mainloop()