def mysplit(strng):
    listOfWords = []
    word = ""
    for ch in strng:
        if ch != " ":
            word += ch
        else:
            if word:
                listOfWords.append(word)
                word = ""
    if word:
        listOfWords.append(word)
    return listOfWords
