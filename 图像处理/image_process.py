#coding=utf-8
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
"""
opencv中opencv不接受non-ascii的路径，
解决方法就是先用先用np.fromfile()读取为np.uint8格式，再使用cv2.imdecode()解码
"""
# img1 = cv2.imdecode(np.fromfile(os.path.join("D:/git/图像处理/","img1.jpg"),dtype=np.uint8),-1)
"""
原图像的灰度直方图
"""
def gray_level(img_dir):
    img1 = cv2.imread(img_dir)
    img_ori = img1[:, :, 0]
    plt.imshow(img_ori)
    result = {}
    for i in img_ori.flatten().tolist():
        if i not in result.keys():
            result[i] = 0
        result[i] = img_ori.flatten().tolist().count(i) / (img_ori.shape[0]*img_ori.shape[1])
    # result={11: 0.0001, 12: 0.0003, 13: 0.0003, 14: 0.0003, 15: 0.0003, 16: 0.0002, 17: 0.0008, 18: 0.0012, 19: 0.0006, 20: 0.001, 21: 0.0015, 22: 0.0012, 23: 0.0013, 24: 0.0022, 25: 0.0022, 26: 0.0021, 27: 0.0025, 28: 0.0028, 29: 0.0031, 30: 0.003, 31: 0.0039, 32: 0.0035, 33: 0.0035, 34: 0.0033, 35: 0.0043, 36: 0.0027, 37: 0.0043, 38: 0.0048, 39: 0.0035, 40: 0.0036, 41: 0.0038, 42: 0.0042, 43: 0.0055, 44: 0.004, 45: 0.0047, 46: 0.0067, 47: 0.0035, 48: 0.0039, 49: 0.0035, 50: 0.0039, 51: 0.003, 52: 0.003, 53: 0.0033, 54: 0.0019, 55: 0.0022, 56: 0.002, 57: 0.0024, 58: 0.0022, 59: 0.0024, 60: 0.0025, 61: 0.0023, 62: 0.0021, 63: 0.0025, 64: 0.0021, 65: 0.0024, 66: 0.0027, 67: 0.0022, 68: 0.0044, 69: 0.0053, 70: 0.0044, 71: 0.0042, 72: 0.0045, 73: 0.0059, 74: 0.0044, 75: 0.004, 76: 0.0044, 77: 0.0039, 78: 0.005, 79: 0.0045, 80: 0.0058, 81: 0.0047, 82: 0.0058, 83: 0.0048, 84: 0.0051, 85: 0.0065, 86: 0.0065, 87: 0.0047, 88: 0.0075, 89: 0.0069, 90: 0.0063, 91: 0.008, 92: 0.0068, 93: 0.0077, 94: 0.0082, 95: 0.0086, 96: 0.0065, 97: 0.0068, 98: 0.0073, 99: 0.0082, 100: 0.0063, 101: 0.0057, 102: 0.008, 103: 0.0061, 104: 0.0084, 105: 0.0079, 106: 0.0078, 107: 0.0078, 108: 0.0094, 109: 0.0062, 110: 0.0094, 111: 0.0085, 112: 0.0088, 113: 0.0074, 114: 0.0067, 115: 0.0085, 116: 0.0086, 117: 0.0081, 118: 0.0089, 119: 0.0081, 120: 0.0118, 121: 0.0093, 122: 0.0093, 123: 0.0108, 124: 0.0113, 125: 0.0108, 126: 0.0109, 127: 0.0097, 128: 0.0105, 129: 0.0118, 130: 0.0092, 131: 0.0107, 132: 0.0104, 133: 0.0089, 134: 0.0093, 135: 0.0089, 136: 0.0111, 137: 0.0105, 138: 0.0073, 139: 0.0104, 140: 0.0077, 141: 0.0086, 142: 0.009, 143: 0.0091, 144: 0.0077, 145: 0.0072, 146: 0.0072, 147: 0.0076, 148: 0.0106, 149: 0.0096, 150: 0.0084, 151: 0.0124, 152: 0.0096, 153: 0.0083, 154: 0.0074, 155: 0.0075, 156: 0.0061, 157: 0.0063, 158: 0.0059, 159: 0.0052, 160: 0.0052, 161: 0.0048, 162: 0.0054, 163: 0.0044, 164: 0.005, 165: 0.004, 166: 0.0058, 167: 0.0037, 168: 0.0051, 169: 0.0047, 170: 0.0031, 171: 0.0035, 172: 0.0039, 173: 0.0028, 174: 0.0039, 175: 0.0025, 176: 0.0031, 177: 0.0033, 178: 0.0028, 179: 0.0021, 180: 0.0026, 181: 0.0018, 182: 0.0019, 183: 0.0024, 184: 0.0025, 185: 0.0018, 186: 0.0024, 187: 0.002, 188: 0.0016, 189: 0.0009, 190: 0.0018, 191: 0.0012, 192: 0.0005, 193: 0.0007, 194: 0.0009, 195: 0.001, 196: 0.0007, 197: 0.0011, 198: 0.0012, 199: 0.0013, 200: 0.0003, 201: 0.0006, 202: 0.0005, 203: 0.0005, 204: 0.001, 205: 0.0004, 206: 0.0003, 207: 0.0003, 208: 0.0002, 209: 0.0002, 210: 0.0001, 211: 0.0006, 212: 0.0003, 213: 0.0002, 214: 0.0004, 215: 0.0006, 216: 0.0001, 217: 0.0002, 218: 0.0002, 219: 0.0003, 220: 0.0002, 221: 0.0003, 222: 0.0002, 223: 0.0001, 224: 0.0005, 225: 0.0004, 226: 0.0001, 228: 0.0004, 229: 0.0003, 230: 0.0001, 231: 0.0004, 233: 0.0001, 234: 0.0003, 235: 0.0003, 236: 0.0001, 239: 0.0003, 240: 0.0006, 241: 0.0003, 242: 0.0003, 243: 0.0003, 244: 0.0004, 245: 0.0002, 246: 0.0005, 247: 0.0003, 248: 0.0002, 249: 0.0001, 250: 0.0007, 251: 0.0001, 252: 0.0006, 253: 0.0005, 254: 0.0038, 255: 0.0125}
    print(result,sum(result.values()))
    plt.bar(result.keys(),result.values())
    plt.title("original image")
    plt.figure()
    hist = cv2.calcHist([img1],[0],None,[256],[0,255])  #元组，使用opencv自带函数得到灰度直方图
    # print(np.array(hist).shape)#(256,1)
    plt.bar(range(len(hist)),np.array(hist).flatten()/(100*100))
    plt.show()

