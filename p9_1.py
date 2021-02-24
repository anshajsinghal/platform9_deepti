import re


grid  =    [ [ 'A',    'F',    'H',     'D',     'T',      'K',     'P',     'E',      'P',     'G'  ],
             [ 'J',    'G',    'R',     'E',     'E',      'N',     'T',     'P',      'W',     'R'  ], 
             [ 'U',    'R',    'G',     'E',     'P',      'Q',     'Y',     'K',      'W',     'E'  ],
             [ 'P',    'E',    'R',     'A',     'C',      'R',     'T',     'P',      'W',     'E'  ],
             [ 'U',    'E',    'F',     'J',     'T',      'U',     'W',     'P',      'Q',     'N'  ],
             [ 'P',    'N',    'U',     'S',     'N',      'W',     'A',      'Z',      'X',     'V'  ] ]
             
input_word = "GREEN"  # example, could be any word

# option 1 - look for the word vertically
# expected output - [(0,9), (1,1)]

# option 2 - look vertically and horizonrally
# expected output - [(0,9), (1,1), (1,1)]

def find_word(grid, word):
	word_indexes = []
	l_word = list(word)
	for i in grid:
		positions = []
		st = join_horizontal(i)
		if word in st:
			matches = re.finditer(word, st)
			positions = [match.start() for match in matches]
			for position in positions:
				word_indexes.append((grid.index(i), position))

	for i in range (0, len(grid[0])):
		st = join_vertical(grid, i)
		if word in st:
			matches = re.finditer(word, st)
			positions = [match.start() for match in matches]
			for position in positions:
				word_indexes.append((position, i))

	print(word_indexes)

def join_horizontal(inp_list):
	st = ""
	st = st.join(inp_list)
	return st

def join_vertical(grid, index):
	h_letters = []
	st = ""
	for i in grid:
		h_letters.append(i[index])

	st = st.join(h_letters)
	return st



find_word(grid, "GREEN")