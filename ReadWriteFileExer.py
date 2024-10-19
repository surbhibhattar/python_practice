'''Exer 1'''

wordsDict = {}

def find_max_occurence():
    f = open("poem.txt","r")
    words = []
    for line in f:
        arr = line.split(' ')
        words+=arr
    for word in words:
        if word in wordsDict:
            wordsDict[word]+=1
        else:
            wordsDict[word]=1
    maxWords = {}
    all_values = list(wordsDict.values())
    max_value = max(all_values)

    for key, value in wordsDict.items():
        if value == max_value:
            maxWords[key]=value
    print(maxWords)


# find_max_occurence()

'''Exer 2'''

def stock_market_app():
    output=""
    with open("stocks.csv", mode='r') as file:
        index=0
        for line in file:
            # print(line)
            arr = line.split(",")
            if index==0:
                newLine = arr[0] + "," + "PE Ratio" + "," + "PB Ratio"
                output+=newLine
                output+="\n"
            else:
                peRatio = float(arr[1]) / float(arr[2])
                pbRatio = float(arr[1]) / float(arr[3])
                newLine = arr[0] + "," + str(peRatio) + "," + str(pbRatio)
                output+=newLine
                output+="\n"
            index+=1
        # print(output)

    with open("output.csv", mode='w') as file:
        file.write(output)


    # f = open("output.csv","a")


stock_market_app()
