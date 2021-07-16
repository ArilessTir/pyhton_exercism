def count_words(sentence):
    charactere_interdit = ['!','&','@','$','%','^','&',',',';','\n']
    dico = {}
    sentence = sentence.lower()
    for char in charactere_interdit:
        if char in sentence:
            sentence = sentence.replace(char, ' ')
    for i in sentence.split():
        dico[i] = sentence.split().count(i)

    return dico

 