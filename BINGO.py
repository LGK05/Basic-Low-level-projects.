import tkinter as tk
import tkinter.font as font
import random

root = tk.Tk()
root.title("Bingo")

def num_creator():
    nums = {}
    numsls = []
    for i in range(1,26):
        i = str(i)
        if len(i)==1:
            i = list(i)
            i.insert(0,"0")
            i = "".join(i)
        numsls.append(i)
    random.shuffle(numsls)
    for i in numsls:
        nums[i]=1
    return nums

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

human_nums_alt = num_creator()
bot_nums_alt = num_creator()
human_nums= list(human_nums_alt)
bot_nums = list(bot_nums_alt)
row_ = 0
col_ = 0

buttons = []
for i in tuple(human_nums_alt):
    x=tk.Button(text=f"{str(i)}", padx = 30, pady = 30,command= lambda i=i,row_=row_,col_=col_:brains(i,row_,col_))
    x['font']=font.Font(size=24)
    x.grid(row= row_, column=col_)
    buttons.append(x)
    col_ += 1
    if col_%5==0:
        row_ +=1
        col_ = 0

def brains(kill,row_,col_):

    global human_nums_alt, bot_nums_alt, buttons

    human_nums[human_nums.index(kill)]="  "
    bot_nums[bot_nums.index(kill)]="  "
    
    buttons[(row_)*5+(col_)].config(state="disabled",text=f"{kill}", bg= "red")
    done_list = ['  ','  ','  ','  ','  ']

    def wincheck(list_of_human_nums, list_of_bot_nums):
        if list_of_human_nums[0] == list_of_human_nums[1] == list_of_human_nums[2] == list_of_human_nums[3] == list_of_human_nums[4]:
            return 'h'
        elif list_of_bot_nums[0] == list_of_bot_nums[1] == list_of_bot_nums[2] == list_of_bot_nums[3] == list_of_bot_nums[4]:
            return 'b'
        else:
            pass

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

    human_nums_alt_alt = [human_row1,human_row2,human_row3,human_row4,human_row5,human_col1,human_col2,human_col3,human_col4,human_col5,human_diagonal_1,human_diagonal_2]
    list_of_nums = [bot_row1,bot_row2,bot_row3,bot_row4,bot_row5,bot_col1,bot_col2,bot_col3,bot_col4,bot_col5,bot_diagonal_1,bot_diagonal_2]

    sorting = [x.sort() for x in list_of_nums]
    sorting= [x.sort() for x in human_nums_alt_alt]
    human_nums_alt_alt.sort()
    list_of_nums.sort()
    winner = wincheck(human_nums_alt_alt, list_of_nums)

    n = 0
    while True:
        if list_of_nums[n] == done_list:
            n+= 1
            continue
        else:
            useful_i = list_of_nums[n]
            break

    useful_i.sort()

    buttons[human_nums.index(f"{useful_i[-1]}")].config(text=f"{useful_i[-1]}", state="disabled", bg = "red")
    
    human_nums[human_nums.index(useful_i[-1])] = "  "
    bot_nums[bot_nums.index(useful_i[-1])] = "  "

    if winner == 'h' or winner == 'b':
        if winner == 'h':
            print("Hooman you take the victory this time\n")
        if winner == 'b':
            print("You have have fallen to the AI you weak hooman\n")
        print("The bot's stadium-\n")
        stadium_set_up(bot_nums)
        root.destroy()
    else:
        if wincheck(human_nums_alt_alt,list_of_nums) == 'h':
            print("Hooman you take the victory this time\n")
            print("The bot's stadium-\n")
            stadium_set_up(bot_nums)
            root.destroy()
        elif wincheck(human_nums_alt_alt,list_of_nums)== 'b':
            print("You have have fallen to the AI you weak hooman\n")
            print("The bot's stadium-\n")
            stadium_set_up(bot_nums)
            root.destroy()

tk.mainloop()
