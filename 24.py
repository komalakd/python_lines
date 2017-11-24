size = 8

height = size + 1

def get_line_str(size,line_type):
	line_str = ''
	for j in range(size):
		if line_type == 'h':
			line_str += ' ---'
		else:
			line_str += '|   '

	return line_str

line_h = get_line_str(size,'h')
line_v = get_line_str(size+1,'v')

for i in range(size):
	print line_h
	print line_v

print line_h
