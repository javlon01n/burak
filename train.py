def reverseSentence(text):
    words = text.split()
    new_words = []
    
    
    for word in words:
        reversed_word = word[::-1]
        new_words.append(reversed_word)
    return " ".join(new_words) 

result = reverseSentence("we like coding!")
   
print(result)   