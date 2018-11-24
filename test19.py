import cv2
import numpy as np
import math

src_img = cv2.imread('test4.png', 0)
src_height = src_img.shape[0]
src_width = src_img.shape[1]
src_pixels = src_height * src_width


temp_img = cv2.imread('test4_template.png', 0)
temp_height = temp_img.shape[0]
temp_width = temp_img.shape[1]
temp_pixels = temp_height * temp_width

src_kernel = [0] * 9
kernel_temp = [0] * 9
a_pow_kernel = [0] * 9
b_pow_kernel = [0] * 9
sum_kernel = [0] * 9
result = []
derp = []

def src(i, j):
    src_kernel[0] = src_img[i - 1, j - 1]
    src_kernel[1] = src_img[i - 1, j]
    src_kernel[2] = src_img[i - 1, j + 1]
    src_kernel[3] = src_img[i, j - 1]
    src_kernel[4] = src_img[i, j]
    src_kernel[5] = src_img[i, j + 1]
    src_kernel[6] = src_img[i + 1, j - 1]
    src_kernel[7] = src_img[i + 1, j]
    src_kernel[8] = src_img[i + 1, j + 1]

    test = src_kernel
    return test

for i in range(1, src_height -1):
    for j in range(1, src_width -1):
        a = src(i, j)
        b = src(i, j)
        a_sum = sum(a)
        a_mean = np.mean(a)

        a_pow_kernel[0] = math.pow(int(a[0]),2)
        a_pow_kernel[1] = math.pow(int(a[1]),2)
        a_pow_kernel[2] = math.pow(int(a[2]),2)
        a_pow_kernel[3] = math.pow(int(a[3]),2)
        a_pow_kernel[4] = math.pow(int(a[4]),2)
        a_pow_kernel[5] = math.pow(int(a[5]),2)
        a_pow_kernel[6] = math.pow(int(a[6]),2)
        a_pow_kernel[7] = math.pow(int(a[7]),2)
        a_pow_kernel[8] = math.pow(int(a[8]),2)

        aa_pow_kernel = a_pow_kernel
        a_pow_sum = sum(aa_pow_kernel)

        b_sum = sum(b)
        b_mean = np.mean(b)

        b_pow_kernel[0] = math.pow(int(b[0]), 2)
        b_pow_kernel[1] = math.pow(int(b[1]), 2)
        b_pow_kernel[2] = math.pow(int(b[2]), 2)
        b_pow_kernel[3] = math.pow(int(b[3]), 2)
        b_pow_kernel[4] = math.pow(int(b[4]), 2)
        b_pow_kernel[5] = math.pow(int(b[5]), 2)
        b_pow_kernel[6] = math.pow(int(b[6]), 2)
        b_pow_kernel[7] = math.pow(int(b[7]), 2)
        b_pow_kernel[8] = math.pow(int(b[8]), 2)

        bb_pow_kernel = b_pow_kernel
        b_pow_sum = sum(bb_pow_kernel)

        sum_kernel[0] = int(a[0]) * int(b[0])  # Need to typecast to int otherwise python cannot multiply!
        sum_kernel[1] = int(a[1]) * int(b[0])
        sum_kernel[2] = int(a[2]) * int(b[2])
        sum_kernel[3] = int(a[3]) * int(b[3])
        sum_kernel[4] = int(a[4]) * int(b[4])
        sum_kernel[5] = int(a[5]) * int(b[5])
        sum_kernel[6] = int(a[6]) * int(b[6])
        sum_kernel[7] = int(a[7]) * int(b[7])
        sum_kernel[8] = int(a[8]) * int(b[8])

        pix_sum = abs(sum(sum_kernel))
        math_pows = math.sqrt(a_pow_sum * b_pow_sum)
        result = pix_sum / math_pows

        if result > 1:
            result = 1.0

        threshold = 0.999
        if result > threshold:
            res = (i,j)
            derp.append(res)
            print('res', derp)





cv2.imshow('test', src_img)
cv2.waitKey()





def temp(i,j):
        kernel_temp[0] = temp_img[k - 1, l - 1]
        kernel_temp[1] = temp_img[k - 1, l]
        kernel_temp[2] = temp_img[k - 1, l + 1]
        kernel_temp[3] = temp_img[k, l - 1]
        kernel_temp[4] = temp_img[k, l]
        kernel_temp[5] = temp_img[k, l + 1]
        kernel_temp[6] = temp_img[k + 1, l - 1]
        kernel_temp[7] = temp_img[k + 1, l]
        kernel_temp[8] = temp_img[k + 1, l + 1]

        test2 = kernel_temp
        print('test2',test2)
        return test2
