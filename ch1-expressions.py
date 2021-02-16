import random

def createExpression():
	string = str(random.randint(1,5)) + " ";
	for x in range(random.randint(1,3)):
		# Append a random connective
		op = random.randint(1,5)
		if op == 1:
			string += "+"
		elif op == 2:
			string += "-"
		elif op == 3:
			string += "*"
		elif op == 4:
			string += "//"
		elif op == 5:
			string += "**"
		string += " " + str(random.randint(1,10))
	return string
					

CHAPTER = "ch1"
TOPIC = "expression-evaluation"
FILENAME = "bin/" + CHAPTER + "-" + TOPIC + ".txt"

f = open( FILENAME, "w" )

# Preamble
f.write( "$CATEGORY: " + CHAPTER + "/" + TOPIC + "\n\n" )

for x in range (10):
	f.write( "::Question " + str(x) + "::[html]<p>What is the result of the following Python expression\: " + createExpression() + "{\n\n\n")

f.close()
