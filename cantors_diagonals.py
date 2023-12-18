# Given a list of lists containing only 1s and 0s, return a new list that differs from list 1 in its first element, list 2 in its second element, list 3 in its 3rd element, and so on.

# cantor([[0,0,0],
#         [1,1,1],
#         [0,1,0]]) = [1,0,1]

# cantor([[1,0,0],
#         [0,1,0],
#         [0,0,1]]) = [0,0,0]
        
# The nested list will always be perfectly square. Your solution should be a list containing only 1s and 0s.

#My solution:

def cantor(nested_list):
    i = 0
    changed_numbers = []
    while i < len(nested_list):
        if nested_list[i][i]:
            nested_list[i][i] = 0
        else:
            nested_list[i][i] = 1
        changed_numbers.append(nested_list[i][i])
        i += 1
    return changed_numbers

#Best voted solution, which I changed the function name for diferentiating of mine:

def cantor2(nested_list):
    return [not(line[i]) for i, line in enumerate(nested_list)]