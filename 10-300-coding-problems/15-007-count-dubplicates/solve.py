# Not so useful you can just skip
# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
#
def countDubplicates(string):
    string=string.upper()
    dict={}
    for c in string:
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1
    print(dict)
    return dict

countDubplicates("GeekForGeeks")
    