import re

# This reader prints how many times a specific opening was played within a database


def ImportChessDataBase(filePath, counts):
    inputFile = open(filePath, "r")
    count = ReadChessDataBase(inputFile, counts)
    inputFile.close()


def ReadChessDataBase(inputFile, counts):
    count = 0
    for line in inputFile:
        line = line.rstrip()  # remove the end of the line character
        if re.search("Opening", line):
            match = re.search(r'"([^"]+)"', line)
            opening = match.group(1)
            count = counts.get(opening, None)
            if count == None:
                counts[opening] = 1
            else:
                counts[opening] = count + 1


counts = dict()
ImportChessDataBase(
    "/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/Chess/Stockfish_15_64-bit.commented.[2600].pgn", counts)

for opening in counts:
    print(opening + " was played " + str(counts[opening]) + " times.")
