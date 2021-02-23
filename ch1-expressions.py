import random

NUM_QUESTIONS = 10

def createExpression():
	startedPar = False
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
		string += " " + str(random.randint(1,10)) + " "
	return string
					

CHAPTER = "ch1"
TOPIC = "expression-evaluation"

FILENAME = "bin/" + CHAPTER + "-" + TOPIC + ".txt"

f = open( FILENAME, "w" )

# Preamble
f.write( "$CATEGORY: " + CHAPTER + "/" + TOPIC + "\n\n" )

for x in range (NUM_QUESTIONS):
	result = 10000 
	while result > 1000 or result < 0: # Dont give out questions where the result is some insanely large number
		question = createExpression()
		result = eval(question)
	f.write( "::Question " + str(x) + "::[html]<p>What is the result of the following Python expression\: " + question + "? <em>Evaluate these by hand first, then confirm their correctness by inputting the expression into the Python interpreter</em></p>{#" + str(result) + "}\n\n" )

f.close()
