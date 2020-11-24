import random
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import ImageTk, Image
from recursive import *
from StringGenerator import *

root = Tk()
root.title("Advanced Algorithm")
# set root background
root.configure(background="white")
root.wm_iconbitmap('./img/Search.ico')
# style = classic
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel', background="white")
style.configure('TButton', background="white")
style.configure('TRadioButton', background="#ffffff")

# width x height + x_offset + y_offset:
root.geometry("1280x600+100+50")


def hello():
    print(hello)


def popup_exit():
    response = messagebox.askyesno("EXIT ??", "Are You sure you want to exit")
    if response == 1:
        root.quit()


# method for button about us in menubar
def about_us():
    top = Toplevel()
    top.wm_iconbitmap('./img/info.ico')
    top.title("About Us")
    top.geometry("300x250+170+150")
    label_frame = LabelFrame(top, text="About Us :", padx=2, pady=2)
    label_frame.pack(padx=2, pady=2)
    label1 = Label(label_frame, text="This is the first version of calculation Algorithm", padx=1, pady=1)
    label1.pack()
    label2 = Label(label_frame, text="TEAM WORK :", padx=2, pady=2)
    label2.pack()
    label3 = Label(label_frame, text="* Ahmad AYADA : M1 DSC\n\n"
                                     + "* Ramez ALSIBAI : M1 DSC\n\n"
                                     + "* Milad Zahediyami : M1 CPS2\n\n"
                                     + "* Parsa Rajabzadeh : M1 CPS2\n")
    label3.pack(padx=2, pady=2)
    button = Button(label_frame, text="Dismiss", command=top.destroy, padx=1, pady=1)
    button.pack(padx=2, pady=2)


# Create Menu Bar
menubar = Menu(root)
# create a pull down menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: about_us())
menubar.add_cascade(label="Help", menu=helpmenu)
# display the menu
root.config(menu=menubar)
# noinspection PyBroadException
my_scrollbar = Scrollbar(root, orient=VERTICAL)
parent = Frame(root, bg='white', )

# noinspection PyBroadException
try:
    C = Canvas(parent, bg="white", height=250, width=300)
    background_image = ImageTk.PhotoImage(Image.open("./img/background.png"))
    background_image_label = Label(parent, image=background_image)
    background_image_label.place(x=0, y=0, relwidth=1, relheight=1)
    # background_image_label.pack(fill=BOTH, expand=YES)
    C.pack()
except Exception:
    print("Error open image")

# Add Logo to Project
# noinspection PyBroadException
try:
    logo_image = ImageTk.PhotoImage(Image.open("./img/ujm_logo.png"))
    logo_image_label = Label(parent, image=logo_image)
    logo_image_label.place(x=0, y=0, width=200, height=77)
except Exception:
    print("Error open image")

# add Title Label Left
title_label = Label(parent, text="Advanced algorithms", bg='white')
my_font = tkFont.Font(family="Times New Roman", size=16, weight="bold")
title_label.configure(font=my_font)
title_label.place(x=2, y=76)

# add Title Label Center
title_label = Label(parent, text="LCS ALGORITHMS\nLongest Common Subsequence\nProject 2020", bg='white')
my_font = tkFont.Font(family="Times New Roman", size=24, weight="bold")
title_label.configure(font=my_font)
title_label.place(x=500, y=0)
# add Title Label Center
title_label = Label(parent, text="MASTER 1°\nComputer Science\nCPS2/DSC/MLDM", bg='white')
my_font = tkFont.Font(family="Times New Roman", size=20, weight="bold")
title_label.configure(font=my_font)
title_label.place(x=1200, y=0)

title_label = Label(parent, text="  Please Select Your Algorithm : ", bg='white', fg='red')
my_font = tkFont.Font(family="Times New Roman", size=18, weight="bold", underline="True")
title_label.configure(font=my_font)
title_label.place(x=50, y=150)
'''_________________________________________________________________________________________________________________'''

pure_recursive = IntVar()
my_font = tkFont.Font(family="Times New Roman", size=16, weight="bold", underline="False")
c_box1 = Checkbutton(parent, text='Recursive Algorithm', variabl=pure_recursive, bg='white', font=my_font)
c_box1.place(x=50, y=200)
'''_________________________________________________________________________________________________________________'''
# add input

recursive_controll=0

def test_entery_int(entery):
    try:
        int(entery.get())
        my_number = int(entery.get())
        if 4 <= my_number <= 10:
            return 1
        else:
            messagebox.showerror(title="String Size Input", message="Error : Please input : " +
                                                                    "4<= Number <=10\r\nOR KEEP IT EMPTY !!" +
                                                                    "String Size by Default = 10")
            return 0
    except ValueError:
        messagebox.showerror(title="String Size Input", message="Error :" +
                                                                "Please input a <NUMBER> Value\r\n" +
                                                                "Or KEEP IT EMPTY\r\n" +
                                                                "String Size by Default = 10")
        return 0


def set_text_entrey(entrery1, entrery2, button):
    global recursive_controll
    if len(entrery2.get()) == 0:
        recursive_controll += 1
        text = random_string()
        entrery1.delete(0, END)
        entrery2.delete(0, END)
        entrery1.insert(0, text)
        entrery1.config(state=DISABLED)
        entrery2.config(state=DISABLED)
        button.config(state=DISABLED)
        return
    else:
        if test_entery_int(entrery2) == 1:
            number = int(entrery2.get())
            text = random_string(longer=number)
            recursive_controll += 1
            entrery1.delete(0, END)
            entrery1.insert(0, text)
            entrery1.config(state=DISABLED)
            entrery2.config(state=DISABLED)
            button.config(state=DISABLED)

    return


