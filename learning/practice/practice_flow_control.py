#created this file to practice some flow control
# Import Statements
import os 

# Helper Function Area
# Practice for If Statements
def if_statmenets():
    try:
        name = ''
        name = input(name)
        print(name)
        if name == 'Matt':
            print('Hi' , name , '.')
        else:
            print('It appears your name is unknown to me; ' , name, ', nice to meet you ',name,' .' )
    except:
        print('something really went wrong: DOH!!')

# Practice with a List of Values and Iterating through with various conditions
def if_with_lists():
    try:
        list = []
        name = ''
        counter = len(list)
        while counter <= 5:
            print(counter)
            counter = counter + 1
            list_value = input(name)
            list.append(list_value)
            print(counter, " Added " , list_value, 'marching to 10 ')
        else:
            if counter > 5:
                print( counter , 'All done here.')
                print(list)
            return
    except: 
        print('the add to list failed')
        print(list)
        print(name)
 
# Open a CSV file and load each line into a list. 
def playing_with_os():
    try:
        # print(help(os))
        print(os.getcwd() , " Current working Directory. ")
        print(os.cpu_count(), " Number of CPU's")
        print(os.uid() , " Currently Logged in Username.")
        print(os.listdir() , " List of files in current working Directory.")

    except:
        print('that didnt work.')
        return














# Main Function Area
def main():
    try:
        # if_statmenets()
        # if_with_lists()
        playing_with_os()

    except:
        print( 'Failed at the main level')


main()



