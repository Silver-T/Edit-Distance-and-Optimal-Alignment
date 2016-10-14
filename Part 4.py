# -*- coding: utf-8 -*-
"""
Created: 12/10/16
Author: Anthony Silvestre
Purpose: 
"""

'''
def opt_alignment(seq1, seq2, sub_mat):
'''    

def edit_distance(seq1, seq2):
    '''
    Computes the edit distance betweeen the two input sequences iteratively
    '''
    #edit = [x[:] for x in [[0]*(len(seq2))]*(len(seq1))]
    edit = [[[[['-'] for i in range(0,5)] for i in range(3)] for i in range(0,len(seq2))] for i in range (0, len(seq1))]
    # sequence 1 is along the x axis
    # sequence 2 is along the y axis
    edit = np.array(edit)    
    edit[0][0][0][0] = 0
    edit[0][0][0][1] = 'M'
    edit[0][0][0][2] = '-'
    edit[0][0][0][3] = '-'
    edit[0][0][0][4] = '-'

    for i in range(1, len(seq1)):
        edit[i][0][0][0] = i                    # current value
        edit[i][0][0][1] = 'I'                  # current type    
        edit[i][0][0][2] = edit[i-1][0][0][1]   # previous type
        edit[i][0][0][3] = i-1                  # previous x coord
        edit[i][0][0][4] = 0                    # previous y coord
    
    for j in range(1, len(seq2)):
        edit[0][j][0][0] = j
        edit[0][j][0][1] = 'I'
        edit[0][j][0][2] = edit[0][j-1][0][1]
        edit[0][j][0][3] = 0
        edit[0][j][0][4] = j-1

    for i in range(0, len(seq1)):
        print(edit[i][0][0][0])
    '''
    for i in range(1, len(seq1)):   # iterates over the rows of edit
        for j in range(1, len(seq2)):   # iterates over the columns of edit
            if seq1[i-1] == seq2[j-1]:
                edit[i][j] = edit[i - 1][j - 1]         
                # If the two letters are a match, the edit cost is zero
            else:
                edit[i][j] = min(edit[i - 1][j - 1]+1, (edit[i - 1][j]) + 1, (edit[i][j - 1]) + 1)
                # need to find min of insert, delete or sub equation
    return edit[len(seq1)-1][len(seq2)-1]
    '''
    
import numpy as np

a = open('seq1', 'r')
a_seq = a.read()
a.close()
b = open('seq2', 'r')
b_seq = b.read()
b.close()
print(a_seq)
print(b_seq)

print(edit_distance(a_seq, b_seq))