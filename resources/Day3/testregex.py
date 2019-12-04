import re
pattern = '[^\/]*$'
# regex = re.compile('[^\/]*$')
fullpath = "resources/Day3/mushroom.png"
regexObj = re.search(pattern,fullpath)
print(regexObj[0])
