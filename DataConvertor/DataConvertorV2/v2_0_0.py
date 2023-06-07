from tkinter import *
import pickle
from data_func import *
import data_func

data = data_func.binary_to_binary(1)

def validate_data(data_type, data_value):
	if data_type == 'Binary': # Binary
		valid_chars = set('01')
		if set(data_value).issubset(valid_chars):
			return True, valid_chars
		else:
			return False, valid_chars
	elif data_type == 'Octal': # Octal
		valid_chars = set('01234567')
		if set(data_value).issubset(valid_chars):
			return True, valid_chars
		else:
			return False, valid_chars
	elif data_type == 'Decimal': # Decimal
		valid_chars = set("0123456789")
		if data_value.isnumeric():
			return True, valid_chars
		else:
			return False, valid_chars
	elif data_type == 'Hexadecimal': # Hexadecimal
		valid_chars = set('0123456789ABCDEFabcdef')
		if set(data_value).issubset(valid_chars):
			return True, valid_chars
		else:
			return False, valid_chars
	elif data_type == 'Base64': # Base64
		valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
		if set(data_value).issubset(valid_chars):
			return True, valid_chars
		else:
			return False, valid_chars
	elif data_type == 'ASCII': # ASCII
		# No validation needed
		return True, " "
	else:
		# Invalid input conversion
		return False

def add_element_to_dict(dict, key, value):
	if key not in dict:
		dict[key] = []
	dict[key].append(value)

def convert_data():
    for i in options:
        output_labels[i][0].config( text = " " )
    input_type = clicked.get()
    input_data = data.get()
    desired_outputs = [i for i in options_dict if options_dict[i].get()]
    for output in desired_outputs:
        curr_conv = conversion_functions.get((input_type, output))
        res = curr_conv(input_data)
        output_labels[output][0].config( text = str(res) )

def handle_data():
    ret, valid_chars = validate_data(clicked.get(), data.get())
    if ret:
        data_valid.config( text = " " )
        convert_data()
    else:
        output_text = "Format incorrect. Must use the following chars: " + str(valid_chars)
        data_valid.config( text = output_text )

# Metadata
version = "v2.0.0"
creator = "Mohamed Hadrami"
title = "Ultimate Data Convertor"
options = [ 'Binary' , 'Octal', 'Decimal', 'Hexadecimal', 'Base64', 'ASCII']
maxCol = 3
maxRow = len(options) + 3
with open('dict_func.txt', 'rb') as func:
	functions = func.read()
conversion_functions = pickle.loads(functions)

root = Tk() # Initialize GUI

# Set up
root.title('Ultimate Data Convertor')
canvas = Canvas(root, width=600, height=300)
canvas.grid(columnspan=maxCol, rowspan=maxRow)

title_text = Label( root, text=title, font="Times 16 bold" )
title_text.grid( columnspan=maxCol, row=0 , column=0 )
step_1 = Label( root, text="Step 1: Select a data type and input the data you want to convert", wraplength=150 )
step_1.grid(row=1,column=0 )
step_2 = Label( root, text="Step 2: Select which data types you want converted to", wraplength=150 )
step_2.grid(row=1,column=1 )
step_3 = Label( root, text="Step 3: Enjoy the output!", wraplength=150 )
step_3.grid(row=1,column=2 )
version_text = Label( root, text=version )
version_text.grid( row=maxRow, column=maxCol, sticky='e' )
creator_text = Label( root, text=creator )
creator_text.grid( row=maxRow, column=0, sticky='w' )

# First Column
clicked = StringVar()
clicked.set("Binary")
drop = OptionMenu( root, clicked, *options )
drop.grid(row=2,column=0)
data = Entry(root, bd=5)
data.grid(row=3,column=0)
data_valid = Label( root, text = " ", wraplength=150, fg="#f00" )
data_valid.grid(rowspan=3,row=4,column=0)

# Second Column
options_select = []
for i in range(len(options)):
    options_select.append(IntVar())
    temp = Checkbutton( root, text=options[i], variable=options_select[i] )
    temp.grid(row=i+2,column=1)
options_dict = dict(zip(options, options_select))
Button( root, text='CONVERT!', command=handle_data).grid(row=maxRow-1, column=1)


# Third Column
output_labels = {}
for i in range(len(options)):
    temp = Label( root, text=" ", wraplength=150)
    add_element_to_dict(output_labels, options[i], temp)
    temp.grid(row=i+2,column=2)

root.mainloop()