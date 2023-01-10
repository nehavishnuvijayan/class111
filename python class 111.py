import os
import shutil
from_dir="D:/Redmi Photos/IMG_20170328_084531.JPG"
to_dir="D:/"
result=shutil.move(from_dir,to_dir)
s=os.listdir(from_dir)
print(s)
root1,extension1=os.path.splitext("D:/Redmi Photos/IMG_20170328_084531.JPG")
print(root1)
print(extension1)

'''
import os
import shutil
# print(dir(os))
os.getcwd()
#os.mkdir("Neha")
#path=os.listdir("C:/Users/User/Downloads")
#print (path)
#path=os.path.exists("C:/Users/User/Downloads")
#print(path)
img=os.path.exists("D:/folder/image.png")
root,extension=os.path.splitext("D:/folder/image.png")
print("The root of the image is",root)
print("The extension of the image is",extension)
source="D:/folder/CropImage.JPG"
destination="D:/abc"
result=shutil.move(source,destination)
'''