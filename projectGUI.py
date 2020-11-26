from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
from recursive import *
from StringGenerator import *
from random import *

root = Tk()
sizex = 1200
sizey = 600
posx = 200
posy = 200
# set Title
root.title("Advanced Algorithm")

# set root background
root.configure(background="white")
# set root Icon image
root.wm_iconbitmap('./img/Search.ico')

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

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.config(state=NORMAL)
    e2.config(state=NORMAL)
    e3.config(state=NORMAL)
    e4.config(state=NORMAL)
    b1.config(state=ACTIVE)
    b2.config(state=ACTIVE)
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

    label2 = Label(label_frame2, text="2nd String = " + string2 + " String length Equal a : " +
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


def test_entery_int2(entery, minimum, maximum):
    try:
        int(entery.get())
        my_number = int(entery.get())
        if minimum <= my_number <= maximum:
            return 1
        else:
            messagebox.showerror(title="String Size Input", message="Error : Please input : " + str(minimum) +
                                                                    " < = Number <= " + str(maximum) + "\r\n" +
                                                                    "OR KEEP IT EMPTY \r\n!!" +
                                                                    "String Size Randomize bitween 10 & 20")
            return 0
    except ValueError:
        messagebox.showerror(title="String Size Input", message="Error :" +
                                                                "Please input a <NUMBER> Value\r\n" +
                                                                "Or KEEP IT EMPTY\r\n" +
                                                                "String Size Randomize bitween 10 & 20")
        return 0


p_dynamic = 0


def generate_string_dynamic(string_entery, size_entery, generator_button, reset_button):
    global string_p_dynamic1
    global string_p_dynamic2
    if len(str(string_entery.get())) == 0:
        if len(str(size_entery.get())) == 0:
            my_random = randrange(10, 17, 2)
            my_random_string = random_string(chars=string.ascii_uppercase, longer=my_random)
            if len(string_p_dynamic1) == 0:
                string_p_dynamic1 = my_random_string
            else:
                string_p_dynamic2 = my_random_string
            string_entery.delete(0, END)
            string_entery.insert(0, string_p_dynamic1)
            size_entery.delete(0, END)
            size_entery.insert(0, str(my_random))
            generator_button.config(state=DISABLED)
            size_entery.config(state=DISABLED)
            string_entery.config(state=DISABLED)
            reset_button.config(state=ACTIVE)
            return
        else:
            if test_entery_int2(size_entery, 10, 20) == 1:
                my_longer = int(size_entery.get())
                my_random_string = random_string(chars=string.ascii_uppercase, longer=my_longer)
                if len(string_p_dynamic1) == 0:
                    string_p_dynamic1 = my_random_string
                else:
                    string_p_dynamic1 = my_random_string
                string_entery.delete(0, END)
                string_entery.insert(0, my_random_string)
                generator_button.config(state=DISABLED)
                size_entery.config(state=DISABLED)
                string_entery.config(state=DISABLED)
                reset_button.config(state=ACTIVE)
                return
            else:
                messagebox.showerror("Error Input N1", "Error in input Number !!")
                return
    else:
        if len(str(size_entery.get())) == 0:
            if len(string_p_dynamic1) == 0:
                string_p_dynamic1 = str(string_entery.get())
            else:
                string_p_dynamic2 = str(string_entery.get())
            my_longer = str(len(string_entery.get()))
            size_entery.delete(0, END)
            size_entery.insert(0, my_longer)
            generator_button.config(state=DISABLED)
            size_entery.config(state=DISABLED)
            string_entery.config(state=DISABLED)
            reset_button.config(state=ACTIVE)
            return
        else:
            if test_entery_int2(size_entery, 10, 20) == 1:
                my_longer = int(size_entery.get())
                my_string_entery = str(string_entery.get())
                my_string_entery = my_string_entery[:my_longer]
                if len(string_p_dynamic1) == 0:
                    string_p_dynamic1 = my_string_entery
                else:
                    string_p_dynamic2 = my_string_entery
                string_entery.delete(0, END)
                string_entery.insert(0, my_string_entery)
                size_entery.delete(0, END)
                size_entery.insert(0, my_longer)
                generator_button.config(state=DISABLED)
                size_entery.config(state=DISABLED)
                string_entery.config(state=DISABLED)
                reset_button.config(state=ACTIVE)
                return
            else:
                messagebox.showerror("Error Input N2", "Error in input Number !!!!")
                return


def reset_all_2(*args):
    n = len(args)
    for i in range(n):
        print("arg : ", i, "\ntype of : ", type(args[i]), "\nits : ", args[i])
        if isinstance(args[i], str):
            print("N° ", i, " Is String class")
            args[i]= "hello"
        if isinstance(args[i], ttk.Entry):
            print("N° ", i, " Is String tkinter ttk Entry")
        if isinstance(args[i], Button):
            print("N° ", i, " Is String tkinter ttk Button")
    print("args size = {0}".format(n))


'''END METHODE INSERTION TO STRING'''

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

entery_p_dynamic_string1 = ttk.Entry(parent)
entery_p_dynamic_string1.place(x=500, y=351, width=140, height=25)

label_string_p_progaming2 = Label(parent, text="String Size : ", bg='white', fg='blue')
label_string_p_progaming2.place(x=645, y=351)
entery_p_dynamic_size1 = ttk.Entry(parent)
entery_p_dynamic_size1.place(x=760, y=351, width=35, height=25)
entery_p_dynamic_string1.bind('<Return>')
entery_p_dynamic_size1.bind('<Return>')
button_p_dyanamic_generator1 = Button(parent, text='Generate String',
                                      command=lambda: generate_string_dynamic(entery_p_dynamic_string1,
                                                                              entery_p_dynamic_size1,
                                                                              button_p_dyanamic_generator1,
                                                                              button_p_dynamic_rest))
button_p_dyanamic_generator1.place(x=800, y=351, width=140, height=25)
'''_________________________________________________________________________________________________________________'''

label_string_p_progaming3 = Label(parent, text="Enter your 2nd String ", bg='white', fg='blue')
label_string_p_progaming3.configure(font=my_font)
label_string_p_progaming3.place(x=300, y=401)
entery_p_dynamic_string2 = ttk.Entry(parent)
entery_p_dynamic_string2.place(x=500, y=401, width=140, height=25)
label_string_progaming4 = Label(parent, text="String Size  : ", bg='white', fg='blue')
label_string_progaming4.place(x=645, y=401)
entery_p_dynamic_size2 = ttk.Entry(parent)
entery_p_dynamic_size2.place(x=760, y=401, width=35, height=25)
entery_p_dynamic_string2.bind('<Return>', )
entery_p_dynamic_size2.bind('<Return>', )
button_p_dyanamic_generator2 = Button(parent, text='Generate String',
                                      command=lambda: generate_string_dynamic(entery_p_dynamic_string2,
                                                                              entery_p_dynamic_size2,
                                                                              button_p_dyanamic_generator2,
                                                                              button_p_dynamic_rest))
button_p_dyanamic_generator2.place(x=800, y=401, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_p_dynamic5 = Label(parent, text="Click to Get a results Test :", bg='white', fg='blue')
label_p_dynamic5.configure(font=my_font)
label_p_dynamic5.place(x=300, y=451)
string_p_dynamic1 = ""
string_p_dynamic2 = ""
string_p_dynamic_length1 = 0
string_p_dynamic_length2 = 0
button_p_dynamic_start = Button(parent, text='Start Test..', state=DISABLED)
button_p_dynamic_start.place(x=550, y=451)
button_p_dynamic_rest = Button(parent, text='Reset All..', state=DISABLED, command=lambda: reset_all_2(string_p_dynamic1, string_p_dynamic2, entery_p_dynamic_string1,button_p_dynamic_rest))
button_p_dynamic_rest.place(x=650, y=451)

''' END OF DYNAMIC PROGRAMING PART'''
'''_________________________________________________________________________________________________________________'''
''' Starting with Greedy Approach'''

greedy_approach = IntVar()
c_box3 = Checkbutton(parent, text='Greedy Approach', variabl=greedy_approach, bg='white', fg='green',
                     font=my_font)
c_box3.place(x=50, y=500)
'''__________________________________________________________________________________________________________________'''
label_string_greedy1 = Label(parent, text="Enter your 1st String", bg='white', fg='green')
label_string_greedy1.configure(font=my_font)
label_string_greedy1.place(x=300, y=501)
entery_greedy_string1 = ttk.Entry(parent)
entery_greedy_string1.place(x=500, y=501, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_greedy_size1 = Label(parent, text="String Size  : ", bg='white', fg='green')
label_greedy_size1.place(x=645, y=501)
entery_greedy_size1 = ttk.Entry(parent)
entery_greedy_size1.place(x=760, y=501, width=35, height=25)
entery_greedy_size1.bind('<Return>', on_return1)
entery_greedy_string1.bind('<Return>', on_return1)
button_greedy_generate1 = Button(parent, text='Generate String')
button_greedy_generate1.place(x=800, y=501, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_greedy2 = Label(parent, text="Enter your 2nd String", bg='white', fg='green')
label_string_greedy2.configure(font=my_font)
label_string_greedy2.place(x=300, y=551)
entery_greedy_string2 = ttk.Entry(parent)
entery_greedy_string2.place(x=500, y=551, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_greedy_size2 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='green')
label_greedy_size2.place(x=645, y=551)
entery_greedy_size2 = ttk.Entry(parent)
entery_greedy_size2.place(x=760, y=551, width=35, height=25)
entery_greedy_size2.bind('<Return>', on_return1)
entery_greedy_string2.bind('<Return>', on_return1)
button_greedy_generate2 = Button(parent, text='Generate String')
button_greedy_generate2.place(x=800, y=551, width=140, height=25)

'''__________________________________________________________________________________________________________________'''
label_greedy_get_result = Label(parent, text="Click to Get a results Test :", bg='white', fg='green')
label_greedy_get_result.configure(font=my_font)
label_greedy_get_result.place(x=300, y=600)
string_greedy1 = ""
string_greedy2 = ""
string_greedy_length1 = 0
string_greedy_length2 = 0
button_greedy_start = Button(parent, text='Start Test..', state=DISABLED)
button_greedy_start.place(x=550, y=601)
button_greedy_rest = Button(parent, text='Reset All..', state=DISABLED)
button_greedy_rest.place(x=650, y=601)
''' END GREEDY APPROACH'''
'''__________________________________________________________________________________________________________________'''
''' Starting with stripe_k'''

stripe_k = IntVar()
c_box4 = Checkbutton(parent, text='Stripe K Algorithm', variabl=stripe_k, bg='white', fg='#01adcb',
                     font=my_font)
c_box4.place(x=50, y=650)
'''__________________________________________________________________________________________________________________'''
label_string_stripe_k1 = Label(parent, text="Enter your 1st String", bg='white', fg='#01adcb')
label_string_stripe_k1.configure(font=my_font)
label_string_stripe_k1.place(x=300, y=650)
entery_stripe_k_string1 = ttk.Entry(parent)
entery_stripe_k_string1.place(x=500, y=650, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_stripe_k_size1 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='#01adcb')
label_stripe_k_size1.place(x=645, y=650)
entery_stripe_k_size1 = ttk.Entry(parent)
entery_stripe_k_size1.place(x=760, y=650, width=35, height=25)
entery_stripe_k_size1.bind('<Return>', on_return1)
entery_stripe_k_string1.bind('<Return>', on_return1)
button_stripe_k_generate1 = Button(parent, text='Generate String')
button_stripe_k_generate1.place(x=800, y=650, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_stripe_k2 = Label(parent, text="Enter your 2nd String", bg='white', fg='#01adcb')
label_string_stripe_k2.configure(font=my_font)
label_string_stripe_k2.place(x=300, y=701)
entery_stripe_k_string2 = ttk.Entry(parent)
entery_stripe_k_string2.place(x=500, y=701, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_stripe_k_size2 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='#01adcb')
label_stripe_k_size2.place(x=645, y=701)
entery_stripe_k_size2 = ttk.Entry(parent)
entery_stripe_k_size2.place(x=760, y=701, width=35, height=25)
entery_stripe_k_size2.bind('<Return>', on_return1)
entery_stripe_k_string2.bind('<Return>', on_return1)
button_stripe_k_generate2 = Button(parent, text='Generate String')
button_stripe_k_generate2.place(x=800, y=701, width=140, height=25)

'''__________________________________________________________________________________________________________________'''
label_stripe_k_get_result = Label(parent, text="Click to Get a results Test :", bg='white', fg='#01adcb')
label_stripe_k_get_result.configure(font=my_font)
label_stripe_k_get_result.place(x=300, y=750)
string_stripe_k1 = ""
string_stripe_k2 = ""
string_stripe_k_length1 = 0
string_stripe_k_length2 = 0
button_stripe_k_start = Button(parent, text='Start Test..', state=DISABLED)
button_stripe_k_start.place(x=550, y=751)
button_stripe_k_rest = Button(parent, text='Reset All..', state=DISABLED)
button_stripe_k_rest.place(x=650, y=751)
''' END STRIPE K'''
'''__________________________________________________________________________________________________________________'''
''' Starting with DP and Devide And Conquer'''

dp_devide = IntVar()
c_box5 = Checkbutton(parent, text='Divide & Conquer', variabl=dp_devide, bg='white', fg='#ffd300',
                     font=my_font)
c_box5.place(x=50, y=800)
'''__________________________________________________________________________________________________________________'''
label_string_dp_devide1 = Label(parent, text="Enter your 1st String", bg='white', fg='#ffd300')
label_string_dp_devide1.configure(font=my_font)
label_string_dp_devide1.place(x=300, y=800)
entery_dp_devide_string1 = ttk.Entry(parent)
entery_dp_devide_string1.place(x=500, y=800, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_dp_devide_size1 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='#ffd300')
label_dp_devide_size1.place(x=645, y=800)
entery_dp_devide_size1 = ttk.Entry(parent)
entery_dp_devide_size1.place(x=760, y=800, width=35, height=25)
entery_dp_devide_size1.bind('<Return>', on_return1)
entery_dp_devide_string1.bind('<Return>', on_return1)
button_dp_devide_generate1 = Button(parent, text='Generate String')
button_dp_devide_generate1.place(x=800, y=800, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_dp_devide2 = Label(parent, text="Enter your 2nd String", bg='white', fg='#ffd300')
label_string_dp_devide2.configure(font=my_font)
label_string_dp_devide2.place(x=300, y=851)
entery_dp_devide_string2 = ttk.Entry(parent)
entery_dp_devide_string2.place(x=500, y=851, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_dp_devide_size2 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='#ffd300')
label_dp_devide_size2.place(x=645, y=851)
entery_dp_devide_size2 = ttk.Entry(parent)
entery_dp_devide_size2.place(x=760, y=851, width=35, height=25)
entery_dp_devide_size2.bind('<Return>', on_return1)
entery_dp_devide_string2.bind('<Return>', on_return1)
button_dp_devide_generate2 = Button(parent, text='Generate String')
button_dp_devide_generate2.place(x=800, y=851, width=140, height=25)

'''__________________________________________________________________________________________________________________'''
label_dp_devide_get_result = Label(parent, text="Click to Get a results Test :", bg='white', fg='#ffd300')
label_dp_devide_get_result.configure(font=my_font)
label_dp_devide_get_result.place(x=300, y=900)
string_dp_devide1 = ""
string_dp_devide2 = ""
string_dp_devide_length1 = 0
string_dp_devide_length2 = 0
button_dp_devide_start = Button(parent, text='Start Test..', state=DISABLED)
button_dp_devide_start.place(x=550, y=901)
button_dp_devide_rest = Button(parent, text='Reset All..', state=DISABLED)
button_dp_devide_rest.place(x=650, y=901)
''' END DP & DEVIDE AND CONQUER'''
'''__________________________________________________________________________________________________________________'''
''' Starting with  Branch and Bond'''

branch_bond = IntVar()
c_box6 = Checkbutton(parent, text=' Branch and Bond', variabl=branch_bond, bg='white', fg='#793AB4',
                     font=my_font)
c_box6.place(x=50, y=950)
'''__________________________________________________________________________________________________________________'''
label_string_branch_bond1 = Label(parent, text="Enter your 1st String", bg='white', fg='#793AB4')
label_string_branch_bond1.configure(font=my_font)
label_string_branch_bond1.place(x=300, y=950)
entery_branch_bond_string1 = ttk.Entry(parent)
entery_branch_bond_string1.place(x=500, y=950, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_branch_bond_size1 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='#793AB4')
label_branch_bond_size1.place(x=645, y=950)
entery_branch_bond_size1 = ttk.Entry(parent)
entery_branch_bond_size1.place(x=760, y=950, width=35, height=25)
entery_branch_bond_size1.bind('<Return>', on_return1)
entery_branch_bond_string1.bind('<Return>', on_return1)
button_branch_bond_generate1 = Button(parent, text='Generate String')
button_branch_bond_generate1.place(x=800, y=950, width=140, height=25)
'''_________________________________________________________________________________________________________________'''
label_string_branch_bond2 = Label(parent, text="Enter your 2nd String", bg='white', fg='#793AB4')
label_string_branch_bond2.configure(font=my_font)
label_string_branch_bond2.place(x=300, y=1001)
entery_branch_bond_string2 = ttk.Entry(parent)
entery_branch_bond_string2.place(x=500, y=1001, width=140, height=25)
'''__________________________________________________________________________________________________________________'''
label_branch_bond_size2 = Label(parent, text="String Size ( <=10 ) : ", bg='white', fg='#793AB4')
label_branch_bond_size2.place(x=645, y=1001)
entery_branch_bond_size2 = ttk.Entry(parent)
entery_branch_bond_size2.place(x=760, y=1001, width=35, height=25)
entery_branch_bond_size2.bind('<Return>', on_return1)
entery_branch_bond_string2.bind('<Return>', on_return1)
button_branch_bond_generate2 = Button(parent, text='Generate String')
button_branch_bond_generate2.place(x=800, y=1001, width=140, height=25)

'''_________________________________________________________________________________________________________'''
label_branch_bond_get_result = Label(parent, text="Click to Get a results Test :", bg='white', fg='#793AB4')
label_branch_bond_get_result.configure(font=my_font)
label_branch_bond_get_result.place(x=300, y=1051)
string_branch_bond1 = ""
string_branch_bond2 = ""
string_branch_bond_length1 = 0
string_branch_bond_length2 = 0
button_branch_bond_start = Button(parent, text='Start Test..', state=DISABLED)
button_branch_bond_start.place(x=550, y=1051)
button_branch_bond_rest = Button(parent, text='Reset All..', state=DISABLED)
button_branch_bond_rest.place(x=650, y=1051)
'''END BRANCH AND BOND'''
'''__________________________________________________________________________________________________________________'''

separator = Frame(height=3, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=1, pady=1)
Label(separator, text="All Rights Recived 2020 University Jean Monnet - Saint Etienne 42000- France").pack()
Label(separator, text="This program was developed by students of the University of Computer Science").pack()
root.mainloop()
