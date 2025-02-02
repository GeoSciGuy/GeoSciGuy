import re


# https://regexr.com/


# Steps to using RegEx
# Import the regex module with import re.
# Create a Regex object with the re.compile() function. (Remember to use a raw string.)
# Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
# Call the Match object’s group() method to return a string of the actual matched text.

# There are three steps to reading or writing files in Python:
# Call the open() function to return a File object.
# Call the read() or write() method on the File object.
# Close the file by calling the close() method on the File object.
# Open the file to read
csvFile = open(r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv\dr02062.csv')
csvFileContent = csvFile.read()
# print(csvFileContent)

# Regex Compilations
# Report Specific Data
reportnumRegEx = re.compile('REPORT:\W\D{5}')
reportnum = reportnumRegEx.findall(csvFileContent)

# Heading Regex Area
# Compile Statements, these are the things that are being search for. 
# headingsRegEx = re.compile(r'\w{8}:')
approvedRegEx = re.compile('PERMIT\W\WAPPROVED:')
additionalinfoRegEx = re.compile('ADDITIONAL\WINFORMATION:')
confidentialRegEx = re.compile('CONFIDENTIAL')

# Objects that are being returned if a Match is Searched for and found. 
approvedheadings = approvedRegEx.findall(csvFileContent)

# Permits Regex Area
permitNumberRegEx = re.compile(r'#\d{5}')

# Objects that are being returned if a Match is Searched for and found. 
permits = permitNumberRegEx.findall(csvFileContent)
permitz = permitNumberRegEx.search(csvFileContent)

# Legal Regex Area
legalRegEx = re.compile('\w{2} \w{2}')

# Objects that are being returned if a Match is Searched for and found. 
legals = legalRegEx.findall(csvFileContent)


# Iterators used in Program
iterator = approvedRegEx.finditer(csvFileContent)

for match in iterator:
    print(match.group())
    print(match.span())
    
                        
# Debug Statements
print("Matched Headers")
print(approvedheadings)
print("Matching Permits")
print(permits)
# print("Matched Legals")
# print(legals)
# print("Permitz")
# print(permitz.group())
# print(iterator)



# The following list of special sequences isn’t complete. 
# For a complete list of sequences and expanded class definitions for Unicode string patterns,
#  see the last part of Regular Expression Syntax in the Standard Library reference.
#  In general, the Unicode versions match any character that’s in the appropriate category
#  in the Unicode database.

# \d
# Matches any decimal digit; this is equivalent to the class [0-9].

# \D
# Matches any non-digit character; this is equivalent to the class [^0-9].

# \s
# Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

# \S
# Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

# \w
# Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

# \W
# Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

# These sequences can be included inside a character class. 
# For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.
# The final metacharacter in this section is .. 
# It matches anything except a newline character, 
# and there’s an alternate mode (re.DOTALL) where it will match even a newline. .
#  is often used where you want to match “any character”.