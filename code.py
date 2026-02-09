from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        # Remove beginWord from the set if present to avoid revisiting
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        while queue:
            current_word, leve