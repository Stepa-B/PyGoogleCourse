import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  #print(os.curdir)
  os.chdir('..')
  #print(os.curdir)

  # Return the absolute path of the parent directory
  return os.path.abspath(os.curdir)

print(parent_directory())