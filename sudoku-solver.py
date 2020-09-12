puzzle = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]

def print_matrix(bo):

    for ind in range(len(bo)):

        if (ind % 3) == 0 and ind != 0:
            print("- - - - - - - - - - - - - - - - - - - - -")

        obj = bo[ind]

        elem_ind = 0

        for elem in obj:

            if (elem_ind % 3) == 0 and elem_ind != 0:
                print(" | ", end=" ")

            print(elem, end="  ")

            elem_ind += 1

        print("\n")


def find_empty(puz):

    for i in range(len(puz)):
        for j in range(len(puz[i])):
            if puz[i][j] == 0:
               return (i,j)

    return False


def fill_matrix(puz):


    global puzzle
    empty_val = find_empty(puzzle)

    if not empty_val:
        return True

    for ind in range(len(puzzle[0])):
            val = ind+1

            if validate(val,empty_val[0],empty_val[1],puzzle):

                puzzle[empty_val[0]][empty_val[1]] = val

                if fill_matrix(puz):
                    return True

                puzzle[empty_val[0]][empty_val[1]] = 0

    return False


def validate(val,i,j,puz):

    #Check row
    for row_elem in range(len(puz[i])):
        if puz[i][row_elem] == val and j != row_elem:
            return False

    #Check column
    for col_elem in range(len(puz)):
        if puz[col_elem][j] == val and i != col_elem:
            return False

    #Check Square

    sq_row = int(i/3)
    sq_col = int(j/3)

    for row_ind in range(sq_row*3, (sq_row*3)+3):
        for col_ind in range(sq_col*3, (sq_col*3)+3):

            if puz[row_ind][col_ind] == val:
                return False

    return True


print_matrix(puzzle)

print(" \n \n ___________________________________________________________________________ \n \n")

fill_matrix(puzzle)

print_matrix(puzzle)
