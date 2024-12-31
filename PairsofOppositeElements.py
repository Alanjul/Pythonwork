from typing import List
import math
def solution(numbers: List[int]) -> List[int]:
    n = len(numbers)
    result = [] #empty lisr
    for i in range(n):
        #append  the tuple number and it's opposite
        result.append((numbers[i], number[n-i-1]))
    return result


number = [1, 2, 3, 4, 5, 6, 7]
print(solution(number))

#returning an geometric mean and it's opposit
def solution2(numbers: List[int]) -> List[int]:
    n = len(numbers)
    result = []
    for i in range(n):
        a = numbers[i]
        b = numbers[n-i-1]
        mean = math.sqrt(a * b)
        answer = round(mean,2)
        result.append((a, answer))
    return result
numbers = [1, 2, 3, 4, 5, 6, 7]
print(solution2(numbers))