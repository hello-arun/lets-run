# https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/
# I could not thing of a better solution as given on github so I am just using that
def printKeypadCode(string,codes):
    string=string.upper()
    seq=""
    for char in string:
        if char==" ":
            seq+="0"
        else:
            seq+=codes[ord(char)-65]
    print(seq)
    return seq

codes = [
    "2","22","222",
    "3","33","333",
    "4","44","444",
    "5","55","555",
    "6","66","666",
    "7","77","777","7777",
    "8","88","888",
    "9","99","999","9999"]

printKeypadCode("ARUN jangir",codes)