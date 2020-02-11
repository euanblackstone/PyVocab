from PyDictionary import PyDictionary

def main():
    dictionary = PyDictionary()
    file = open("words.txt", 'r')
    defdict = {}
    for word in file.readlines():
        tempword = word.strip('\n')
        definition = dictionary.meaning(tempword)
        defdict[tempword] = definition
    file.close()
    file = open("results.txt", "w")
    for k, v in defdict.items():
        tempstring = ("%s - %s" % (k, v))
        file.write(tempstring)

if __name__ == "__main__":
    main()