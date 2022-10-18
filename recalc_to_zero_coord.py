import sys
from parse import search

if (len(sys.argv) > 1):
	path = sys.argv[1]

	output_buffer = []

	coord_file = open(path, "r", encoding='latin-1')
	coord_buffer = coord_file.readlines()

	zero_coords = search('{:f}, {:f}, {:f}', coord_buffer[0])
	x = float(zero_coords[0])
	y = float(zero_coords[1])
	z = float(zero_coords[2])
	
	for i in range(len(coord_buffer)):
		coords = search('{:f}, {:f}, {:f}', coord_buffer[i])
		output_buffer.append(
					"{:10.6f}".format(coords[0] - x) + ", " 
					"{:10.6f}".format(coords[1] - y) + ", " 
					"{:10.6f}".format(coords[2] - z) + "\n")

	coord_file.close()

	output_file = open(path, "w", encoding='latin-1')
	output_file.writelines(output_buffer)
	output_file.close()

else:
	print('argument not found') 
