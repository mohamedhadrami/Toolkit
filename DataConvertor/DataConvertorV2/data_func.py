import base64

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