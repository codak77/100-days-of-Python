#y=0
#n=0
picture = 0
#is_picture = input("0 or 1 ")
is_picture = int(input("0 or 1 "))
#if is_picture == y: #invalid because y is not defined
if is_picture == 0:
  picture = 1
  picture_bool = bool(picture)
  print(picture_bool)
else:
  picture = 0
  picture_bool = bool(picture)
  print(picture_bool)
#picture_bool = bool(picture)
#print(is_picture)
