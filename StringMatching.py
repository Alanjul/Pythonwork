"""Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

 """
from typing import List
def stringMatching(words:List[str]) -> List[str]:

   #sort words by length
    words.sort(key=len, reverse=True)
    result = []
    #set to store words
    word_set = set()
   #loop through words
    for word in words:

        #check if the word is set
        for seen_word in word_set:

            if word in seen_word:
                result.append(word) #apend it to result
                break
        word_set.add(word)

    return result #return result
words = ["mass","as","hero","superhero"]
print(stringMatching(words))