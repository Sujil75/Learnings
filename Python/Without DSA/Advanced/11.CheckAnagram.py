def checkAnagram(w1, w2):
    if len(w1) != len(w2): return False

    for i in range(len(w1)):
        if w1[i] not in list(w2):
            return False
    
    return True

word1, word2 = map(str, input("Enter the two words to check Anagram: ").split(", "))

result = checkAnagram(word1, word2)
print(result)