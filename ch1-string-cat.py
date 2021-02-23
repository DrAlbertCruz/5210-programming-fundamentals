# Generate random HW questions about what happens if you try to do various 
# strcat operations in the Python command line. Questions test knowledge of 
# syntax and semantics

import random

NUM_QUESTIONS = 15


# Bakersfield themed strings
BAKO_STRINGS = [ "Bakersfield",
	"Kern",
	"Apple",
	"Camelot",
	"Carrot",
	"Horse",
	"Dog",
	"Murray",
	"Fox",
	"Hart",
	"Rabobank" ]

# Correct string concatenation
def makeStrCatC1(x):
	str1 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	str2 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	f.write( "::Question " + str(x) + "::[html]<p>You want to combine two strings together\: " + str1 + " and " + str2 + ", so that it reads\:</p><pre>" + str1 + str2 + "</pre>Consider this command:</p><pre>&#62;&#62;&#62; " + str1 + " + " + str2 + "</pre><p>Is there an error?</p>{\n" )
	f.write( "\t=No, this is correct.\n" )
	f.write( "\t~Yes, there is a syntax error.\n" )
	f.write( "\t~Yes, there is a semantic error.\n" )
	f.write( "\t~Yes, there is a semantic error and a syntax error.\n" )
	f.write( "}\n\n" )

# Python's weird string multiplication command
def makeStrCatC2(x):
	str1 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	number = random.randint(0,20);
	f.write( "::Question " + str(x) + "::[html]<p>You want to repeat the  string " + str1 + " " + str(number) + " times so that it reads\:</p><pre>" + str1 * number + "</pre>Consider this command:</p><pre>&#62;&#62;&#62; " + str1 + " * " + str(number) + "</pre><p>Is there an error?</p>{\n" )
	f.write( "\t=No, this is correct.\n" )
	f.write( "\t~Yes, there is a syntax error.\n" )
	f.write( "\t~Yes, there is a semantic error.\n" )
	f.write( "\t~Yes, there is a semantic error and a syntax error.\n" )
	f.write( "}\n\n" )

# Mixing ' attempting to use a possessive: apostrophe will cause an error
def makeStrCatX1(x):
	str1 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	str2 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	f.write( "::Question " + str(x) + "::[html]<p>You want to combine two strings together\: " + str1 + " and " + str2 + ", so that it reads\:</p><pre>" + str1 + "'s " + str2 + "</pre>Consider this command:</p><pre>&#62;&#62;&#62; " + str1 + " + ''s ' + " + str2 + "</pre><p>Is there an error?</p>{\n" )
	f.write( "\t~No, this is correct.\n" )
	f.write( "\t=Yes, there is a syntax error.\n" )
	f.write( "\t~Yes, there is a semantic error and a syntax error.\n" )
	f.write( "}\n\n" )

# missing a space causing a semantic error
def makeStrCatX2(x):
	str1 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	str2 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	f.write( "::Question " + str(x) + "::[html]<p>You want to combine two strings together\: " + str1 + " and " + str2 + ", so that it reads\:</p><pre>" + str1 + "'s " + str2 + "</pre>Consider this command:</p><pre>&#62;&#62;&#62; " + str1 + " + \"'s\" + " + str2 + "</pre><p>Is there an error?</p>{\n" )
	f.write( "\t~No, this is correct.\n" )
	f.write( "\t=Yes, there is a syntax error.\n" )
	f.write( "\t~Yes, there is a semantic error and a syntax error.\n" )
	f.write( "}\n\n" )

# Combo of X1 and X2 -- syntax and a semantic error
def makeStrCatX3(x):
	str1 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	str2 = BAKO_STRINGS[ random.randint(0,len(BAKO_STRINGS)-1) ];
	f.write( "::Question " + str(x) + "::[html]<p>You want to combine two strings together\: " + str1 + " and " + str2 + ", so that it reads\:</p><pre>" + str1 + "'s " + str2 + "</pre>Consider this command:</p><pre>&#62;&#62;&#62; " + str1 + " + ''s' + " + str2 + "</pre><p>Is there an error?</p>{\n" )
	f.write( "\t~No, this is correct.\n" )
	f.write( "\t~Yes, there is a syntax error.\n" )
	f.write( "\t=Yes, there is a semantic error and a syntax error.\n" )
	f.write( "}\n\n" )

CHAPTER = "ch1"
TOPIC = "string-cat"

FILENAME = "bin/" + CHAPTER + "-" + TOPIC + ".txt"

f = open( FILENAME, "w" )

# Preamble
f.write( "$CATEGORY: " + CHAPTER + "/" + TOPIC + "\n\n" )

for x in range (NUM_QUESTIONS):
	roll = random.randint(1,3)
	makeStrCatC2
	#if roll == 1:
	#	makeStrCatC1(x)
	#if roll == 2:
	#	makeStrCatX1(x)
	#if roll == 3:
	#	makeStrCatX2(x)

f.close()
