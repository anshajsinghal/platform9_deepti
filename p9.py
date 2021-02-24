import copy

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

# deepti@platform9.com




def find_word(grid, word):
	word_indexes = []
	org_grid = copy.deepcopy(grid)
	l_word = list(word)
	l_word_org = copy.deepcopy(l_word)
	for i in org_grid:		
		indexes = get_letter(i, l_word[0])
		for ind in indexes:
			result = get_indexes_letter_vert(grid, l_word, ind)
			if result:
				word_indexes.append((org_grid.index(i), ind))
			l_word = copy.deepcopy(l_word_org)
			result1 = get_indexes_letter_horz(i, l_word, ind)
			if result1:
				word_indexes.append((org_grid.index(i), ind))
		grid.pop(0)
		
	print(word_indexes)

def get_indexes_letter_horz(h_list_orig, l_word_orig, ind):
	h_list = copy.deepcopy(h_list_orig)
	l_word = copy.deepcopy(l_word_orig)

	if len(h_list)-ind >= len(l_word):
		if h_list[ind] == l_word[0]:
			h_list.pop(ind)
			l_word.pop(0)
			if len(l_word) == 0:
				return True
			elif len(h_list) == 0:
				return False
			else:
				return(get_indexes_letter_horz(h_list, l_word, ind))
		else:
			return False



def get_indexes_letter_vert(grid_orig, l_word_orig, index):
	grid = copy.deepcopy(grid_orig)
	l_word = copy.deepcopy(l_word_orig)
	if grid[0][index] == l_word[0]:
		grid.pop(0)
		l_word.pop(0)
		if len(l_word) == 0:
			return True
		elif len(grid) == 0:
			return False
		else:
			return get_indexes_letter_vert(grid, l_word, index)
	else:
		return False



def get_letter(inp_list, letter):
	indexes = [index for index, value in enumerate(inp_list) if value == letter]
	return indexes



find_word(grid, "GREEN")
