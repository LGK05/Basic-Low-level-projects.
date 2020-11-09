
import random

not_required = [4,9,14,19,24]
done_list = ['  ','  ','  ','  ','  ']

def random_generator():
    lisa_of_numbers = []
    for i in range(1,26):
        lisa_of_numbers.append(i)
    random.shuffle(lisa_of_numbers)
    return lisa_of_numbers

human_nums = random_generator()
bot_nums = random_generator()
no_of_guesses = 0


def stadium_set_up(nums):
    
    print(nums[0],   '    |    ',nums[1], '    |    ',nums[2], '    |    ',nums[3], '    |    ',nums[4], '    |    ')
    print('\n')
    print(nums[5],   '    |    ',nums[6], '    |    ',nums[7], '    |    ',nums[8], '    |    ',nums[9], '    |    ')
    print('\n')
    print(nums[10],  '    |    ',nums[11],'    |    ',nums[12],'    |    ',nums[13],'    |    ',nums[14],'    |    ')
    print('\n')
    print(nums[15],  '    |    ',nums[16],'    |    ',nums[17],'    |    ',nums[18],'    |    ',nums[19],'    |    ')
    print('\n')
    print(nums[20],  '    |    ',nums[21],'    |    ',nums[22],'    |    ',nums[23],'    |    ',nums[24],'    |    ')


done_list = ['  ','  ','  ','  ','  ']
def bot_intel():
	human_row1 = [str(human_nums[0]),str(human_nums[1]),str(human_nums[2]),str(human_nums[3]),str(human_nums[4])]
	human_row2 = [str(human_nums[5]),str(human_nums[6]),str(human_nums[7]),str(human_nums[8]),str(human_nums[9])]
	human_row3 = [str(human_nums[10]),str(human_nums[11]),str(human_nums[12]),str(human_nums[13]),str(human_nums[14])]
	human_row4 = [str(human_nums[15]),str(human_nums[16]),str(human_nums[17]),str(human_nums[18]),str(human_nums[20])]
	human_row5 = [str(human_nums[20]),str(human_nums[21]),str(human_nums[22]),str(human_nums[23]),str(human_nums[24])]

	human_col1 = [str(human_nums[0]),str(human_nums[5]),str(human_nums[10]),str(human_nums[15]),str(human_nums[20])]
	human_col2 = [str(human_nums[1]),str(human_nums[6]),str(human_nums[11]),str(human_nums[16]),str(human_nums[21])]
	human_col3 = [str(human_nums[2]),str(human_nums[7]),str(human_nums[12]),str(human_nums[17]),str(human_nums[22])]
	human_col4 = [str(human_nums[3]),str(human_nums[8]),str(human_nums[13]),str(human_nums[18]),str(human_nums[23])]
	human_col5 = [str(human_nums[4]),str(human_nums[9]),str(human_nums[14]),str(human_nums[19]),str(human_nums[24])]
    
	human_diagonal_1 = [str(human_nums[0]),str(human_nums[6]),str(human_nums[12]),str(human_nums[18]),str(human_nums[24])]
	human_diagonal_2 = [str(human_nums[4]),str(human_nums[8]),str(human_nums[12]),str(human_nums[16]),str(human_nums[20])]

	bot_row1 = [str(bot_nums[0]),str(bot_nums[1]),str(bot_nums[2]),str(bot_nums[3]),str(bot_nums[4])]
	bot_row2 = [str(bot_nums[5]),str(bot_nums[6]),str(bot_nums[7]),str(bot_nums[8]),str(bot_nums[9])]
	bot_row3 = [str(bot_nums[10]),str(bot_nums[11]),str(bot_nums[12]),str(bot_nums[13]),str(bot_nums[14])]
	bot_row4 = [str(bot_nums[15]),str(bot_nums[16]),str(bot_nums[17]),str(bot_nums[18]),str(bot_nums[20])]
	bot_row5 = [str(bot_nums[20]),str(bot_nums[21]),str(bot_nums[22]),str(bot_nums[23]),str(bot_nums[24])]

	bot_col1 = [str(bot_nums[0]),str(bot_nums[5]),str(bot_nums[10]),str(bot_nums[15]),str(bot_nums[20])]
	bot_col2 = [str(bot_nums[1]),str(bot_nums[6]),str(bot_nums[11]),str(bot_nums[16]),str(bot_nums[21])]
	bot_col3 = [str(bot_nums[2]),str(bot_nums[7]),str(bot_nums[12]),str(bot_nums[17]),str(bot_nums[22])]
	bot_col4 = [str(bot_nums[3]),str(bot_nums[8]),str(bot_nums[13]),str(bot_nums[18]),str(bot_nums[23])]
	bot_col5 = [str(bot_nums[4]),str(bot_nums[9]),str(bot_nums[14]),str(bot_nums[19]),str(bot_nums[24])]
	  
	bot_diagonal_1 = [str(bot_nums[0]),str(bot_nums[6]),str(bot_nums[12]),str(bot_nums[18]),str(bot_nums[24])]
	bot_diagonal_2 = [str(bot_nums[4]),str(bot_nums[8]),str(bot_nums[12]),str(bot_nums[16]),str(bot_nums[20])]
	
	list_of_nums = [bot_row1,bot_row2,bot_row3,bot_row4,bot_row5,bot_col1,bot_col2,bot_col3,bot_col4,bot_col5,bot_diagonal_1,bot_diagonal_2]
	sorting = [x.sort() for x in list_of_nums]
	list_of_nums.sort()
	list_of_nums = [bot_row1,bot_row2,bot_row3,bot_row4,bot_row5,bot_col1,bot_col2,bot_col3,bot_col4,bot_col5,bot_diagonal_1,bot_diagonal_2]
	sorting = [x.sort() for x in list_of_nums]
	n = 0
	while True:
		if list_of_nums[n] == done_list:
			n += 1
			continue
		else:
			useful_i = list_of_nums[n]
			break
	useful_i.sort()
	return useful_i[-1]    

