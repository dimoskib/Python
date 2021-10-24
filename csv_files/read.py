# BAD!
# with open('example.csv') as file:
# 	data = file.read()


# using reader
# from csv import reader
# with open('example.csv') as file:
# 	csv_reader = reader(file)
# 	next(csv_reader)
# 	for fighter in csv_reader:
# 		print(f'{fighter[0]} is from {fighter[1]}')


# using DictReader
from csv import DictReader
with open('example.csv') as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		print(row)