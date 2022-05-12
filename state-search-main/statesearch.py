# 1. Complete the header comments
# Shane Steiner
# Python version 3.10.0
# State Capitol Search

# Allow for 5 Searches
# Save Results of search to state_result.txt

#########################################
# IMPORT THE STATES & CAPITOLS
#########################################

# 2. Explain why we start with an empty Dictionary
# A: We use an empty Dictionary to set the varible so we can use it later in the script.
# Create Blank Dictionary
states = {}

# 3. Explain how the FOR Loop here is used to import the data
#  and separate it into KEY / VALUE pairs.
# A: The for loop takes each line from states.txt and separates the key & value.
# This makes it easy for the user to put in a state name and for it to return the capital for that state name.
# Import State & Capitol in the blank Dictionary
with open('states.txt', 'r') as f:
    for line in f:
        (key, val) = line.split(',')
        states[key] = val

# User must enter the name of the state to search
print ('STATE SEARCH SCRIPT')
print ('Please enter the name of 5 states to search for.')
# 4. Create a variable called count with an assigned value of 5
count = 5

##########################################
# LOOP THE SEARCH & WRITE TO EXTERNAL FILE
##########################################

# Open Report file
f = open('state_results.txt', 'w+')

# 5. Describe how the WHILE Loop uses the count variable as a control.
# A: While count is greater than 0:
        # Once the user searches count -= 1
        # Once count hits 0 the loop ends
# 6. How is the count variable updated?
# A: Everytime the user searches count -= 1.
# 7. What is the effect?
# A: The count varible has the effect of making sure the user has a limit amount of times to search before the script ends.
# 8. Explain how states[search] returns a value.
# A: for line in f:
       # (key, val) = line.split(',')
        #states[key] = val
    # Because that we are splitting the key and value when we put states[search] it will return the value from that key.
    # Hopefully I explained it well enough.
    # states[key] = val and now all you need is print(states['New York'])

# Use a Loop to run search 5 times
while count > 0:
    search = str(input('Enter Name of State: ')).title()

    # Check the Dictionary for the State / Capitol result
    if search in states:
        print ('The Capitol of ' + search + ' is ' + states[search])
        count -= 1
        print ('Remaining number of searches: ', count)
        f.write('State: ' + search + ' Capitol: ' + states[search])
    else:
        print ("You have entered an incorrect value.")

###########################################

# 9. Rewrite the LOOP SEARCH Section above (Lines 22 - 28) to utilize with open()
#with open('states.txt', 'r') as f:
 #   for line in f:
  #      (key, val) = line.split(',')
  #      states[key] = val
# 10. Test and confirm your script works before submitting to FSO!