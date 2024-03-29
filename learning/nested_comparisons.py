# the goal here is to compare items in one list to another list. 
# dictionaries
from unittest import result


headers = {'a':10 , 'b':20 , 'c':30}
permits = {'#a1':21 , '#b1':22 , '#c1':33}
approved_permits = {}
# Lists 
list_headers = []
list_permits = []

for key in headers:
    list_headers.append(key)
print(list_headers)

for key in permits:
    list_permits.append(key)
print(list_permits)
  
total_headers = len(list_headers)
total_permits = len(list_permits)
begin_header = 0
begin_permit = 0 

print("H: " , total_headers, "P: " ,  total_permits)

for permit in list_permits:
    print('----------------------------------------')
    print('Begin Permit index: ' , begin_permit)
    print('Permit ' , begin_permit , ' is ' , list_permits[begin_permit])
    print((list_permits[begin_permit]) in permits)
    
    if (list_permits[begin_permit]) in permits:
        result_permit_span = permits.get(list_permits[begin_permit])
        print(result_permit_span)
        result_prior_header_span = headers.get(list_headers[begin_header])
        result_later_header_span = headers.get(list_headers[begin_header + 1 ])
        print("Previous Header Span: " , result_prior_header_span )
        print("Next Header Span is: " , result_later_header_span )
        if result_permit_span < result_later_header_span:
            approved_permits[list_permits[begin_permit]] = list_headers[begin_header]
            print(approved_permits)
            print("No Need to continue processing")
            print( "This permits belongs in the category: " ,list_headers[begin_header] )
        elif result_permit_span > result_prior_header_span:
            print("Continuing to process")

    print('+++++++++++++++++++++++++++++++++++++++')
    print('Increment Index + 1 ' , begin_permit)
    print('||||||||||||||||||||||||||||||||||||||||')