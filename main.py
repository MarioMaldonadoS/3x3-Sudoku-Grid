# Mario M.
# 3x3 A,B,C grid solver

def main():
    n = str(input())
    ni = n.replace(',', '')
    ns = ni.replace(' ', '')
    nn = ['','','','','','','','',''] # our grid-list
    ln = list(ns)

    # initialize the grid
    pointer = 1
    for i in range(int(ln[0])): # range is first number of the input
        p = int(ln[pointer]) # get the position 'number'
        nn[p-1] = ln[pointer+1] # set the letter in the correct position
        pointer+=2

    # fill in the grid
    nn = fillGrid(nn,0)
    print(''.join(nn))

# steps to solve the 3x3 'Sudoku'
# 1. pick an empty position '' (start from left to right)
# 2. try A or B or C
# 3. find the letter that works (does not break the rules)
# 4. repeat
# 5. backtrack if no chosen letter works
#
# fillGrid takes in the grid-list and the start position (0-8)
# returns a list with a new letter inserted
def fillGrid(nn,start):
    # not at the end of the grid yet
    if start < 9:
        # 1. find an empty position ''
        if nn[start] == '':
            set = ['A', 'B', 'C']
            # 2. try A or B or C
            for s in set:
                nn[start] = s
                # 3. find the letter that works
                if test(nn,start):
                    # 4. repeat
                    newnn = fillGrid(nn, start+1)  # fill the grid starting at the next position
                    # if the filled in grid works, return the grid-list
                    if newnn:
                        return newnn
            # 5. backtrack if no chosen letter works
            nn[start] = ''
            return None
        else:
            return fillGrid(nn,start+1) # go to the next position
    # reached the end of the grid
    else:
        return nn

# test takes the grid-list and the starting position
# returns True if no rules are broken, False otherwise
def test(nn,start):
    if rowCheck(nn,start) and colCheck(nn, start):
        return True
    return False

# rowCheck takes the grid-list and the starting position
# returns True if the new letter only appears once in its row, false otherwise
def rowCheck(nn,start):
    if start == 0 or start == 3 or start == 6:
        if nn[start] != nn[start+1] and nn[start] != nn[start+2]:
                return True
        return False
    elif start == 1 or start == 4 or start == 7:
        if nn[start] != nn[start-1] and nn[start] != nn[start+1]:
                return True
        return False
    else:
        if nn[start] != nn[start-2] and nn[start] != nn[start-1]:
                return True
        return False

# colCheck takes the grid-list and the starting position
# returns True if the new letter only appears once in its column, false otherwise
def colCheck(nn,start):
    if start == 0 or start == 1 or start == 2:
        if nn[start] != nn[start+3] and nn[start] != nn[start+6]:
                return True
        return False
    elif start == 3 or start == 4 or start == 5:
        if nn[start] != nn[start-3] and nn[start] != nn[start+3]:
                return True
        return False
    else:
        if nn[start] != nn[start-6] and nn[start] != nn[start-3]:
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/