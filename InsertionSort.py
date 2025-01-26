def insertion(arr):
    for i in range(1, len(arr)): #loop through the array from 1 to last index
        key = arr[i] #initialize the key with the first element
        j = i -1  #initialize the next element
        #move all elements greater than the key to one position heade
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j] #move the element to one position a head
            j= j-1 #decrement the index
        arr[j+1] = key
def print_arry(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("Next:")
if __name__ == "__main__":
    elements = [15, 1, 7, 18, 200, 100, 65, 9]
    print_arry(elements)
    insertion(elements)
    print_arry(elements)