"""
直方图均衡化
假如图像的灰度分布不均匀，其灰度分布集中在较窄的范围内，使图像的细节不够清晰，对比度较低。
通常采用直方图均衡化及直方图规定化两种变换，使图像的灰度范围拉开或使灰度均匀分布，从而增大反差，使图像细节清晰，以达到增强的目的。
直方图均衡化，对图像进行非线性拉伸，重新分配图像的灰度值，使一定范围内图像的灰度值大致相等。
这样，原来直方图中间的峰值部分对比度得到增强，而两侧的谷底部分对比度降低，输出图像的直方图是一个较为平坦的直方图
"""
def histogram_equalization(img_dir):
    img1 = cv2.imread(img_dir)
    img_ori = img1[:, :, 0]
    img_new = cv2.equalizeHist(img_ori)
    plt.figure()
    plt.imshow(img_new)
    plt.figure()
    hist = cv2.calcHist([img_new],[0],None,[256],[0,255])  #元组
    plt.bar(range(len(hist)),np.array(hist).flatten()/(100*100))
    plt.show()
"""
二维高斯函数图像绘制
"""
def plt_Gussian():
    deta=3
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x=np.arange(-10,10,0.1)
    y=np.arange(-10,10,0.1)
    x,y=np.meshgrid(x,y)
    z=(1/(2*np.pi*deta**2))*np.exp(-(x**2+y**2)/(2*deta**2))
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # ax.set_zlim(-1.01, 1.01)  # 坐标系的下边界和上边界
    # ax.zaxis.set_major_locator(LinearLocator(10))  # 设置Z轴标度
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # Z轴精度
    # fig.colorbar(surf, shrink=0.5, aspect=5)  # shrink颜色条伸缩比例（0-1），aspect颜色条宽度（反比例，数值越大宽度越窄）
    plt.show()


"""
椒盐噪声
"""
def addsalt_pepper(img, SNR):
    img_ = img.copy()
    h, w, c = img_.shape

    mask = np.random.choice((0, 1, 2), size=(h, w, 1), p=[SNR, (1 - SNR) / 2., (1 - SNR) / 2.])
    mask = np.repeat(mask, c, axis=2)     # 按channel 复制到 与img具有相同的shape
    img_[mask == 1] = 255    # 盐噪声
    img_[mask == 2] = 0      # 椒噪声
    return img_

"""
图像平滑(模板)
"""
def mean_filtering(img,filter):
    img_ = np.zeros((img.shape[0]-2,img.shape[1]-2,img.shape[2]))
    for c in range(img_.shape[2]):
        for h in range(img_.shape[0]):
            for w in range(img_.shape[1]):
                img_[h,w,c] = np.sum(img[h:h+3,w:w+3,c]*filter)
    img_ = img_.astype(dtype=np.uint8)
    return img_


if __name__ == "__main__":
    img1 = cv2.imdecode(np.fromfile(os.path.join("D:/git/图像处理/","img1.jpg"),dtype=np.uint8),-1)
    img1 = img1[150:250,150:250,:]
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # img2 = addsalt_pepper(img1,0.8)
    img2 = mean_filtering(img1,filter)
    cv2.imshow("image",img1)
    cv2.imshow("image1",img2)
    filter1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    img3 = mean_filtering(img1,filter1)
    cv2.imshow("image2",img3)
    cv2.waitKey()
    # print(img1.shape)  #(297,396,3)
    # img1_noise = addsalt_pepper(img1,0.1)
    #
    # cv2.imshow("image_noise",img1_noise)
    #plt_Gussian()