def wincheck():
	human_row1 = [str(human_nums[0]),str(human_nums[1]),str(human_nums[2]),str(human_nums[3]),str(human_nums[4])]
	human_row2 = [str(human_nums[5]),str(human_nums[6]),str(human_nums[7]),str(human_nums[8]),str(human_nums[9])]
	human_row3 = [str(human_nums[10]),str(human_nums[11]),str(human_nums[12]),str(human_nums[13]),str(human_nums[14])]
	human_row4 = [str(human_nums[15]),str(human_nums[16]),str(human_nums[17]),str(human_nums[18]),str(human_nums[20])]
	human_row5 = [str(human_nums[20]),str(human_nums[21]),str(human_nums[22]),str(human_nums[23]),str(human_nums[24])]

	human_col1 = [str(human_nums[0]),str(human_nums[5]),str(human_nums[10]),str(human_nums[15]),str(human_nums[20])]
	human_col2 = [str(human_nums[1]),str(human_nums[6]),str(human_nums[11]),str(human_nums[16]),str(human_nums[21])]
	human_col3 = [str(human_nums[2]),str(human_nums[7]),str(human_nums[12]),str(human_nums[17]),str(human_nums[22])]
	human_col4 = [str(human_nums[3]),str(human_nums[8]),str(human_nums[13]),str(human_nums[18]),str(human_nums[23])]
	human_col5 = [str(human_nums[4]),str(human_nums[9]),str(human_nums[14]),str(human_nums[19]),str(human_nums[24])]
    
	human_diagonal_1 = [str(human_nums[0]),str(human_nums[6]),str(human_nums[12]),str(human_nums[18]),str(human_nums[24])]
	human_diagonal_2 = [str(human_nums[4]),str(human_nums[8]),str(human_nums[12]),str(human_nums[16]),str(human_nums[20])]

	bot_row1 = [str(bot_nums[0]),str(bot_nums[1]),str(bot_nums[2]),str(bot_nums[3]),str(bot_nums[4])]
	bot_row2 = [str(bot_nums[5]),str(bot_nums[6]),str(bot_nums[7]),str(bot_nums[8]),str(bot_nums[9])]
	bot_row3 = [str(bot_nums[10]),str(bot_nums[11]),str(bot_nums[12]),str(bot_nums[13]),str(bot_nums[14])]
	bot_row4 = [str(bot_nums[15]),str(bot_nums[16]),str(bot_nums[17]),str(bot_nums[18]),str(bot_nums[20])]
	bot_row5 = [str(bot_nums[20]),str(bot_nums[21]),str(bot_nums[22]),str(bot_nums[23]),str(bot_nums[24])]

	bot_col1 = [str(bot_nums[0]),str(bot_nums[5]),str(bot_nums[10]),str(bot_nums[15]),str(bot_nums[20])]
	bot_col2 = [str(bot_nums[1]),str(bot_nums[6]),str(bot_nums[11]),str(bot_nums[16]),str(bot_nums[21])]
	bot_col3 = [str(bot_nums[2]),str(bot_nums[7]),str(bot_nums[12]),str(bot_nums[17]),str(bot_nums[22])]
	bot_col4 = [str(bot_nums[3]),str(bot_nums[8]),str(bot_nums[13]),str(bot_nums[18]),str(bot_nums[23])]
	bot_col5 = [str(bot_nums[4]),str(bot_nums[9]),str(bot_nums[14]),str(bot_nums[19]),str(bot_nums[24])]
	  
	bot_diagonal_1 = [str(bot_nums[0]),str(bot_nums[6]),str(bot_nums[12]),str(bot_nums[18]),str(bot_nums[24])]
	bot_diagonal_2 = [str(bot_nums[4]),str(bot_nums[8]),str(bot_nums[12]),str(bot_nums[16]),str(bot_nums[20])]

	list_of_human_nums = [human_row1,human_row2,human_row3,human_row4,human_row5,human_col1,human_col2,human_col3,human_col4,human_col5,human_diagonal_1,human_diagonal_2]
	list_of_bot_nums = [bot_row1,bot_row2,bot_row3,bot_row4,bot_row5,bot_col1,bot_col2,bot_col3,bot_col4,bot_col5,bot_diagonal_1,bot_diagonal_2]
	sorting = [x.sort() for x in list_of_bot_nums]
	list_of_human_nums.sort()
	list_of_bot_nums.sort()
   
	if list_of_human_nums[0] == list_of_human_nums[1] == list_of_human_nums[2] == list_of_human_nums[3] == list_of_human_nums[4]:
		return 'h'
	elif list_of_bot_nums[0] == list_of_bot_nums[1] == list_of_bot_nums[2] == list_of_bot_nums[3] == list_of_bot_nums[4]:
		return 'b'
	else:
		pass
