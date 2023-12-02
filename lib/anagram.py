# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, list_of_anagrams):
        matches = []
        for anagram in list_of_anagrams:
            if ''.join(sorted(anagram)) == self.sorted_word:
                matches.append(anagram)
        return matches
    
anagram_object = Anagram("listen")

list_of_anagrams = ["enlist", "silent", "gently", "intent", "denlist"]

matches = anagram_object.match(list_of_anagrams)

print(matches) # Output: ['enlist', 'silent', 'intent'] 