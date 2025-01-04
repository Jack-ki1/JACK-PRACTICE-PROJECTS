from collections import defaultdict


def group_anagrams(w):
    anagrams = defaultdict(list)
    
    for word in w:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)
        
    return anagrams


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))