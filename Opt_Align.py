"""
Created:    12/10/16
Modified:   16/10/16
Author:     Anthony Silvestre
Purpose:    To find the optimal alignment and optimal alignment score of two strings
Input:      Two strings (to be aligned), a substitution matrix, gap opening penalty
            and gap closing penalty
Output:     The optimal alignment and alignment score of the two strings
"""
import sys

def opt_alignment(seq1, seq2):
    '''
    Computes the optimal alignment and optimal alignment score of two sequences
    '''
    
    edit = [x[:] for x in [[0]*(len(seq2)+1)]*(len(seq1)+1)]
    edit_type = [x[:] for x in [[0]*(len(seq2)+1)]*(len(seq1)+1)]
    #edit stores the alignment scores and edit_type stores the transition types    
    # sequence 1 is along the y axis
    # sequence 2 is along the x axis
    
    # Sets the initial value corresponding to an empty-emtpy match
    edit[0][0] = 0                  
    edit_type[0][0] = 'M'
    
    # Sets the initial M to I transition at edit[0][1]
    edit[0][1] = edit[0][0] + g_0   
    edit_type[0][1] = 'I'
    
    # Sets the initial M to D transition at edit[1][0]
    edit[1][0] = edit[0][0] + g_0   
    edit_type[1][0] = 'D'
    
    # Sets the first row of I to I transitions
    for j in range(2, len(seq2)+1):
        edit[0][j]= edit[0][j-1] + g_e
        edit_type[0][j] = 'I'
    
    # Sets the first column of D to D transitions
    for i in range(2, len(seq1)+1):
        edit[i][0]= edit[i-1][0] + g_e
        edit_type[i][0] = 'D'
        
    for i in range(1, len(seq1)+1):         # iterates over the rows of edit
        for j in range(1, len(seq2)+1):     # iterates over the columns of edit
            if seq1[i-1] == seq2[j-1]:      # If the two letters are a match
                cost = Match_cost(seq1[i-1], seq2[j-1], edit_type[i-1][j-1])                
                edit[i][j] = edit[i - 1][j - 1] + cost
                edit_type[i][j] = 'M'
                
            else:
                # Find the min surrounding value
                # Find the type of that value
                # Enter one of the cost functions
                min_val = min(edit[i-1][j-1], edit[i-1][j], edit[i][j-1])                
                if edit[i-1][j-1] == min_val:
                    # Match/Substition
                    cost = Match_cost(seq1[i-1], seq2[j-1], edit_type[i-1][j-1])
                    edit[i][j] = edit[i-1][j-1] + cost
                    edit_type[i][j] = 'M'
                elif edit[i-1][j] == min_val:
                    # Deletion
                    cost = Delete_cost(seq1[i-1], seq2[j-1], edit_type[i-1][j])
                    edit[i][j] = edit[i-1][j] + cost
                    edit_type[i][j] = 'D'
                elif edit[i][j-1] == min_val:
                    # Insertion
                    cost = Insert_cost(seq1[i-1], seq2[j-1], edit_type[i][j-1])
                    edit[i][j] = edit[i][j-1] + cost
                    edit_type[i][j] = 'I'
    
    # returns the optimal alignment and optimal alignment score
    return [backtrack(seq1, seq2, edit_type), edit[len(seq1)-1][len(seq2)-1]]
   
def Match_cost(letter1, letter2, prev_type):
    # Computes the additional cost when the alignment is a match 
    row = sub_dict[letter1]+1
    col = sub_dict[letter2]+1
    
    if prev_type == 'M':
        return int(submat[row][col])
    elif prev_type == 'D' or prev_type == 'I':
        return g_0

def Delete_cost(letter1, letter2, prev_type):
    # Computes the additional cost when the alignment is a deletion
    row = sub_dict[letter1]+1
    col = sub_dict[letter2]+1
    
    if prev_type == 'M':
        return int(submat[row][col])
    elif prev_type == 'D':
        return g_e
    elif prev_type == 'I':
        return g_0

def Insert_cost(letter1, letter2, prev_type):
    # Computes the additional cost when the alignment is an insertion
    row = sub_dict[letter1]+1 
    col = sub_dict[letter2]+1
    
    if prev_type == 'M':
        return int(submat[row][col])
    elif prev_type == 'D':
        return g_0
    elif prev_type == 'I':
        return g_e  

def backtrack(old_seq1, old_seq2, edit_type):
    new_seq1 = ''
    new_seq2 = ''
    
    i = len(old_seq1)-1
    j = len(old_seq2)-1
    
    # Backtracks from an optimal score and constructs an alignment 
    while i > -1 and j > -1:    # Stop when the start of the string is reached
        if edit_type[i][j] == 'M':
            new_seq1 += old_seq1[i]
            new_seq2 += old_seq2[j]
            i -= 1
            j -= 1
        elif edit_type[i][j] == 'I':
            new_seq1 += '-'
            new_seq2 += old_seq2[j]
            j -= 1
        elif edit_type[i][j] == 'D': 
            new_seq1 += old_seq1[i]
            new_seq2 += '-'
            i -= 1
    # reverses the alignment as it was constructed in reverse
    new_seq1 = new_seq1[::-1]
    new_seq2 = new_seq2[::-1]
    
    return [new_seq2, new_seq1]
    
    
a = open(sys.argv[1], 'r')
a_seq = a.read().rstrip()
a.close()
b = open(sys.argv[2], 'r')
b_seq = b.read().rstrip()
b.close()

f = open(sys.argv[3], 'r')
submat = [line.split() for line in f]
f.close()

# Constructs a dictionary to easily find the index of a letter
sub_dict = {}
count = 0
for letter in submat[0]:
    sub_dict[letter] = count
    count += 1

# define g_0, gap opening penalty
g_0 = int(sys.argv[4])
# define g_e, gap extension penalty
g_e = int(sys.argv[5])

[[align_str1, align_str2], align_score] = opt_alignment(b_seq, a_seq)
print('String 1: ', a_seq)
print('String 2: ', b_seq)
print()
print('Aligned string 1: ', align_str1)
print('Aligned string 2: ', align_str2)
print('Alignment score: ', align_score)