class Solution(object):
    def uniqueMorseRepresentations(self, words):
        def get_morse_string(word):
            result = ""
            codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                     "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
            for char in word:
                result = result + codes[ord(char) - ord('a')]
            return result

        return len(set(map(get_morse_string, words)))
