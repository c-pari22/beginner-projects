
story = open("story.txt", "w")
draft = open("rough.txt", "r")

def replaceI(line):
	counter = 0
	prev = None	
	new_line = ""
	for i in range(len(line)-1):
		if line[i] == "i":
			if (prev == " " or prev == "-" or prev == None) and (line[i+1] == "-" or line[i+1] == " "):
				new_line += "I"	
				counter += 1		
			else:
				new_line += line[i]
		else:
			new_line += line[i]
		prev = line[i]		
	return new_line, counter
count = 0
for line in draft:	
	reviewed, errors  = replaceI(line)
	count += errors
	story.write(reviewed + "\n")
print("There were {} errors in the text".format(count))
story.close()
