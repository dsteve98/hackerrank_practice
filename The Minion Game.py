_vowel = ['A','I','U','E','O']

def split(word):
    return [char for char in word]

def minion_game(string):  ##TLE
    stuart_score = 0
    kevin_score = 0
    split_string = split(string)
    for x in range(len(string)):
        for y in range(len(string)-x):
            _verdict = split_string[x] not in _vowel
            stuart_score += _verdict
            kevin_score += not _verdict
    if(stuart_score > kevin_score):
        print("Stuart " + str(stuart_score))
    elif(stuart_score < kevin_score):
        print("Kevin " + str(kevin_score))
    else:
        print("Draw")

def minion_game(string): ##TLE, Faster
    stuart_score = 0
    kevin_score = 0
    split_string = split(string)
    is_vowel = [ele in _vowel for ele in split_string]
    kevin_score += sum(is_vowel)
    stuart_score += len(split_string) - kevin_score
    str_len = len(split_string)
    for x in range(1,str_len):
        vow_len = str_len - x
        vow_val = sum(is_vowel[:-x])
        kevin_score += vow_val
        stuart_score += vow_len - vow_val
    if(stuart_score > kevin_score):
        print("Stuart " + str(stuart_score))
    elif(stuart_score < kevin_score):
        print("Kevin " + str(kevin_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
