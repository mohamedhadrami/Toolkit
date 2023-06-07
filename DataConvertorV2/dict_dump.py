from data_func import *

conversion_functions = {
		('Binary', 'Binary'): binary_to_binary,
		('Binary', 'Octal'): binary_to_octal,
		('Binary', 'Decimal'): binary_to_decimal,
		('Binary', 'Hexadecimal'): binary_to_hexadecimal,
		('Binary', 'Base64'): binary_to_base64,
		('Binary', 'ASCII'): binary_to_ascii,
		('Octal', 'Binary'): octal_to_binary,
		('Octal', 'Octal'): octal_to_octal,
		('Octal', 'Decimal'): octal_to_decimal,
		('Octal', 'Hexadecimal'): octal_to_hexadecimal,
		('Octal', 'Base64'): octal_to_base64,
		('Octal', 'ASCII'): octal_to_ascii,
		('Decimal', 'Binary'): decimal_to_binary,
		('Decimal', 'Octal'): decimal_to_octal,
		('Decimal', 'Decimal'): decimal_to_decimal,
		('Decimal', 'Hexadecimal'): decimal_to_hexadecimal,
		('Decimal', 'Base64'): decimal_to_base64,
		('Decimal', 'ASCII'): decimal_to_ascii,
		('Hexadecimal', 'Binary'): hexadecimal_to_binary,
		('Hexadecimal', 'Octal'): hexadecimal_to_octal,
		('Hexadecimal', 'Decimal'): hexadecimal_to_decimal,
		('Hexadecimal', 'Hexadecimal'): hexadecimal_to_hexadecimal,
		('Hexadecimal', 'Base64'): hexadecimal_to_base64,
		('Hexadecimal', 'ASCII'): hexadecimal_to_ascii,
		('Base64', 'Binary'): base64_to_binary,
		('Base64', 'Octal'): base64_to_octal,
		('Base64', 'Decimal'): base64_to_decimal,
		('Base64', 'Hexadecimal'): base64_to_hexadecimal,
		('Base64', 'Base64'): base64_to_base64,
		('Base64', 'ASCII'): base64_to_ascii,
		('ASCII', 'Binary'): ascii_to_binary,
		('ASCII', 'Octal'): ascii_to_octal,
		('ASCII', 'Decimal'): ascii_to_decimal,
		('ASCII', 'Hexadecimal'): ascii_to_hexadecimal,
		('ASCII', 'Base64'): ascii_to_base64,
		('ASCII', 'ASCII'): ascii_to_ascii
	}

# importing the module
import pickle
  
# opening file in write mode (binary)
file = open("dict_func.txt", "wb")
  
# serializing dictionary 
pickle.dump(conversion_functions, file)
  
# closing the file
file.close()