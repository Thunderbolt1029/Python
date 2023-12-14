wordListFile = open("words.txt", "r")
words = wordListFile.read().split("\n")


wordLen3 = open("3letterwords.txt", "w"); wordLen3.write(""); wordLen3.close()
wordLen4 = open("4letterwords.txt", "w"); wordLen4.write(""); wordLen4.close()
wordLen5 = open("5letterwords.txt", "w"); wordLen5.write(""); wordLen5.close()
wordLen6 = open("6letterwords.txt", "w"); wordLen6.write(""); wordLen6.close()
wordLen7 = open("7letterwords.txt", "w"); wordLen7.write(""); wordLen7.close()
wordLen8 = open("8letterwords.txt", "w"); wordLen8.write(""); wordLen8.close()
wordLen9 = open("9letterwords.txt", "w"); wordLen9.write(""); wordLen9.close()
wordLen10 = open("10letterwords.txt", "w"); wordLen10.write(""); wordLen10.close()


wordLen3 = open("3letterwords.txt", "a")
wordLen4 = open("4letterwords.txt", "a")
wordLen5 = open("5letterwords.txt", "a")
wordLen6 = open("6letterwords.txt", "a")
wordLen7 = open("7letterwords.txt", "a")
wordLen8 = open("8letterwords.txt", "a")
wordLen9 = open("9letterwords.txt", "a")
wordLen10 = open("10letterwords.txt", "a")


for i in range(len(words)):
    word = words[i]
    if len(word)<3 or len(word)>10: continue
    elif len(word)==3: wordLen3.write(word+"\n")
    elif len(word)==4: wordLen4.write(word+"\n")
    elif len(word)==5: wordLen5.write(word+"\n")
    elif len(word)==6: wordLen6.write(word+"\n")
    elif len(word)==7: wordLen7.write(word+"\n")
    elif len(word)==8: wordLen8.write(word+"\n")
    elif len(word)==9: wordLen9.write(word+"\n")
    elif len(word)==10: wordLen10.write(word+"\n")

wordLen3.close()
wordLen4.close()
wordLen5.close()
wordLen6.close()
wordLen7.close()
wordLen8.close()
wordLen9.close()
wordLen10.close()