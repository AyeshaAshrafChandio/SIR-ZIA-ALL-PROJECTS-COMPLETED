


adjective = input("Enter a funny adjective (e.g., crazy, magical): ")
verb1 = input("Enter a silly action (e.g., dancing, singing): ")
verb2 = input("Enter another funny action (e.g., sleeping, laughing): ")
celebrity = input("Your favorite celebrity/cartoon character: ")


#We use an f-string to insert the user's words into our story template
#The \ at the end of first line lets us continue the string on next line
funny_story = f"Today was totally {adjective}! I spent the whole day {verb1} and then started {verb2}. \
My friend said, 'Dude! You’ve turned into {celebrity}!' 😂"

