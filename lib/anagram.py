# your code goes here!
class Anagram:
    def __init__(this, term):
        this.term = sorted(term.lower())

    def match(this, word_list):
        return [w for w in word_list if this._is_anagram(w)]

    def _is_anagram(this, other_word):
        return this.term == sorted(other_word.lower())



