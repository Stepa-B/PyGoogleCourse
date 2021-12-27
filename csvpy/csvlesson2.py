import os
import csv
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file
    rows = csv.reader(file, delimiter=',')
    # Process each row
    line_count = 0
    for row in rows:
      if line_count==0:
        line_count += 1
      else:
      # Format the return string for data rows only
        line_count += 1
        return_string += "a {} {} is {}\n".format(row[0],row[1],row[2],)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))