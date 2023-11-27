
#dictionary
youtubers = {
  "hikakinn" : 1000,
  "nakata" : 440
}

youtubers["shirasu"] = 160


youtubers["hikakinn"] = 1100

youtubers.update({"mimi" : 100, "jake":150})
# print(youtubers)

# for key,value in youtubers.items():
# #  print(str(key) + " : " + str(value))


#set
# m_students = {"miyako","yasuda","suzuki","honey"}

# j_students = {"John","Mary","Prue","Simon","yasuda"}

# print(m_students & j_students)

# fav_youtubers = ["naja","nakagawake"]
# for name in fav_youtubers:
#  print(name)


fav_youtubers = {"naja" : 40,"nakagawake" : 50}
for name, age in youtubers.items():
 print(str(name) + " : " + str(age))