#creating a 2d array
numbers = [[1,2,3,4,6],
           [7,8,10,11],
           [30,12,34,15,17]]
numbers[1][0] = 80 #update
#adding new elements to the floor
numbers.append([81,90,100,110])
#remove 10
numbers[1].remove(10)
#loop through the arrays
for floor in numbers:
    for row in floor:
        if row == 100:
            break
        print(row, end=", ")
    print()
