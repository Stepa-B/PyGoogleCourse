import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return ""
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)