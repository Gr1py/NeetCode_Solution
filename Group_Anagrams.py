# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

anagram_map = defaultdict(list)
        
for word in strs:
    sorted_word = ''.join(sorted(word))
    anagram_map[sorted_word].append(word)
        
print (list(anagram_map.values()))
