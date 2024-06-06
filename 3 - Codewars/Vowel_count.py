def get_count(sentence):
    count = 0
    for i in range (len(sentence)):
        if sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u":
            count += 1

    return(count)

get_count('aeiou')

#def getCount(inputStr):
#return sum(1 for let in inputStr if let in "aeiouAEIOU")