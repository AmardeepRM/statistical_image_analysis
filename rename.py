import os
folder = "data"
lst = os.listdir(folder)

for idx,item in enumerate(lst):
    src = os.path.join(folder,item)
    dst = os.path.join(folder,f"img_{idx}.jpg")
    os.rename(src,dst)
    print(f"current name: {src} and new name: image_{dst}.jpg")



