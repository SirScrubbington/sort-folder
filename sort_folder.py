# Require the system libraries for OS calls, sys.argv
import sys,os

# Require shutil for moving files around (as sh for simplicity)
import shutil as sh

def sort(base):

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

      # Create an array storing the matches
      match = [0] * len(active)

      # Loop over the length of the item
      for depth in range(len(active)):

        # No previous matches
        if depth > bdep and match[depth-1] == 0:

          # Not possible for more matches
          break

        # Loop over the remaining items
        for item in files:

          # If the current item starts with the current substring
          if item.startswith(active[:depth + 1]):

            # Increment the match depth
            match[depth] += 1

      # Common Value
      cv = match[bdep]
    
      # Common Depth
      cd = bdep

      # If there are no matches
      if not cv:

        # Not possible for mores matches
        continue

      # Iterate over matches
      # Can skip the first value as we have
      # already captured that
      for m in range(len(match)):

        # If there are the same number of 
        # matches as the previous level
        if cv == match[m]:

          # Update the common depth
          cd = m
          
        else: # There are not the same matches

          # No need to continue
          break

      # Generate the new folder path
      newpath = path + '/' + active[:cd + 1]

      # Attempt to create a new directory

      # If the new path does not already exist
      if not os.path.exists(newpath):

        try:

          # Try to create it
          os.mkdir(newpath)

        except Exception as e:

          pass

      # Track the number of items that have been moved
      moved = 0

      # Loop over items in the directory again
      # Keeping in mind there is now an additional item,
      # the folder just created which will not show up in
      # this array
      for item in files:

        if item.startswith(active[:cd + 1]):

          # Move the file to the new folder
          sh.move(path + '/' + item, newpath + '/' + item)

          # Increment the number of items that have been moved
          moved += 1

        # Stop looping over and break out of the function
        cont = False

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