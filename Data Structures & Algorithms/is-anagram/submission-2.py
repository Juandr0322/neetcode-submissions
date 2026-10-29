class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = True
        word_s = []
        word_t = []
        if len(s) == len(t):
            for i in range(len(s)):
                word_s.append(s[i])
                word_t.append(t[i])
            word_s.sort()
            word_t.sort()
            for i in range(len(s)):
                if word_s[i] != word_t[i]:
                    anagram = False
                    break
        elif len(s) != len(t):
                anagram=False
        return anagram