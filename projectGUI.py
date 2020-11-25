from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
from recursive import *
from StringGenerator import *

root = Tk()
sizex = 1200
sizey = 600
posx = 200
posy = 200
root.title("Advanced Algorithm")

# set root background
root.configure(background="white")
root.wm_iconbitmap('./img/Search.ico')
# style = classic
# style = ttk.Style()
# style.theme_use('classic')
# style.configure('TLabel', background="white")
# style.configure('TButton', background="white")
# style.configure('TRadioButton', background="#ffffff")

# width x height + x_offset + y_offset:
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

'''_________________________________________________________________________________________________________________'''





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


'''_________________________________________________________________________________________________________________'''

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
'''_________________________________________________________________________________________________________________'''
# Create Main Frame

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)  # expand=YES
# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scroll bar
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configyre the Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create Another Frame inde the Canvas
parent = Frame(my_canvas, bg='white')

# Add the New Freame to a Window in Canvas
my_canvas.create_window((0, 0), window=parent, anchor="nw")

# parent.pack(fill=BOTH, expand=YES)

'''_________________________________________________________________________________________________________________'''

# noinspection PyBroadException
try:

    background_image = ImageTk.PhotoImage(Image.open("./img/background.png"))
    background_image_label = Label(parent, image=background_image)
    # background_image_label.(frame.scrollable_frame)(x=0, y=0, relwidth=1, relheight=1)
    background_image_label.pack(fill=BOTH, expand=YES)

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
'''_________________________________________________________________________________________________________________'''

# add Title Label Left
title_label = Label(parent, text="Advanced algorithms", bg='white')
my_font = tkfont.Font(family="Times New Roman", size=16, weight="bold")
title_label.configure(font=my_font)
title_label.place(x=2, y=76)

# add Title Label Center
title_label = Label(parent, text="LCS ALGORITHMS\nLongest Common Subsequence\nProject 2020", bg='white')
my_font = tkfont.Font(family="Times New Roman", size=24, weight="bold")
title_label.configure(font=my_font)
title_label.place(x=500, y=0)
# add Title Label Center
title_label = Label(parent, text="MASTER 1°\nComputer Science\nCPS2/DSC/MLDM", bg='white')
my_font = tkfont.Font(family="Times New Roman", size=20, weight="bold")
title_label.configure(font=my_font)
title_label.place(x=1200, y=0)

title_label = Label(parent, text="  Please Select Your Algorithm : ", bg='white', fg='red')
my_font = tkfont.Font(family="Times New Roman", size=18, weight="bold", underline="True")
title_label.configure(font=my_font)
title_label.place(x=50, y=150)
'''_________________________________________________________________________________________________________________'''

recursive_controll = 0


def test_entery_int(entery1):
    try:
        int(entery1.get())
        my_number = int(entery1.get())
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


def on_return1(event):
    global entery_rec1
    global entery_rec2
    global button1_rec_gen
    set_text_entrey(entery_rec1, entery_rec2, button1_rec_gen)


def on_return2(event):
    global entery_rec3
    global entery_rec4
    global button2_rec_gen
    set_text_entrey(entery_rec3, entery_rec4, button2_rec_gen)


def set_text_entrey(entrery1, entrery2, button):
    global recursive_controll
    global string_rec1
    global string_rec2
    global string_rec_len1
    global string_rec_len2
    global button3_rec_gen
    global button4_rec_gen

    if len(str(entrery1.get())) == 0:
        if len(entrery2.get()) == 0:
            if recursive_controll < 2:
                recursive_controll += 1
                button4_rec_gen.config(state=ACTIVE)

            text = random_string()
            entrery1.delete(0, END)
            entrery2.delete(0, END)
            entrery1.insert(0, text)
            if len(string_rec1) == 0:
                string_rec1 = text
                string_rec_len1 = 10
            else:
                string_rec2 = text
                string_rec_len2 = 10
            entrery1.config(state=DISABLED)
            entrery2.config(state=DISABLED)
            button.config(state=DISABLED)
            if recursive_controll == 2:
                button3_rec_gen.config(state=ACTIVE)
                button4_rec_gen.config(state=ACTIVE)
            return
        else:
            if test_entery_int(entrery2) == 1:
                number = int(entrery2.get())
                text = random_string(longer=number)
                if recursive_controll < 2:
                    recursive_controll += 1
                    button4_rec_gen.config(state=ACTIVE)

                entrery1.delete(0, END)
                entrery1.insert(0, text)
                if len(string_rec1) == 0:
                    string_rec1 = text
                    string_rec_len1 = number
                else:
                    string_rec2 = text
                    string_rec_len2 = number
                entrery1.config(state=DISABLED)
                entrery2.config(state=DISABLED)
                button.config(state=DISABLED)
                if recursive_controll == 2:
                    button3_rec_gen.config(state=ACTIVE)
                    button4_rec_gen.config(state=ACTIVE)
            return
    else:
        if recursive_controll < 2:
            recursive_controll += 1
            button4_rec_gen.config(state=ACTIVE)
        if len(string_rec1) == 0:
            string_rec1 = str(entrery1.get())
            if len(string_rec1) <= 10:
                string_rec_len1 = len(string_rec1)
            else:
                string_rec_len1 = 10
                string_rec1 = string_rec1[:10]
        else:
            string_rec2 = str(entrery1.get())
            if len(string_rec2) <= 10:
                string_rec_len2 = len(string_rec2)
            else:
                string_rec_len2 = 10
                string_rec2 = string_rec2[:10]
        entrery1.config(state=DISABLED)
        entrery2.config(state=DISABLED)
        button.config(state=DISABLED)
        if recursive_controll == 2:
            button3_rec_gen.config(state=ACTIVE)
        return


