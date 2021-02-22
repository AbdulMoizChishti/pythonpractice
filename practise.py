name = "abdulmoiz"
vowel=0
consonants=0
space=0
for i in range(0,len(name)):
    if name[i]== 'a'or name[i]== 'e'or name[i]== 'i'or name[i]== 'o'or name[i]== 'u':
        vowel+=1
    elif name[i]=='':
        space +=1
    else:
        consonants+=1

print(vowel)
print(consonants)
print(space)