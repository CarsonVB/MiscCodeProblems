def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return False
    string1_c = {}
    string2_c = {}
    for letter in string1:
        if letter.lower() in string1_c:
            string1_c[letter.lower()] += 1
        else:
            string1_c[letter.lower()] = 0
    for letter in string2:
        if letter.lower() in string2_c:
            string2_c[letter.lower()] += 1
        else:
            string2_c[letter.lower()] = 0
    if string1_c == string2_c:
        return True
    else:
        return False


str1 = input('Please enter the first string to compare: ')
str2 = input('Please enter the second string to compare: ')

if compare_strings(str1, str2):
    print('They are anagrams!')
else:
    print('They are not anagrams!')
