import random

NUM_QUESTIONS = 10

def makeIntQuestion(x):
	f.write( "::Question " + str(x) + "::[html]<p>Consider the following\: " + str( random.randint(1,1000) ) + ". What type of data is this?</p>{\n" )
	f.write( "\t=Integer\n" )
	f.write( "\t~Floating point\n" )
	f.write( "\t~String\n" )
	f.write( "\t~Function\n" )
	f.write( "}\n\n" )

def makeFloatQuestion(x):
	number = round( random.uniform(-100, 100), random.randint(1,5) )
	f.write( "::Question " + str(x) + "::[html]<p>Consider the following\: " + str(number) + ". What type of data is this?</p>{\n" )
	f.write( "\t~Integer\n" )
	f.write( "\t=Floating point\n" )
	f.write( "\t~String\n" )
	f.write( "\t~Function\n" )
	f.write( "}\n\n" )

# Trap: Present an integer or floating point as a string
def makeStrQuestion(x):
	if random.randint(1,2) == 1:
		number = round( random.uniform(-100, 100), random.randint(1,5) )
	else:
		number = str( random.randint(1,1000) )
	f.write( "::Question " + str(x) + "::[html]<p>Consider the following\: '" + str(number) + "'. What type of data is this?</p>{\n" )
	f.write( "\t~Integer\n" )
	f.write( "\t~Floating point\n" )
	f.write( "\t=String\n" )
	f.write( "\t~Function\n" )
	f.write( "}\n\n" )

CHAPTER = "ch1"
TOPIC = "data-types"

FILENAME = "bin/" + CHAPTER + "-" + TOPIC + ".txt"

f = open( FILENAME, "w" )

# Preamble
f.write( "$CATEGORY: " + CHAPTER + "/" + TOPIC + "\n\n" )

for x in range (NUM_QUESTIONS):
	roll = random.randint(1,3)
	if roll == 1:
		makeIntQuestion(x)
	if roll == 2:
		makeFloatQuestion(x)
	if roll == 3:
		makeStrQuestion(x)

f.close()
