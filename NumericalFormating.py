number = 27
#add a plus  sign at the front with zeros as leading
print(f'[{number:+010d}]')
print(f'[{number: d}]') #add a spaces
print(f'[{100000:,d}]')
value1 = 10240.47
value2 = -3210.9521
print(f'[{value1:+10,.2f}]')
print(f'[{value2:-10,.2f}]')
string1 = '{:.2f}'.format(156.12)  # format the numbers as string
print(string1)
string2 = '{} {}'.format("Amanda","Cyan")
print(string2)
string3  = '{0} {0} {1}'.format("happy", "Cyan")
print(string3)
string4= '{last} {first}'.format(last ="Alan", first="Gray")
print(string4)

print('[{:c} {:c} ]'.format(45, 41))
print('{:c}'.format(58))
print('[{name:^10}]'.format(name="amanda"))
print('[{name:<10}]'.format(name="amanda"))
print('[{name:>10}]'.format(name="amanda"))
print('[{number1:+10,.2f}]'.format(number1=-3210.9521))
print('[{number2:+10,.2f}]'.format(number2=10240.47))
def merge(arr,left,mid, right):
    n1 = mid -left+1
    n2 = right -mid
    #create temporary array
    array1 = [0]* n1 #left array created
    array2 = [0] * n2 #right array created

    #copy elements in array1 and array2
    for i in range(n1):
        array1[i] = arr[left +i]
    for j in range(n2):
        array2[j] = arr[mid+1 +j]
    i = 0
    j= 0
    k = left #initializing the index of original array
    while i < n1 and j < n2:
        if array1[i] <= array2[j]:
            arr[k] = array1[i]
            i +=1
        else:
            arr[k] = array2[j]
            j +=1
        k +=1
        #sorting any remaining item in array1
    while i < n1:
        arr[k] = array1[i]
        i +=1
        k+=1
        #sorting an remaining items in array2
    while j < n2:
        arr[k] = array2[j]
        j +=1
        k +=1
def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        return arr
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
if __name__ == "__main__":
    elements = [1, 12, 16, 5, 18, 3, 5, 10,100, 90, 25, 36]
    printArray(elements)
    mergeSort(elements, 0, len(elements) - 1)
    print()
    printArray(elements)

