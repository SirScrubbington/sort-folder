import sys, os, random

import string

# Make a new file
def touch(path):

  # If the path exists
  if os.path.exists(path):

    # Idk what this does
    os.utime(path,None)

  # File does not exist
  else:

    # Create a new file then close it
    open(path,'a').close()

def generate(path, items, length):

  # Iterate over the number of items to create
  for i in range(items):

    # Generate a random sequence of characters
    rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

    # Create a file at the given path and file name
    touch(path + '/' + rand)



if __name__ == '__main__':

  # Empty argument variables
  path = items = length = None

  # Argument 1: Path
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = '.'

  # Argument 2: No. of items
  if len(sys.argv) > 2:
    items = sys.argv[2]
  else:
    items = 30

  # Argument 3: No. of length
  if len(sys.argv) > 3:
    length = sys.argv[3]
  else:
    length = 8

  # Perform the generate function
  generate(path,items,length)