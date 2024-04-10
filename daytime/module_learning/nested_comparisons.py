# the goal here is to compare items in one list to another list. 
# dictionaries
headers = {'a':10 , 'b':20 , 'c':30 , 'd':40}
permits = {'#a1':21 , '#b1':22 , '#c1':33}
approved_permits = {}
# Lists 
list_headers = []
list_permits = []
 
 

#Load up the Lists
for key in headers:
    list_headers.append(key)
print(list_headers)

for key in permits:
    list_permits.append(key)
print(list_permits)

# Do some accounting. 
total_headers = len(list_headers)
total_permits = len(list_permits)
begin_header = 0
begin_permit = 0 

# Create Global Variables
result_permit_span = permits.get(list_permits[begin_permit])
result_current_header_span = headers.get(list_headers[begin_header])
result_next_header_span = headers.get(list_headers[begin_header + 1 ])


print("Hdr's: " , total_headers, "P's: " ,  total_permits)

def perm_cat_01():
    for permit in list_permits:
        print('----------------------------------------')
        # Begin Permit
        print('Begin Permit index: ' , begin_permit)
        # Identify the First Permit in the List
        print('Permit ' , begin_permit , ' is ' , list_permits[begin_permit])
        # True if the Permit is in the List, it should be. 
        print(("Expected Result, True: " , list_permits[begin_permit]) in permits)
        # Begin processing each permit in the list. 
        if (list_permits[begin_permit]) in permits:
            print( "***The permit is in the Dictionary***")
            # Get the Permit Span
            result_permit_span = permits.get(list_permits[begin_permit])
            print("Current Permit Span is : " , result_permit_span)
            # Get comparison Spans
            # Current Header Span
            result_prior_header_span = headers.get(list_headers[begin_header])
            print("Previous Header Span is : " , result_prior_header_span )
            # Next Header Span
            result_later_header_span = headers.get(list_headers[begin_header + 1 ])
            print("Next Header Span is : " , result_later_header_span )
            # Create Comparison Logic
            if result_permit_span < result_later_header_span:
                
                print(approved_permits)
                print("No Need to continue processing")
                print( "This permits belongs in the category: " ,list_headers[begin_header] )
                
            else:
                begin_header = begin_header +1
                print("Current Value of begin header is : " , begin_header)
                print("Continuing to process")
        
        else: 
            print( 'The permit is not in the dictionary')
    
    print('+++++++++++++++++++++++++++++++++++++++')
    begin_permit = begin_permit + 1
    print('Increment Index + 1 ' , begin_permit)
    print('||||||||||||||||||||||||||||||||||||||||')
    

def permit_categorizer():
    for permit in list_permits:
        print(" Beginning Try")
        try:
            # Scenario 1 - Error Condition ( Permit is before Current Header)
            if result_permit_span < result_current_header_span:
                print( " Permit Occurs before the first header, there is an error")
            elif result_permit_span > result_current_header_span:
                and 
                
            print("Inside the Try")
        except:
            print("Error Occured Done")


def main():
    permit_categorizer()


main()
