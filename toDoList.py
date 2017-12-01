
import Tkinter
import random

#Creates Root Window
root = Tkinter.Tk()

#Create functions

def add_task():
	pass
	
def del_all():
	pass
	
def del_one():
	pass
	
def sort_asc():
	pass
	
def sort_des():
	pass
	
def choose_random():
	pass
	
def show_number_of_tasks():
	pass


lbl_title = Tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.pack()

lbl_display = Tkinter.Label(root, text="", bg="white")
lbl_display.pack()

txt_input = Tkinter.Entry(root, width=15)
txt_input.pack()

btn_add_task = Tkinter.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_del_all = Tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.pack()

btn_del_one = Tkinter.Button(root, text="Delete One", fg="green", bg="white", command=del_one)
btn_del_one.pack()

btn_sort_asc = Tkinter.Button(root, text="Sort ASC", fg="green", bg="white", command=sort_asc)
btn_sort_asc.pack()

btn_sort_des = Tkinter.Button(root, text="Sort Des", fg="green", bg="white", command=sort_des)
btn_sort_des.pack()

btn_choose_random = Tkinter.Button(root, text="Choose Random", fg="green", bg="white", command=choose_random)
btn_choose_random.pack()

btn_show_number_of_tasks = Tkinter.Button(root, text="Number of Tasks", fg="green", bg="white", command=show_number_of_tasks)
btn_show_number_of_tasks.pack()

btn_exit = Tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_exit.pack()

lb_tasks =Tkinter.Listbox(root)
lb_tasks.pack()




#Starts main loop
root.mainloop()
