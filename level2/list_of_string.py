
def isSubWord(word, subword):
    check = True
    short_length = len(subword)
    long_length = len(word)

    if (long_length<short_length):
        check = False
        return check
    elif(long_length == short_length):
        if(word==subword):
            return check
        else:
            check = False
            return check
    else:
        for k in range(long_length-short_length+1):
            check = True
            for i in range(short_length):
                if(word[i+k]!=subword[i]):
                    check = False
                if(i==3 and check==True):
                    return check
        return check

def filter_strings(dataList,word):
    valid=[]
    for i in dataList:
        words_array = i.split()
        for j in words_array:
            if isSubWord(j,word):
                valid.append(i)
    print (valid)

list_ = ['Do you play football?', 'I love hand ball', 'i love food', 'food is life', "I'm gonna be great with this", "I'm a learner of all ball related stuff", "if tennisballg was a thing?"]
filter_strings(list_,"ball")

# list_ = ['i want to learn', 'would you just let me learn', 'learning is good', 'i love food', 'food is life', "I'm gonna be great with this", "I'm a learner by nature"]
# filter_strings(list_,"learn")
