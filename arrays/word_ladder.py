from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))  # (current_word, level)
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            # Try all possible one-letter transformations
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]
                    
                    if new_word in wordSet:
                        queue.append((new_word, steps + 1))
                        wordSet.remove(new_word)  # avoid revisiting
        
        return 0