def reset_all(e1, e2, e3, e4, b1, b2):
    global recursive_controll
    global string_rec1
    global string_rec2
    global string_rec_len1
    global string_rec_len2
    global button3_rec_gen
    global button4_rec_gen

    button3_rec_gen.config(state=DISABLED)
    string_rec1 = ""
    string_rec2 = ""
    string_rec_len1 = 0
    string_rec_len2 = 0

    if recursive_controll > 0:
        recursive_controll -= 1
        button4_rec_gen.config(state=ACTIVE)

    if recursive_controll == 0:
        button4_rec_gen.config(state=DISABLED)


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

# Run Pure Rcursive in other windows
def run_pure_recursive(string1, string2, str_len1, str_len2):
    global button3_rec_gen

    top2 = Toplevel()
    top2.wm_iconbitmap('./img/Halloween.ico')
    top2.title("Pure Recursive Results")
    top2.geometry("400x200+170+150")
    font2 = tkfont.Font(family="Times New Roman", size=16, weight="bold")
    label_frame2 = LabelFrame(top2, text="The Algorithm Results:", padx=2, pady=2)
    label_frame2.configure(font=font2)
    label_frame2.pack(side=TOP, fill=BOTH, expand=1, padx=21, pady=2)

    label1 = Label(label_frame2, text="First String = " + string1 + " String length Equal a : " +
                                      str(str_len1) + "  ", padx=2, pady=2)
    font2 = tkfont.Font(family="Times New Roman", size=12, weight="normal", underline="False")

    label1.configure(font=font2)
    label1.pack(fill=BOTH, expand=1)

    label2 = Label(label_frame2, text="Second String = " + string2 + " String length Equal a : " +
                                      str(str_len2) + "  ", padx=1, pady=1)
    label2.configure(font=font2)
    label2.pack(fill=BOTH, expand=1)

    font2 = tkfont.Font(family="Times New Roman", size=12, weight="normal", underline="True")

    start_time = time()
    min_operations = lcs_recursive(string1, string2)
    end_time = time()
    my_time = '%3f seconds' % (end_time - start_time)
    label3 = Label(label_frame2, text="Result : Minimum Operation(s)" +
                                      " : {0}\nRun Time : {1}".format(str(min_operations),
                                                                      str(my_time)), padx=2, pady=2)
    label3.configure(font=font2)
    label3.pack(fill=BOTH, expand=1)

    button3_rec_gen.config(state=ACTIVE)
    button = Button(label_frame2, text="Dismiss", command=top2.destroy, padx=1, pady=1)
    button.pack()


'''_________________________________________________________________________________________________________________'''
''' Starting with Pure Recursive '''

pure_recursive = IntVar()
my_font = tkfont.Font(family="Times New Roman", size=16, weight="bold", underline="False")
c_box1 = Checkbutton(parent, text='Recursive Algorithm', variabl=pure_recursive, bg='white', font=my_font)
c_box1.place(x=50, y=200)

'''_________________________________________________________________________________________________________________'''
label_string_recursive = Label(parent, text="Enter your 1st String", bg='white')
label_string_recursive.configure(font=my_font)
label_string_recursive.place(x=300, y=201)

entery_rec1 = ttk.Entry(parent)

