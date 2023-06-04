import sys
import base64

conversions = { '1':'Binary' , '2':'Octal', '3':'Decimal', '4':'Hexadecimal', '5':'Base64', '6':'ASCII' }

def validate_inputs(state: int, data):
	valid_inputs = ['1', '2', '3', '4', '5', '6']
	if state == "input":
		res = data
		while res not in valid_inputs:
			print("Invalid input. Please enter a valid option.")
			res = input()
		return res
	elif state == "output":
		output_conv = data
		output_list = output_conv.split()
		invalid_outputs = []
		attempts = 0
		while any(output not in valid_inputs for output in output_list):
			for output in output_list:
				if output not in valid_inputs:
					invalid_outputs.append(output)
			if invalid_outputs:
				print("Invalid output options:", ', '.join(invalid_outputs))
				print("Please provide the correction for these invalid outputs.")
				output_list = [output for output in output_list if output not in invalid_outputs]
			new_output = input()
			new_output_list = new_output.split()
			output_list.extend(new_output_list)
			invalid_outputs = []
			attempts += 1
			if attempts == 2:
				print("\nThat's enough!")
				sys.exit("Come back when you've figured out what you want to do.")
		res = [*set(output_list)]
		return res

def validate_data(data_type, data):
	if data_type == '1': # Binary
		valid_chars = set('01')
		if set(data).issubset(valid_chars):
			return True
		else:
			return False
	elif data_type == '2': # Octal
		valid_chars = set('01234567')
		if set(data).issubset(valid_chars):
			return True
		else:
			return False
	elif data_type == '3': # Decimal
		if data.isnumeric():
			return True
		else:
			return False
	elif data_type == '4': # Hexadecimal
		valid_chars = set('0123456789ABCDEFabcdef')
		if set(data).issubset(valid_chars):
			return True
		else:
			return False
	elif data_type == '5': # Base64
		valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
		if set(data).issubset(valid_chars):
			return True
		else:
			return False
	elif data_type == '6': # ASCII
		# No validation needed
		return True
	else:
		# Invalid input conversion
		return False

def add_element_to_dict(dict, key, value):
	if key not in dict:
		dict[key] = []
	dict[key].append(value)



################# BINARY #################

def binary_to_binary(data):
	# No computation needed
	return data

