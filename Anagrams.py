'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

str1="lissten"
str2="silsent"

print(set(str1))
print(set(str2))
if set(str1)==set(str2) and len(str1)==len(str2):
    print("Anagrams")
else:
    print("Not")

#Another Solution

# if(sorted(str1)==sorted(str2)):
#     print("Anagrams")
# else:
#     print("Not")

# Another Solution:

# str1="listen"
# str2="sikent"
#
# if(not len(str1)==len(str2)):
#     print("Not Anagrams")
# else:
#     flag=False
#     d1=dict()
#     d2=dict()
#     for i in range(len(str1)):
#         d1[str1[i]]=d1.get(str1[i],0)+1
#         d2[str2[i]]=d2.get(str2[i],0)+1
#
#     sorted(d1)
#     sorted(d2)
#     if(len(d1)==len(d2)):
#         for key,value in d1.items():
#             if(d1.get(key)==d2.get(key)):
#                 flag=True
#             else:
#                 flag=False
#                 print("Not Anagrams")
#                 break
#     else:
#         print("Not Anagrams")
#         pass
#     if(flag is True):
#         print("Anagrams")