entery_rec1.place(x=500, y=201, width=140, height=25)
label_string_recursive2 = Label(parent, text="String Size ( <=10 ) : ", bg='white')
label_string_recursive2.place(x=645, y=201)
entery_rec2 = ttk.Entry(parent)
entery_rec2.place(x=760, y=201, width=35, height=25)
entery_rec1.bind('<Return>', on_return1)
entery_rec2.bind('<Return>', on_return1)
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
entery_rec3.bind('<Return>', on_return2)
entery_rec4.bind('<Return>', on_return2)
button2_rec_gen = Button(parent, text='Generate String',
                         command=lambda: set_text_entrey(entery_rec3, entery_rec4, button2_rec_gen))
button2_rec_gen.place(x=800, y=251, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_recursive3 = Label(parent, text="Click to Get a results Test :", bg='white')
label_string_recursive3.configure(font=my_font)
label_string_recursive3.place(x=300, y=301)
string_rec1 = ""
string_rec2 = ""
string_rec_len1 = 0
string_rec_len2 = 0
button3_rec_gen = Button(parent, text='Start Test..', state=DISABLED,
                         command=lambda: run_pure_recursive(string_rec1, string_rec2,
                                                            string_rec_len1,
                                                            string_rec_len2))
button3_rec_gen.place(x=550, y=301)
button4_rec_gen = Button(parent, text='Reset All..', state=DISABLED, command=lambda: reset_all(entery_rec1, entery_rec2,
                                                                                               entery_rec3, entery_rec4,
                                                                                               button1_rec_gen,
                                                                                               button2_rec_gen))
button4_rec_gen.place(x=650, y=301)
''' END OF RECURSIVE '''
'''_________________________________________________________________________________________________________________'''
''' Starting Dynamic partis'''
dynamic_programming = IntVar()
c_box2 = Checkbutton(parent, text='Dynamic Programming', variabl=dynamic_programming, bg='white', fg='blue',
                     font=my_font)
c_box2.place(x=50, y=350)
'''__________________________________________________________________________________________________________________'''
label_string_p_progaming1 = Label(parent, text="Enter your 1st String", bg='white', fg='blue')
label_string_p_progaming1.configure(font=my_font)
label_string_p_progaming1.place(x=300, y=351)

'''__________________________________________________________________________________________________________________'''

entery_progam1 = ttk.Entry(parent)
entery_progam1.place(x=500, y=351, width=140, height=25)

label_string_p_progaming2 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='blue')
label_string_p_progaming2.place(x=645, y=351)
entery_progam2 = ttk.Entry(parent)
entery_progam2.place(x=760, y=351, width=35, height=25)
entery_progam1.bind('<Return>', on_return1)
entery_progam2.bind('<Return>', on_return1)
button_programing1 = Button(parent, text='Generate String')
button_programing1.place(x=800, y=351, width=140, height=25)
'''_________________________________________________________________________________________________________________'''

label_string_p_progaming3 = Label(parent, text="Enter your 2nd String ", bg='white', fg='blue')
label_string_p_progaming3.configure(font=my_font)
label_string_p_progaming3.place(x=300, y=401)
entery_progam3 = ttk.Entry(parent)
entery_progam3.place(x=500, y=401, width=140, height=25)
label_string_progaming4 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='blue')
label_string_progaming4.place(x=645, y=401)
entery_progam4 = ttk.Entry(parent)
entery_progam4.place(x=760, y=401, width=35, height=25)
entery_progam3.bind('<Return>', on_return2)
entery_progam4.bind('<Return>', on_return2)
button_programing2 = Button(parent, text='Generate String')
button_programing2.place(x=800, y=401, width=140, height=25)

''' END OF DYNAMIC PROGRAMING PART'''
'''_________________________________________________________________________________________________________________'''
''' Starting with Greedy Approach'''

greedy_approach = IntVar()
c_box3 = Checkbutton(parent, text='Greedy Approach', variabl=greedy_approach, bg='white', fg='green',
                     font=my_font)
c_box3.place(x=50, y=500)
'''__________________________________________________________________________________________________________________'''

''' END GREEDY APPROACH'''
'''__________________________________________________________________________________________________________________'''
''' Starting with stripe_k'''

stripe_k = IntVar()
c_box4 = Checkbutton(parent, text='Stripe K Algorithm', variabl=stripe_k, bg='white', fg='#01adcb',
                     font=my_font)
c_box4.place(x=50, y=650)
'''__________________________________________________________________________________________________________________'''

''' END GREEDY APPROACH'''
'''__________________________________________________________________________________________________________________'''

separator = Frame(height=3, bd=0, relief=SUNKEN)
separator.pack(fill=X, padx=1, pady=1)
Label(separator, text="Status Bar").pack()
root.mainloop()
