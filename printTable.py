# Practical project from Chapter 6 - Manipulating Strings.
# The code takes in a list of lists of strings and displays it in a table in
# right-justified position.

# Column right-justified three lists.
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Function takes in a big list, compares the length of each list in big list
# and stores the biggest value. The value is used to r.just words in each list.
def printTable(table):
    # Set up empty list to store length of longest word.
    colWidths = [0] * len(table)
    # For loops used to loop through each word in each list in big list to compare length.
    # Biggest value for each list is stored in colWidths.
    for i in range(len(table)):
        longest = 0
        for j in range(len(table[i])):
            if len(table[i][j]) > longest:
                longest = len(table[i][j])
                colWidths[i] = longest
    print(colWidths)

    # For loop used to "transpose" list in tableData into columns.
    # Similar to picture grid practical project in Chapter 4.
    for i in range(len(table[0])):
        for j in range(len(table)):
            lst = (table[j][i]).rjust(colWidths[j])
            print(lst, end = ' ')
        print('')
        
printTable(tableData)

# Comment:
# - Code will run if each list in list is the same length. This means empty spaces
#   in list must be replaced with ''.
# - Started with one list to test out r.just as shown below.

##list = ['apples', 'oranges', 'cherries', 'banana']
##
##def printTable(table):
##    longest = 0
##    for i in table: 
##        if len(i) > longest:
##            longest = len(i)
##    for i in table:
##        print(i.rjust(longest))
##        
##    
##printTable(list)
