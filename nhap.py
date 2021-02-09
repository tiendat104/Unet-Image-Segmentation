
import os
import glob
import shutil
import cv2
import matplotlib.pyplot as plt
def transfer():
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


def visualize():
    imgpath = "data/test/6a951d3a3131_03.jpg"
    predicted_imgpath = "predicted_imgs/6a951d3a3131_03.jpg"
    img = cv2.imread(imgpath)
    predicted = cv2.imread(predicted_imgpath)
    images = [img, predicted]

    fig = plt.figure(figsize=(8,4))
    columns = 2
    rows = 1

    ax = []
    ax.append(fig.add_subplot(rows, columns, 1))
    ax[-1].set_title('original image')
    plt.imshow(img)
    plt.axis('off')
    ax.append(fig.add_subplot(rows, columns, 2))
    ax[-1].set_title('segmentation')
    plt.imshow(predicted)
    plt.axis('off')
    #plt.show()
    plt.savefig("assets/visualize.png")

def resize_img():
    img = cv2.imread("assets/model.png")
    # 560
    img = cv2.resize(img,(800,560))
    cv2.imwrite("1.png", img)
resize_img()

















