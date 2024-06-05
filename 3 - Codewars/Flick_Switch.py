def flick_switch(lst):
	res = []
	state = True
	for i in lst:
		if i == 'flick':
			state = not state
		res.append(state)
	print(res)
	return res




lst = ['codewars', 'flick', 'code', 'wars']

flick_switch(lst)



