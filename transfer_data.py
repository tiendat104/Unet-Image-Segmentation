
import os
import glob
from random import shuffle
def old_to_new(old_folder = "data/train_", new_folder= "data/train", num_img_limit = 500):
    # data/train_pre/imgs/0cdf5b5d0ce1_01.jpg
    # data/train_pre/masks/0cdf5b5d0ce1_01_mask.gif
    os.makedirs(os.path.join(new_folder, "imgs"), exist_ok=True)
    os.makedirs(os.path.join(new_folder, "masks"), exist_ok=True)

    img_names = os.listdir(os.path.join(old_folder, "imgs"))
    shuffle(img_names)
    img_names = img_names[:num_img_limit]
    for img_name in img_names:
        id_img = img_name.split(".")[0]
        mask_name = id_img + "_mask.gif"
        old_img_path = os.path.join(old_folder, "imgs", img_name)
        old_mask_path = os.path.join(old_folder, "masks", mask_name)

        new_img_path = os.path.join(new_folder, "imgs", img_name)
        new_mask_path = os.path.join(new_folder, "masks", mask_name)
        os.rename(old_img_path, new_img_path)
        os.rename(old_mask_path, new_mask_path)

old_to_new(num_img_limit=200)
















































