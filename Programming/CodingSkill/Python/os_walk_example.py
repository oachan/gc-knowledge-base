import os

root = "/python/demo/"
for dpath, dnames, fnames in os.walk(root):
    print(dpath)
    for fname in fnames:
        print(os.path.join(dpath, fname))
