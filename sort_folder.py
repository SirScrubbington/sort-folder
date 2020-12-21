# Require the system libraries for OS calls, sys.argv
import sys,os

# Require shutil for moving files around (as sh for simplicity)
import shutil as sh

def sort(base):

  print('Starting to sort folder "' + str(base) + ' ..."')

  # Stack of folders to iterate over
  stack = []

  # Append the base folder to the stack
  stack.append([base,0])

  # While there are folders left to parse
  while(len(stack)):

    # Pop the top element off the stack
    pop = stack.pop()

    # Dereference the stack elements
    path = pop[0]
    bdep = pop[1]

    print('Working on folder "' + str(path) + '"')

    # Retrieve all of the items in the folder
    items = os.listdir(path)

    # Array which will store all of the files,
    # excluding folders
    files = []

    # Iterate over all of the items in the folder
    for item in items:

      # If the item is not a directory
      if os.path.isfile(path + '/' + item):

        # Add it to the files list
        files.append(item)

    print('Folder items retrieved...')

    print('Items: "' + str(len(items)) + '",Files: "' + str(len(files)) + '" ...')

    # If this is true, we've made changes to the folder and need to refresh
    # Otherwise, no changes have been made and we should keep looping over
    cont = True

    # While the continue flag is set
    while cont:

      # If there are no files in the path
      if not files:

        # Exit out of the loop
        break

      # Take the back item from the list as the active item (removes it)
      active = files.pop()

      print('Active item selected: "' + str(active) + '"')

      print('Remaining Files: "' + str(files) + '"')

      # Create an array storing the matches
      match = [0] * len(active)

      print('Starting depth loop ... Max Depth: "' + str(len(match)) + '"')
    
      # Loop over the length of the item
      for depth in range(len(active)):

        print('Current Depth: "' + str(depth) + '"')
    
        # No previous matches
        if depth > bdep and match[depth-1] == 0:
      
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
      cv = match[bdep]
    
      # Common Depth
      cd = bdep

      print('Common Value: "' + str(cv) + '", Common Depth: "' + str(cd) + '"')
    
      # If there are no matches
      if not cv:

        print('No matches, breaking ...')

        # Not possible for mores matches
        continue

      print('Iterate over matches ...')

      # Iterate over matches
      # Can skip the first value as we have
      # already captured that
      for m in range(len(match)):
      
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

      # Track the number of items that have been moved
      moved = 0

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

          # Increment the number of items that have been moved
          moved += 1

      # If any files have been moved
      if moved:

        print('No. of Files Moved: "' + str(moved) + '", Adding new paths to the stack ...')

        # Move the filter item to the folder
        sh.move(path + '/' + active, newpath + '/' + active)

        print('Moving the reference file "' + active + '" to "' + newpath + '" ...')

        # Add the current folder to the stack
        stack.append([path,bdep])

        print('Added the current path "' + path + '" back to the stack ...')

        # Add the new folder to the stack
        stack.append([newpath, bdep + 1])

        print('Added the new path "' + newpath + '" to the stack ...')

        # Stop looping over and break out of the function
        cont = False

      else: # No files moved
          
        # Otherwise, don't work on this folder again
        print('No files moved! Not adding new paths to the stack.')

        # Keep looping over

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
    sort(base)