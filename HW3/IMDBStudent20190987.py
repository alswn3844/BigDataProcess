import sys
inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])
genreList = {}

f = open(outputFile, "at")
with open(inputFile,"rt") as fp:
	for line in fp:
		movie = line.split('::')
		if movie[2].find('|'):
			genre = movie[2].split('|')
			for i in genre:
				if i.strip() in genreList:
					genreList[i.strip()] = genreList[i.strip()]+1
				else:
					genreList[i.strip()] = 1
		else:
			genre = movie[2].strip()
			if genre in genreList:
				genreList[genre] = genreList[genre]+1
			else:
				genreList[genre] = 1
keylist = genreList.keys()
for i in keylist:
	f.write("%s %d\n" % (i, genreList[i]))
f.close()
