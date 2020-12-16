# Require the system libraries for OS calls, sys.argv
import sys,os

# Require shutil for moving files around (as sh for simplicity)
import shutil as sh

def sort_folder(path):

  # Retrieve all of the items in the folder
  items = os.listdir(path)
  
  # If folder is empty
  if not items:
  
    # Break out
    return
  
  # Take the back item from the list as the active item (removes it)
  active = items.pop()
  
  match = [0] * len(active)
  
  # Loop over the length of the item
  for depth in range(len(active)):
  
    # No previous matches
    if depth and match[depth-1] == 0:
    
      # Not possible for more matches
      break
  
    # Loop over the remaining items
    for item in items:
    
      # If the current item starts with the current substring
      if item.startswith(active[:depth + 1]):

        # Increment the match depth
        match[depth] += 1

  # Common Value
  cv = match[0]
  
  # Common Depth
  cd = 0
  
  # If there are no matches
  if not cv:
  
    # Break out
    return
   
  # Iterate over matches
  # Can skip the first value as we have
  # already captured that
  for m in range(1,len(match)):
  
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
  try:
    os.mkdir(newpath)
  except Exception as e:
    print('Failed to create path, reason:',e)
    
  # Loop over items in the directory again
  # Keeping in mind there is now an additional item,
  # the folder just created which will not show up in
  # this array
  for item in items:
  
    # If the item matches the search string
    print(item,active[:cd + 1])
    
    # If they are a perfect match
    if not item == active[:cd + 1] and item.startswith(active[:cd + 1]):
    
      print('moving item "',item,'" ...')
    
      # Move the file to the new folder
      sh.move(path + '/' + item, newpath + '/' + item)
      
  # Run the algorithm on the new folder
  sort_folder(newpath)
    
  # Run the algorithm on the current folder again
  sort_folder(path)
    
  # Break out
  return

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