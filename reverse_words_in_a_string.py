s = "Let's take LeetCode contest"

class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        result = []

        for word in words:
            reversed_word = word[::-1]
            result.append(reversed_word)
        return " ".join(result)
            