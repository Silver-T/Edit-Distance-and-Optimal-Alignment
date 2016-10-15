# -*- coding: utf-8 -*-
"""
Created: 12/10/16
Author: Anthony Silvestre
Purpose: 
"""
import numpy as np
'''
def opt_alignment(seq1, seq2, sub_mat):
'''    

def edit_distance(seq1, seq2):
    '''
    Computes the edit distance betweeen the two input sequences iteratively
    '''
    edit = [x[:] for x in [[0]*(len(seq2)+1)]*(len(seq1)+1)]
    edit_type = [x[:] for x in [[0]*(len(seq2)+1)]*(len(seq1)+1)]
    edit_path = [x[:] for x in [[0]*(len(seq2)+1)]*(len(seq1)+1)]
    print()
    # sequence 1 is along the x axis
    # sequence 2 is along the y axis
  
    #edit = np.array(edit)    
    edit[0][0] = 0
    edit_type[0][0] = 'M'
    edit_path[0][0] = '-'

    for i in range(1, len(seq1)+1):
        edit[i][0]= edit[i-1][0] + g_e
        edit_type[i][0] = 'I'
        edit_path[i][0] = 'l'
    
    for j in range(1, len(seq2)+1):
        edit[0][j]= edit[0][j-1] + g_e
        edit_type[0][j] = 'D'
        edit_path[0][j] = 'u'
        
    for i in range(1, len(seq1)+1):       # iterates over the rows of edit
        for j in range(1, len(seq2)+1):   # iterates over the columns of edit
            if seq1[i-1] == seq2[j-1]:
                edit[i][j] = edit[i - 1][j - 1]
                edit_type[i][j] = 'M'
                edit_path[i][j] = 'u_l'
                # If the two letters are a match, the edit cost is zero
            else:
                # Find min surrounding value
                # Find type of that value
                # enter that function
                min_val = min(edit[i-1][j-1], edit[i-1][j], edit[i][j-1])                
                if edit[i-1][j-1] == min_val:
                    # Match/Substition
                    cost = Match_cost(seq1[i-1], seq2[j-1], edit_type[i-1][j-1])
                    edit[i][j] = edit[i-1][j-1] + cost
                    edit_type[i][j] = 'M'
                    edit_path[i][j] = 'u_l'
                elif edit[i-1][j] == min_val:
                    # Insertion
                    cost = Insert_cost(seq1[i-1], seq2[j-1], edit_type[i-1][j])
                    edit[i][j] = edit[i-1][j] + cost
                    edit_type[i][j] = 'I'
                    edit_path[i][j] = 'l'
                elif edit[i][j-1] == min_val:
                    # Deletion
                    cost = Delete_cost(seq1[i-1], seq2[j-1], edit_type[i][j-1])
                    edit[i][j] = edit[i][j-1] + cost
                    edit_type[i][j] = 'D'
                    edit_path[i][j] = 'u'
               
    print(np.array(edit))    
    return edit[len(seq1)-1][len(seq2)-1]
   
def Match_cost(letter1, letter2, prev_type):
    row = sub_dict[letter1]+1
    col = sub_dict[letter2]+1
    
    if prev_type == 'M':
        return int(submat[row][col])
    elif prev_type == 'D' or prev_type == 'I':
        return g_0

def Delete_cost(letter1, letter2, prev_type):
    row = sub_dict[letter1]+1
    col = sub_dict[letter2]+1
    
    if prev_type == 'M':
        return int(submat[row][col])
    elif prev_type == 'D':
        return g_e
    elif prev_type == 'I':
        return g_0

def Insert_cost(letter1, letter2, prev_type):
    row = sub_dict[letter1]+1 
    col = sub_dict[letter2]+1
    
    if prev_type == 'M':
        return int(submat[row][col])
    elif prev_type == 'D':
        return g_0
    elif prev_type == 'I':
        return g_e  
    
    
'''
a = open('seq1', 'r')
a_seq = a.read()
a.close()
b = open('seq2', 'r')
b_seq = b.read()
b.close()
print(a_seq)
print(b_seq)
'''
f = open('submat', 'r')
submat = [line.split() for line in f]
f.close()

# Constructs a dictionary to easily find the index of a letter
sub_dict = {}
count = 0
for letter in submat[0]:
    sub_dict[letter] = count
    count += 1

# define global variable: g_0, gap opening penalty
g_0 = 10                    # so it's not favourable

# define global variable: g_e, gap extension penalty
g_e = 5                     # more favourable then opening a new gap

'''
edit_distance(b_seq, a_seq)
'''
edit_distance('ATA', 'AGTA')