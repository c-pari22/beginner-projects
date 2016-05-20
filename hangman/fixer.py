

fileName = input("Fix up what file? ")


f = open(fileName, "r")
lines = f.readlines()
f.close()

blacklist = ['SPIN ID','2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008']

with open("wof.txt", "a") as myfile:
	for line in lines:
		shouldWrite = True
		for item in blacklist:
			if item in line or line == "\n":
				shouldWrite = False
		if shouldWrite:
			myfile.write(line)
