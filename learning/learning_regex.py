import re



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
print(csvFileContent)

permitNumberRegEx = re.compile(r'#\d\d\d\d\d')
companyNameRegEx = re.compile()
permits = permitNumberRegEx.findall(csvFileContent)
print(permits)

headings = ['PERMIT APPROVED','ADDITIONAL INFORMATION','RELEASED FROM “CONFIDENTIAL” STATUS:  ']
for line in csvFile:
    print(line,end='')
    print(line)