print('Welcome to BINGO. ""Developed By- Shogun""')

already_done = []
while True:
    print('\n'*100)
    stadium_set_up(human_nums)
    print('Its your turn now.')
    print('You cant choose these: ', already_done)
    human_number = int(input('Enter which number you want to cross out: '))
    if human_number in already_done:
    	continue
    else:
    	already_done.append(human_number)
    human_index = human_nums.index(human_number)
    human_nums[human_index] = '  '
    if wincheck() == 'h' :
    	print('Congrats you have won the match')
    	print('Your Stadium: \n')
    	stadium_set_up(human_nums)
    	print('Computers stadium: \n')
    	stadium_set_up(bot_nums)
    	break
    bot_index = bot_nums.index(human_number)
    bot_nums[bot_index] = '  '
    if wincheck() == 'b':
    	print('Sorry the computer has won')
    	print('Your Stadium: \n')
    	stadium_set_up(human_nums)
    	print('Computers stadium: \n')
    	stadium_set_up(bot_nums)
    	break   
    bot_selected_num = bot_intel()
    print(bot_selected_num)
    bot_index1 = bot_nums.index(int(bot_selected_num))   
    bot_nums[bot_index1] = '  '
    already_done.append(bot_selected_num)
    if wincheck() == 'b':
    	print('Sorry the bot has won')
    	print('Your Stadium: \n')
    	stadium_set_up(human_nums)
    	print('Computers stadium: \n')
    	stadium_set_up(bot_nums)
    	break
    human_index1 = human_nums.index(int(bot_selected_num))
    human_nums[human_index1] = '  '
    if wincheck() == 'h':
    	print('Congrats you have won')
    	print('Your Stadium: \n')
    	stadium_set_up(human_nums)
    	print('Computers stadium: \n')
    	stadium_set_up(bot_nums)
    	break
