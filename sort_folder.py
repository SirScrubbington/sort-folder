# Require the system libraries for OS calls, sys.argv
import sys,os

# Require shutil for moving files around (as sh for simplicity)
import shutil as sh

def sort_folder(base):

  print('Starting to sort folder "' + str(base) + ' ..."')

  # Stack of folders to iterate over
  stack = []

  # Append the base folder to the stack
  stack.append(base)

  while(len(stack)):

    # Pop the top element off the stack
    path = stack.pop()

    print('Working on folder "' + str(path) + '"')

    # Retrieve all of the items in the folder
    items = os.listdir(path)

    # Array which will store all of the files,
    # excluding folders
    files = []

    # Iterate over all of the items in the folder
    for item in items:

      # If the item is not a directory
      if not os.path.isdir(item):

        # Add it to the files list
        files.append(item)

    print('Folder items retrieved...')
  
    # Take the back item from the list as the active item (removes it)
    active = files.pop()

    print('Active item selected: "' + str(active) + '"')

    # Create an array storing the matches
    match = [0] * len(active)

    print('Starting depth loop ... Max Depth: "' + str(len(match)) + '"')
  
    # Loop over the length of the item
    for depth in range(len(active)):

      print('Current Depth: "' + str(depth) + '"')
  
      # No previous matches
      if depth and match[depth-1] == 0:
    
        print('Previous depth had no matches: Breaking ...')

        # Not possible for more matches
        break
  
      print('Checking for matches ...')

      # Loop over the remaining items
      for item in files:

        # If the current item starts with the current substring
        if item.startswith(active[:depth + 1]):

          print('Match found: "' + str(item) + '" matches "' + str(active) + '" filter: "' + str(active[:depth + 1]) + '"')

          # Increment the match depth
          match[depth] += 1

    print('Matches: "' + str(match) + '"')

    # Common Value
    cv = match[0]
  
    # Common Depth
    cd = 0

    print('Common Value: "' + str(cv) + '", Common Depth: "' + str(cd) + '"')
   
    print('Iterate over matches ...')

    # Iterate over matches
    # Can skip the first value as we have
    # already captured that
    for m in range(1,len(match)):
  
      print('Checking Match at Range "' + str(m) + '" ...')

      # If there are the same number of 
      # matches as the previous level
      if cv == match[m]:
    
        print('Same number of matches as the previous level, updating common depth ...')

        # Update the common depth
        cd = m
      
      else: # There are not the same matches
    
        print('Matches are not the same, breaking out of the loop ...')

        # No need to continue
        break

    # Generate the new folder path
    newpath = path + '/' + active[:cd + 1]
      
    print('New folder path: "' + newpath + '"')

    # Attempt to create a new directory
    
    print('Attempting to create directory ...')

    # If the new path does not already exist
    if not os.path.exists(newpath):

      print('Path "' + newpath + '" does not exist, creating path ...')

      try:

        # Try to create it
        os.mkdir(newpath)

        print('Path "' + newpath + '" has been created.')

      except Exception as e:

        # Failed to create it, output error
        print('Failed to create path, reason:',e)

    else: # Already exists

      # Attempt to skip
      print('Path "' + newpath + '" already exists, skipping ...')

    print('Checking for files that fit match: "' + active[:cd + 1] + '"')

    # Loop over items in the directory again
    # Keeping in mind there is now an additional item,
    # the folder just created which will not show up in
    # this array
    for item in files:

      # If the item matches the search string
      print('Checking file: "' + item + '" ...')

      if item.startswith(active[:cd + 1]):
        
        print('Matched file: "',item,'", moving ...')
    
        # Move the file to the new folder
        sh.move(path + '/' + item, newpath + '/' + item)

    """
    # Add the new folder to the stack
    stack.append(newpath)
    """

# If we are running the script
if __name__ == '__main__':

  # If there are at LEAST two arguments to the function
  # (The first argument is always the script / fn name)
  if len(sys.argv) >= 2:
  
    # Set the base path array to be the arguments minus the first entry
    bases = sys.argv[1:]
    
  # No arguments provided
  else:
  
    # Set the base path array to contain the current directory
    bases = [os.getcwd()]

  # Iterate over all of the base folders
  for base in bases:
    
    # Run the sort function on the base folder
    sort_folder(base)    