def reset_all(e1, e2, e3, e4, b1, b2):
    global recursive_controll
    print("globale before delete = {}".format(recursive_controll))
    print("globale before delete = {}".format(recursive_controll))
    recursive_controll -= 1
    b1.config(state=ACTIVE)
    b2.config(state=ACTIVE)
    e1.delete(0, END)
    e1.config(state=NORMAL)
    e2.delete(0, END)
    e2.config(state=NORMAL)
    e3.delete(0, END)
    e3.config(state=NORMAL)
    e4.delete(0, END)
    e4.config(state=NORMAL)
    return


def run_pure_recursive(string1, string2, str_len1, str_len2):
    top2 = Toplevel()
    top2.wm_iconbitmap('./img/Halloween.ico')
    top2.title("Results")
    top2.geometry("500x350+170+150")
    label_frame2 = LabelFrame(top2, text="Pure Algoruthme Results:", padx=2, pady=2)
    label_frame2.pack(padx=2, pady=2)
    label1 = Label(label_frame2, text="This is the first version of calculation Algorithm", padx=1, pady=1)
    label1.pack()
    label2 = Label(label_frame2, text="TEAM WORK :", padx=2, pady=2)
    label2.pack()
    label3 = Label(label_frame2, text="* Ahmad AYADA : M1 DSC\n\n"
                                     + "* Ramez ALSIBAI : M1 DSC\n\n"
                                     + "* Milad Zahediyami : M1 CPS2\n\n"
                                     + "* Parsa Rajabzadeh : M1 CPS2\n")
    label3.pack(padx=2, pady=2)
    button = Button(label_frame2, text="Dismiss", command=top2.destroy, padx=1, pady=1)
    button.pack(padx=2, pady=2)


label_string_recursive = Label(parent, text="Enter your 1st String ", bg='white')
label_string_recursive.configure(font=my_font)
label_string_recursive.place(x=300, y=201)

entery_rec1 = ttk.Entry(parent)
entery_rec1.place(x=500, y=201, width=140, height=25)
label_string_recursive2 = Label(parent, text="String Size ( <=10 ) : ", bg='white')
label_string_recursive2.place(x=645, y=201)
entery_rec2 = ttk.Entry(parent)
entery_rec2.place(x=760, y=201, width=35, height=25)

button1_rec_gen = Button(parent, text='Generate String', command=lambda: set_text_entrey(entery_rec1, entery_rec2,
                                                                                         button1_rec_gen))
button1_rec_gen.place(x=800, y=201, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_recursive2 = Label(parent, text="Enter your 2nd String ", bg='white')
label_string_recursive2.configure(font=my_font)
label_string_recursive2.place(x=300, y=251)
entery_rec3 = ttk.Entry(parent)
entery_rec3.place(x=500, y=251, width=140, height=25)
label_string_recursive2 = Label(parent, text="String Size ( <=10 ) : ", bg='white')
label_string_recursive2.place(x=645, y=251)
entery_rec4 = ttk.Entry(parent)
entery_rec4.place(x=760, y=251, width=35, height=25)

button2_rec_gen = Button(parent, text='Generate String', command=lambda: set_text_entrey(entery_rec3, entery_rec4, button2_rec_gen))
button2_rec_gen.place(x=800, y=251, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_recursive3 = Label(parent, text="Click to Get a results Test :", bg='white')
label_string_recursive3.configure(font=my_font)
label_string_recursive3.place(x=300, y=301)
#button3_rec_gen = Button(parent, text='Start Test..', command=lambda: run_pure_recursive())
#button3_rec_gen.place(x=550, y=301)
button4_rec_gen = Button(parent, text='Reset All..', command=lambda: reset_all(entery_rec1, entery_rec2,
                                                                                          entery_rec3, entery_rec4,
                                                                                          button1_rec_gen,
                                                                                          button2_rec_gen))
button4_rec_gen.place(x=650, y=301)
'''_________________________________________________________________________________________________________________'''
dynamic_programming = IntVar()
c_box2 = Checkbutton(parent, text='Dynamic Programming', variabl=dynamic_programming, bg='white', font=my_font)
c_box2.place(x=50, y=350)

'''
languages = ['Python', 'Perl', 'C++', 'Java', 'Tcl/Tk']
labels = range(5)

for i in range(5):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    ll = Label(parent, text=languages[i], fg='White' if brightness < 120 else 'Black', bg=bg_colour)
    ll.place(x=20, y=30 + i * 30, width=120, height=25)
# add input
entery1 = ttk.Entry(parent)
entery1.place(x=200, y=30, width=140, height=25)
button1 = ttk.Button(parent, text="Click here")
button1.pack()
button_quit = ttk.Button(parent, text="quit Program", command=root.quit)
button_quit.place(x=200, y=60)
button_quit2 = ttk.Button(parent, text="quit Program??", command=lambda: popup_exit())
button_quit2.place(x=270, y=60)


def bu_entery():
    print(entery1.get())
    entery1.delete(0, END)


button1.config(command=lambda: bu_entery())
'''
parent.pack(fill=BOTH, expand=YES)
separator = Frame(height=3, bd=0, relief=SUNKEN)
separator.pack(fill=X, padx=1, pady=1)
Label(separator, text="Status Bar").pack()
root.mainloop()
