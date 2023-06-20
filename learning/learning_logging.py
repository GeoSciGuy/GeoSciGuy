# Import Logging
import logging
import os

# Global variable area
log_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\py_logs'

# General Notes from the Tutorial on Python.Org

# Task you want to perform                                  # The best tool for the task
#-------------------------------------------------------#  #----------------------------------------------------------------#
# Display console output for ordinary usage of a 
# command line script or program
                                                            # print()

# Report events that occur during normal operation
#  of a program (e.g. for status monitoring or fault investigation)

                                                            # logging.info() (or logging.debug() 
                                                            # for very detailed output for diagnostic purposes)

# Issue a warning regarding a particular runtime event

                                                            # warnings.warn() in library code if the
                                                            # issue is avoidable and the client
                                                            # application should be modified to eliminate the warning

                                                            # logging.warning() if there is nothing 
                                                            # the client application can do about 
                                                            # the situation, but the event should still be noted

# Report an error regarding a particular runtime event

                                                            # Raise an exception    

# Report suppression of an error without raising an
#  exception 
# (e.g. error handler in a long-running server process)

                                                            # logging.error(), logging.exception() or logging.critical()
                                                            #  as appropriate for the specific error and application domain.


# Level
    # When it’s used

# DEBUG
    # Detailed information, typically of interest only when diagnosing problems.
# INFO
    #Confirmation that things are working as expected.
# WARNING
    # An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR
    # Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL
    # A serious error, indicating that the program itself may be unable to continue running.          

# Example 1
# Logging to the screen. 
# logging.warning('Watch out!') # Will print a message to the console.
# logging.info('I told you so') # Will not print anything. 

# Example 2
# Logging to a file.

# logging.basicConfig(filename = 'example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

# Example 3
#Logging from multiple modules
# myapp.py
# import logging


# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logging.info('Started')
#     print("Test App Complete")
#     logging.info('Finished')

# if __name__ == '__main__':
#     main()

# Example 4
# Logging Variable Data
# logging.warning('%s before you %s', 'Look', 'leap!')

# Ex 5. 
# Changing the Format of displayed messages
# # To change the format which is used to display messages, you need to specify the format you want to use:
# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')

# Ex 6. Displaying the date/time in messages
# To display the date and time of an event, you would place ‘%(asctime)s’ in your format string:
# import logging
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('is when this event was logged.')

# The default format for date/time display (shown above) is like ISO8601 or RFC 3339. If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig, as in this example:
# This is the format I want! ************************###
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