def binary_to_octal(data):
	data = data.zfill((len(data) + 2) // 3 * 3)
	data = ''.join(str(int(data[i:i+3], 2)) for i in range(0, len(data), 3))
	return data

def binary_to_decimal(data):
	data = int(data, 2)
	return data

def binary_to_hexadecimal(data):
	data = data.zfill((len(data) + 3) // 4 * 4)
	data = ''.join(hex(int(data[i:i+4], 2))[2:] for i in range(0, len(data), 4))
	return data

def binary_to_base64(data):
	data = data.zfill((len(data) // 8) * 8)
	data = bytes([int(data[i:i+8], 2) for i in range(0, len(data), 8)])
	data = base64.b64encode(data).decode('utf-8')
	return data

def binary_to_ascii(data):
	data = data.zfill((len(data) // 8) * 8)
	data = [data[i:i+8] for i in range(0, len(data), 8)]
	data = ''.join(chr(int(byte, 2)) for byte in data)
	return data


################# OCTAL #################

def octal_to_binary(data):
	data = int(data, 8)
	data = bin(data)[2:]
	return data

def octal_to_octal(data):
	# No computation needed
	return data

def octal_to_decimal(data):
	data = octal_to_binary(data)
	data = binary_to_decimal(data)
	return data

def octal_to_hexadecimal(data):
	data = octal_to_binary(data)
	data = binary_to_hexadecimal(data)
	return data

def octal_to_base64(data):
	data = octal_to_binary(data)
	data = binary_to_base64(data)
	return data

def octal_to_ascii(data):
	data = octal_to_binary(data)
	data = binary_to_ascii(data)
	return data
	
	
################# DECIMAL #################

def decimal_to_binary(data):
	data = bin(int(data))[2:]
	return data

def decimal_to_octal(data):
	data = decimal_to_binary(data)
	data = binary_to_octal(data)
	return data

def decimal_to_decimal(data):
	# No computation needed
	return data

def decimal_to_hexadecimal(data):
	data = decimal_to_binary(data)
	data = binary_to_hexadecimal(data)
	return data

def decimal_to_base64(data):
	data = decimal_to_binary(data)
	data = binary_to_base64(data)
	return data

def decimal_to_ascii(data):
	data = decimal_to_binary(data)
	data = binary_to_ascii(data)
	return data


################# HEXADECIMAL #################

def hexadecimal_to_binary(data):
	data = int(data, 16)
	data = bin(data)[2:]
	return data

def hexadecimal_to_octal(data):
	data = hexadecimal_to_binary(data)
	data = binary_to_octal(data)
	return data

def hexadecimal_to_decimal(data):
	data = hexadecimal_to_binary(data)
	data = binary_to_decimal(data)
	return data

def hexadecimal_to_hexadecimal(data):
	# No computation needed
	return data

def hexadecimal_to_base64(data):
	data = hexadecimal_to_binary(data)
	data = binary_to_base64(data)
	return data

def hexadecimal_to_ascii(data):
	data = hexadecimal_to_binary(data)
	data = binary_to_ascii(data)
	return data


################# BASE64 #################

def base64_to_binary(data):
	data = base64.b64decode(data)
	data = bin(int.from_bytes(data, 'big'))[2:]
	return data

def base64_to_octal(data):
	data = base64_to_binary(data)
	data = binary_to_octal(data)
	return data

def base64_to_decimal(data):
	data = base64_to_binary(data)
	data = binary_to_decimal(data)
	return data

def base64_to_hexadecimal(data):
	data = base64_to_binary(data)
	data = binary_to_hexadecimal(data)
	return data

def base64_to_base64(data):
	# No computation needed
	return data

def base64_to_ascii(data):
	data = base64_to_binary(data)
	data = binary_to_ascii(data)
	return data


################# ASCII #################

def ascii_to_binary(data):
	data = ''.join(format(ord(char), '08b') for char in data)
	return data

def ascii_to_octal(data):
	data = ascii_to_binary(data)
	data = binary_to_octal(data)
	return data

def ascii_to_decimal(data):
	data = ascii_to_binary(data)
	data = binary_to_decimal(data)
	return data

def ascii_to_hexadecimal(data):
	data = ascii_to_binary(data)
	data = binary_to_hexadecimal(data)
	return data

def ascii_to_base64(data):
	data = ascii_to_binary(data)
	data = binary_to_base64(data)
	return data

def ascii_to_ascii(data):
	# No computation needed
    	return data


def data_parser(input_conv, output_conv, data):
	conversion_functions = {
		('1', '1'): binary_to_binary,
		('1', '2'): binary_to_octal,
		('1', '3'): binary_to_decimal,
		('1', '4'): binary_to_hexadecimal,
		('1', '5'): binary_to_base64,
		('1', '6'): binary_to_ascii,
		('2', '1'): octal_to_binary,
		('2', '2'): octal_to_octal,
		('2', '3'): octal_to_decimal,
		('2', '4'): octal_to_hexadecimal,
		('2', '5'): octal_to_base64,
		('2', '6'): octal_to_ascii,
		('3', '1'): decimal_to_binary,
		('3', '2'): decimal_to_octal,
		('3', '3'): decimal_to_decimal,
		('3', '4'): decimal_to_hexadecimal,
		('3', '5'): decimal_to_base64,
		('3', '6'): decimal_to_ascii,
		('4', '1'): hexadecimal_to_binary,
		('4', '2'): hexadecimal_to_octal,
		('4', '3'): hexadecimal_to_decimal,
		('4', '4'): hexadecimal_to_hexadecimal,
		('4', '5'): hexadecimal_to_base64,
		('4', '6'): hexadecimal_to_ascii,
		('5', '1'): base64_to_binary,
		('5', '2'): base64_to_octal,
		('5', '3'): base64_to_decimal,
		('5', '4'): base64_to_hexadecimal,
		('5', '5'): base64_to_base64,
		('5', '6'): base64_to_ascii,
		('6', '1'): ascii_to_binary,
		('6', '2'): ascii_to_octal,
		('6', '3'): ascii_to_decimal,
		('6', '4'): ascii_to_hexadecimal,
		('6', '5'): ascii_to_base64,
		('6', '6'): ascii_to_ascii
	}
	
	final_output = {}
	for output in output_conv:
		curr_conv = conversion_functions.get((input_conv, output))
		curr_conv_name = conversions.get(output)
		res = curr_conv(data)
		add_element_to_dict(final_output, curr_conv_name, res)
	
	return final_output
		

def convertor():
	#### TAKE INPUT CONVERSION ####
	print("Select an input conversion:")
	print("\t\t(1) Binary \t[Base-2]\n \
		(2) Octal \t[Base-8]\n \
		(3) Decimal \t[Base-10]\n \
		(4) Hexadecimal [Base-16]\n \
		(5) Base64 \t[Base-64]\n \
		(6) ASCII")
	input_conv = input()
	input_conv = validate_inputs("input", input_conv)
	
	#### TAKE OUTPUT CONVERSION ####
	print("\nWhich outputs do you want?")
	print("\t\t(1) Binary \t[Base-2]\n \
		(2) Octal \t[Base-8]\n \
		(3) Decimal \t[Base-10]\n \
		(4) Hexadecimal [Base-16]\n \
		(5) Base64 \t[Base-64]\n \
		(6) ASCII")
	print("If multiple outputs are desired, please place a space in between each input")
	output_conv = input()
	output_conv = validate_inputs("output", output_conv)
	
	#### TAKE INPUT VALUE AND VALIDATE ####
	print("Please input the data now")
	data = input()
	# Validate data based on input selection
	while not validate_data(input_conv, data):
		print("Invalid input data for selected conversion.")
		data = input()
	#### GET RESULTS AND PRINT ####
	final_output = data_parser(input_conv, output_conv, data)
	print("\n######### RESULTS #########")
	for key, value in final_output.items():
		print(str(key) + ":  \t" + str(value[0]))
	

if __name__ == '__main__':
	print("\n\nWelcome to the Ultimate Data Convertor!\n\n")
	convertor()





