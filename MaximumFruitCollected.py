"""3,3,2,1,2,1,0,3,1,2
functions that returns a backet with the maximum fruit
sliding window problem with with the maximum of two types of fruits.
it is invalid if there are 3 distinct fruits.
Pick Two Types of Fruits" problem, where you need to find the longest
 subarray containing at most two distinct fruits."""

def fruit_into_baskets(fruits):
    start = 0
    state = {} #hashmap to track the frequencies of the
    max_fruit = 0 #store the maximum length of valid subarray
    for end in range(len(fruits)):
        #add current fruit to the map and if it exits increment by 1
        #ad not if it doesn't exist
        state[fruits[end]] = state.get(fruits[end], 0) + 1
        #if have more that two fruits iterate through
        while len(state) > 2:
            #shrink until we have only two distinct fruits
            state[fruits[start]] -= 1
            #if count becomes zero remove the fruit from the hashmap
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            start += 1 #move the start point to left
        max_fruit = max(max_fruit, end-start+1) #update maximum if it is longer
    return max_fruit

#sliding window problem two
"""You are given a string s and an integer k. 
You can choose any character of the string and change
 it to any other uppercase English character. 
 You can perform this operation at most k times.
Return the length of the longest substring containing 
the same letter you can get after performing the above operations.
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' 
in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, 
which is 4.
There may exists other ways to achieve this answer to"""
def characterReplacement(s:str, k:int) ->int:
    state = {} #stores the characters
    longest = 0 #stores the longest substring
    start = 0  #starting point
    max_val = 0 #max substring
    for end in range(len(s)):
        #check if the character exist exist in the map increment if it does
        #decrement if it doesn't
        state[s[end]] = state.get(s[end], 0) + 1
        #current substring
        window = end - start + 1
        #get most character appearing in the string
        max_val = max(max_val, state[s[end]])
        if window - max_val > k:
            #shrink the window
            state[s[start]] -=1
            start +=1
        longest = max(longest, end - start + 1)
    return longest
if __name__ == '__main__':
    s = "ABA"
    k = 2
    print(characterReplacement(s, k))
#what is a variable
print("hello")
help(round)


