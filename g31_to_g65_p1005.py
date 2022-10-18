import sys

if (len(sys.argv) > 1):
	path = sys.argv[1]

	file = open(path, "r", encoding='latin-1')
	line_buffer = file.readlines()

	for i in range(len(line_buffer)): # перебираем строки
		if (line_buffer[i].find("G31") > -1): # если находим строку с G31, то
			line_buffer[i] = "G65 P1005\n" # заменяем ее

	file.close()

	# записываем в тот же файл, что открыли
	file = open(path, "w")
	file.writelines(line_buffer)
	file.close()

else:
	print('argument not found')
