from typing import List
#traversing the matrix in columnar zigzag format
def column_traverse(matrix:List[List[int]]):
    #initializing the rows and cols
    rows,cols = len(matrix),len(matrix[0])
    directions = "up" #upward motions
    row,col = rows-1,cols-1
    next=[]
    while(len(next)<rows * cols):
        next.append(matrix[row][col])
        if directions == "up":
            #checking if the top row has been visited
            if row -1 < 0 :
                directions = "down"
                col = col - 1 #move to the next column to go down
            else:
                row -= 1 #move up in the current column
        else:
            if directions == "down":
                if row + 1 == rows: #at bottom switch direction
                    directions = "up"
                    col = col - 1 #move to next column
                else:
                    row = row + 1 #move down in the current column
    return next
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(column_traverse(matrix))
#implement the reversal order matrix display
def reverse_traverse(matrix:List[List[int]]) -> List[int]:
    rows,cols = len(matrix),len(matrix[0])
    output = []
    for row in range(rows-1, -1, -1):
        for col in range(cols-1,-1,-1):
            output.append(matrix[row][col])
    return output
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("print the  matrix in reverse order")
print(reverse_traverse(matrix))

"""in this challenge, let's adjust our book traversal method! Originally,
 our method involved traversing even-indexed columns upwards and odd-indexed
  columns downwards. Your task is to reverse this pattern without adding
   new lines of code. Make the necessary change in the condition within the
    loop so that even-indexed columns are traversed downwards, and odd-indexed
     ones upwards."""
def print_books_traverse(book_shelves: List[List[int]]) -> List[int]:
    rows,cols = len(book_shelves),len(book_shelves[0])
    output = []
    for col in range(cols-1,-1,-1):
        if col % 2 != 0:
            for row in range(rows-1,-1,-1):
                output.append(book_shelves[row][col])
        else:
            for row in range(rows):
                output.append(book_shelves[row][col])
    return output

book_shelves = [[1,2,3],[4,5,6],[7,8,9]]
print(print_books_traverse(book_shelves))

