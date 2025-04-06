from imutils import paths
import argparse
import cv2
import os
import sys
from collections import defaultdict

def dhash(image, hashSize=8):
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
                help="Folder containing images to check for duplicates")
args = vars(ap.parse_args())

imagePaths = list(paths.list_images(args["folder"]))

# # Optional cleanup for non-Windows paths
# if sys.platform != "win32":
#     imagePaths = [p.replace("\\", "") for p in imagePaths]

hash_dict = defaultdict(list)

print("[INFO] Processing images and computing hashes...")
for path in imagePaths:
    image = cv2.imread(path)
    if image is None:
        continue
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h = dhash(gray)
    hash_dict[h].append(path)

# Display duplicates
print("\n[INFO] Duplicate Images Found:")
found = False
for h, paths in hash_dict.items():
    if len(paths) > 1:
        found = True
        print(f"\nHash: {h}")
        for p in paths:
            print(f" - {p}")
if not found:
    print("[INFO] No duplicates found.")
