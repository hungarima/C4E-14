#create: append
#read: print, indexing
#update: indexing
#delete: pop

print("Hi there, here is my favourite things so far:")
favs = ["movie", 99, "guitar"]
#for i, fav in enumerate(favs):
    #print(i + 1, fav, sep=".")
for i in range(len(favs)):
    print(i+1, favs[i],sep=". ")
# for item in favs:
#     print(item)

fav = input("Favourite stuff you want to get rid of?")
# replace = input("Your replacing favourite?")
# favs[update - 1]=replace
# favs.pop(remove-1)
if fav in favs: #Not in
    favs.remove(fav)
    for i in range(len(favs)):
        print(i+1, favs[i], sep=". ")
else:
    print("Not found")


# # menu = ['com', 'kem', 'keo', 'baron']
# # # # print[-1] #baron
# # # print(len(menu))
# #
# # for i in range(len(menu)):
# #     print(menu[i])
#
# menu.pop(2)
# print(*menu)
# del menu[0]
# print(*menu)
