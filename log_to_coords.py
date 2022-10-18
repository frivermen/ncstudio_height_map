import sys
from parse import search

if (len(sys.argv) > 1): # работаем только если был путь при запуске
	path = sys.argv[1] # получаем этот путь

	output_buffer = []

	log_file = open(path, "r", encoding='latin-1') # открываем лог
	log_buffer = log_file.readlines()

	for i in reversed(range(len(log_buffer))): # начинаем с конца файла
		# если нашли начало карты высот
		if (log_buffer[i].find("Initiate a machining task:") > -1):
			# проходимся по строчка к концу файла
			for j in range(i, len(log_buffer)):
				# если в строке есть координаты забираем их
				if (log_buffer[j].find("Current MC:") > -1):
					coords = search('X={}, Y={}, Z={},', log_buffer[j])

					output_buffer.append( # добавляем координаты в буффер
							coords[0] + ", " + coords[1] + ", " + coords[2] + "\n")

			break # т.к. мы уже закончили искать вверх уже не надо

	log_file.close() # закрываем лог

	# если файла с координатами нет, он будет создан в каталоге со скриптом
	output_file = open("clean_coords.txt", "w", encoding='latin-1')
	output_file.writelines(output_buffer)
	output_file.close()

else:
	print('argument not found') # сообщение, если не был передан путь
