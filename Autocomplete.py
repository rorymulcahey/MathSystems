'''

Autocomplete: string[] GetSuggestions(string[] corpus, string prefix)
Given some corpus of words (eg. ['cat','carrot','dog',...]).
Give a function that gives an array of suggestions based on the prefix.
For example, 'ca' would give cat and carrot.

'''


#lst must contain characters
def auto_complete(lst, prefix):
    output = []
    for x in range(0, len(lst)):
        same_letters = True
        index = 0
        while same_letters and index < len(prefix):
            if lst[x][index] != prefix[index]:
                same_letters = False
            index += 1
        if same_letters:
            output.append(lst[x])
    return output


print(auto_complete(['cat', 'carrot', 'dog'], 'd'))


