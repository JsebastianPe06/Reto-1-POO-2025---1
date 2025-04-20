#This function checks if two strings have the same characters
def same_characters(string1, string2):
    if(len(string1)!=len(string2)):
        return False
    cop1 = list(string1)
    cop2 = list(string2)
    for char in cop1:
        if char in cop2:
            cop2.remove(char)
        else:
            return False
    return True

#This function forms groups of strings with the same characters into a list
def groups_same_characters(lis):
    s = lis.copy()
    new_list = []
    while(len(s)!=0):
        group = [s[0]]
        for i in range(1,len(s)):
            if(same_characters(s[0], s[i])):
                group.append(s[i])
        new_list.append(group)
        for i in group:
            s.remove(i)
    return new_list

#This function removes sublists from a list that contain only one element
def keep_groups(lis):
    t = len(lis)
    i = 0
    while(i < t):
        if(len(lis[i])==1):
            lis.remove(lis[i])
            t -= 1
        else:
            i += 1
    return lis 

list_strings = ["roma", "amor", "perro", "uno", "onu", "nou", "sol", "los"]
formed_groups = keep_groups(groups_same_characters(list_strings))
for i in range(len(formed_groups)):
    print(formed_groups[i])