import shlex
from random import randint
wordsToCheck = ["hyakpacento","bowel control","hey","goodnight","goodjob","impendingdisaster",'impending disaster','goddamnit','shutup',"shutupben","go home", 'jon','confused']
command_args = ["go","home"]

testString = "wow go home"
length = len(testString)

phrases = ["k","something ","another thing"]
phrasenum = randint(0,2)

print(phrases[phrasenum])
# Beyond this point we process script commands only
# if the sentence one word then find it in the list of words to check
#OR if the sentence is more than one word and this word is the first one use that
# OR if the word has a space before it. This is to make sure its a single word and not like sneaking
if(testString in wordsToCheck):
	print(testString)

for word in wordsToCheck:	
	if (testString.find(word) >=0 and ((len(command_args)==1 and (word in command_args)) or ( len(command_args) > 1 and (testString.find(word+" ")==0) or (" "+word+" " in testString) or (testString.find(" "+word)==(length-len(word)-1))))):
		print(word)
		break
