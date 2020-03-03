def duplicate_encode(word):
    #your code here
    word = word.lower()
    answer = []
    for j in range (len(word)):
    
        letter = word[j]
        
        for i in range (len(word)):
            if i == j:
                if j == (len(word)-1):
                    answer.append("(")
                    break
                else:
                    continue
            elif letter == word[i]:
                answer.append(")")
                break
            elif i == (len(word)-1):
                answer.append("(")
                break

    return"".join(answer)