my_word_list = ['east', 'after', 'up', 'over', 'inside',10]

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_word_list))