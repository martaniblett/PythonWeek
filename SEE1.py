def see1(word, phrase):
    word_phrase_string = (word + phrase)
    word_phrase_list = word_phrase_string.split()
    
    count = 0
    for word in word_phrase_list:
        count = count + 1
    
    count = word_phrase_list.count(word)
    print (count)

see1("marta", "my nameis marta")


