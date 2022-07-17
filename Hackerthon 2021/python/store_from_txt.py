import os
def space_to_underscr(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = str(lst[i][j]).replace("_"," ")
    return lst  

def txt_categories(txt_file):
    final_data = []
    carry_data = []
    i = 0 
    with open(txt_file) as f:
        txt_data = f.read().strip().split()
    #os.remove(txt_file)
    for i in txt_data: 
        if i == '#':
            carry_data = sorted(carry_data)
            final_data.append(carry_data)
            carry_data = []
        else:
            carry_data.append(i)
    space_to_underscr(final_data)
    return final_data
