def anagrams():
    str_words = input()
    words = str_words.split()
    sorted_word1 = ''.join(sorted(words[0].lower()))
    sorted_word2 = ''.join(sorted(words[1].lower()))
    if sorted_word1 == sorted_word2:
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"

print(anagrams())
