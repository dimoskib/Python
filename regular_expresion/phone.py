import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

# print(extract_phone('my number is 432 432-4323'))
# print(extract_phone('my number is 432 432-42323'))

def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

# print(extract_all_phones('my number is 432 432-4323 or 123 321-3333'))
# print(extract_all_phones('my number is 432 432-42323'))


#Option 1 for is_valid_phone
# def is_valid_phone(input):
# 	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
# 	match = phone_regex.fullmatch(input)
# 	if match:
# 		return True
# 	return False

#Option 2 for is_valid_phone
def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	return False

# print(is_valid_phone("432 432-4232"))
# print(is_valid_phone("432 432-4232a"))
# print(is_valid_phone("432 432-4232 a"))