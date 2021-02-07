
import os
import glob
import shutil
original_dir = "data_/train"
des_dir = "data/train"
sample = 50
imgnames = os.listdir(os.path.join(original_dir, "imgs"))[:sample]
masknames = [x.replace(".jpg", "_mask.gif") for x in imgnames]
for imgname in imgnames:
    imgpath = os.path.join(original_dir, "imgs", imgname)
    maskname = imgname.replace(".jpg", "_mask.gif")
    maskpath = os.path.join(original_dir, "masks", maskname)
    new_imgpath = os.path.join(des_dir, "imgs", imgname)
    new_maskpath = os.path.join(des_dir, "masks", maskname)
    shutil.copyfile(imgpath, new_imgpath)
    shutil.copyfile(maskpath, new_maskpath)













