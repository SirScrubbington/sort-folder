import sys,os

import sort_folder as sort
import random_files as rand

if __name__ == '__main__':

  # Remove the test folder
  # os.unlink('test')

  # Create the test folder
  os.mkdir('test')

  # Generate a bunch of random file names
  rand.generate('test',pow(2,8),pow(2,2))

  # Sort all of the files in the folder
  sort.sort('test')