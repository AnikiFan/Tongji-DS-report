import os
pngs = os.listdir(os.curdir)
pngs.remove("tongji.pdf")
for png in pngs:
    print(png)
