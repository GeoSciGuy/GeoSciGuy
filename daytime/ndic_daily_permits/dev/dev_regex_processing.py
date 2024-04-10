import re
import pprint

# https://regexr.com/

csv_File = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv\dr11012.csv'
csvFile = open(csv_File)
csvFileContent = csvFile.read()
# print(csvFileContent)
# Debug Statements

# Regex Compilations
# Report Specific Data
reportnumRegEx = re.compile('REPORT:\W\d{5}')
reportnumber = re.findall(reportnumRegEx, csvFileContent)
print("Report Number")
print(reportnumber)

# Heading Regex Area
# Compile Statements, these are the things that are being search for. 
# headingsRegEx = re.compile(r'\w{8}:')
# headingsRegEx = r'(PERMITS APPROVED|PERMIT RENEWALS|ADDITIONAL INFORMATION|RELEASED FROM CONFIDENTIAL STATUS|DRY HOLE|TEMPORARILY ABANDONED WELL PLUGGED|PRODUCER NOW ABANDONED|CONFIDENTIAL WELLS PLUGGED OR PRODUCING|DATE|Active Daily Rig Count|APPROVED FOR CONFIDENTIAL STATUS|LOCATIONS RESURVEYED - SURFACE HOLE LOCATION CHANGE|PRODUCING WELL COMPLETED|PRODUCING WELLS COMPLETED|WELL NAME CHANGE)'
# all_headers = re.search(headingsRegEx, csvFileContent)

# Various Storage Lists and Dictionaries
found_headers = []
header_spans = []
found_permits = []
permit_spans = []
headersDict = {}
permitsDict = {}
legalsDict = {}

# Iterate through found headers and add them to the Headers Dictionary
# def find_headers():
    
#     with open(csv_File, 'r') as file:
#         reader = file.read(csv_File)
#         data = list(reader)
#     regex = r'(PERMITS APPROVED|PERMIT RENEWALS|ADDITIONAL INFORMATION|RELEASED FROM CONFIDENTIAL STATUS|DRY HOLE|TEMPORARILY ABANDONED WELL PLUGGED|PRODUCER NOW ABANDONED|CONFIDENTIAL WELLS PLUGGED OR PRODUCING|DATE|Active Daily Rig Count|APPROVED FOR CONFIDENTIAL STATUS|LOCATIONS RESURVEYED - SURFACE HOLE LOCATION CHANGE|PRODUCING WELL COMPLETED|PRODUCING WELLS COMPLETED|WELL NAME CHANGE)'
#     headersDict = {}
#     for i, row in enumerate(data):
#         for j, col in enumerate(row):
#             match = re.search(regex, col)
#             if match:
#                 headersDict[match.group()] = {'match': match.group(), 'span': (i,j)}
#     print(headersDict)

# Creating a new function to find headers
def find_headers():
    # Headers Regex
    # headingsRegEx = re.compile(r'\w{8}:')
    headingsRegEx = re.compile(r'((\w+)\s*(\w+)\s*:)')
    headers = headingsRegEx.findall(csvFileContent)
    headingIter = headingsRegEx.finditer(csvFileContent)
    for head in headingIter:
        headersDict[head.group()] = head.span()
    for key in headersDict.keys():
        found_headers.append(key)
    print(found_headers)
    print(headersDict)

def find_permits():
    # Permits Regex Area
    permitNumberRegEx = re.compile(r'#\d{5}')
    # Objects that are being returned if a Match is Searched for and found. 
    permits = permitNumberRegEx.findall(csvFileContent)
    permitIter = permitNumberRegEx.finditer(csvFileContent)
    for permit in permitIter:
        permitsDict[permit.group()] = permit.span()
    for key in permitsDict.keys():
        found_permits.append(key)
    # print("Found Permits")
    print(permitsDict)
    print(found_permits)
    print(len(found_permits))
    # permitz = permitNumberRegEx.search(csvFileContent)

def find_legals():
    #  Legal Regex Area
    legalRegEx = re.compile(r'[NESW]{2}\W[NESW]{2}')
    # Objects that are being returned if a Match is Searched for and found. 
    legals = legalRegEx.findall(csvFileContent)
    legalsIter = legalRegEx.finditer(csvFileContent)
    for legal in legalsIter:
        legalsDict[legal.group()] = legal.span()
    # print("Found some Legals")
    print(legalsDict)
    # Iterators used in Program
    # Iterate over Permits and Determine Grouping. 

def permit_grouping():
    # Local Variables
    total_permits = len(permitsDict)
    current_permit = 1
    current_header = 0
    next_header = current_header + 1
    num_of_headers = len(found_headers)
    num_of_permits = len(found_permits)
    beg_header_index = 0
    next_header_index = beg_header_index + 1 
    last_header_index = num_of_headers
    category = ''
    permit_approved_options = ['PERMITS APPROVED :']
    no_approved_permits = "No Permits Today"
    try:
        for i in permitsDict.items():
            for each in permit_approved_options:
                if each in found_headers:
                    print("Found the Approved Permit Header in Document. Will continue to process. ")
                    no_approved_permits = " There are permits today"
                else:
                    print( "No Approved Headers for today, halting execution")
                    return
            print("**********************************************")
            print("Total Permits: " , total_permits)
            print("Remaining Permits: " , total_permits - current_permit)
            print("Current permit is: " , i[0] , "Span beg's at: " , i[1][0])
            print("Approved Permits Exists?: " , no_approved_permits)
            header_span = headersDict.get(each)
            print('Header Span' , header_span)
            print("==============================================")
            current_permit = current_permit + 1
            print("increminting the permit counter")
            print("just procesed permit number" , current_permit - 1 )
            print("beginning span comparison")
            print("---------------------------------------------")
            # Create the two spinning wheels of comparisons. 
            # Need to know how many items are in the various lists. 
            # print("First Header is : " , found_headers[beg_header_index])
            # print( 'Next Header is : ' , found_headers[next_header_index])
            # print((found_headers[beg_header_index]) in headersDict)
            # beg_header_index = beg_header_index + 1
            # next_header_index = next_header_index + 1 
            print("==============================================")              
    except:
        print("Back to the drawing board, Exception Occured")    
        return

def permit_categorizer():
    # How many permits are there? 
    total_permits = len(found_permits)
    # How many headers are there?
    total_headers = len(found_headers)
    # Iterate over the Permits
    for permit in found_permits:
        print(permit)
        print(permit in permitsDict)





def main():
    try:
        find_headers()
        print('headers done')
        find_permits()
        print('permits done')
        find_legals()
        print('legals done')
        print("Program is done")
        # permit_grouping()
        permit_categorizer()
        print("Done with Permits")
    except:
        print("Program excepted out")

main()


