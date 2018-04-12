# Character Picture Grid is a practical project from Chapter 4 - Lists.
# It takes a user defined picture grid of a heart and flip 90 degrees clockwise.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Two for loops are used to loop through each list within the grid list.
for i in range(len(grid[0])): # First loop loops through list in grid list.
    for j in range(len(grid)): # Second loop loops through list in grid.
        print(grid[j][i], end = '') # Print each element in grid[j][i].
    print()

# Comments:
# - Had trouble flipping image 90 degrees so had to look up the solution online.
# - Below is the code I used.
##for i in range(len(grid)):
##    lst = grid[i]
##    for j in range(len(lst)):
##        print(lst[j], end= '')
##    print('')
