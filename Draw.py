# Given any three points and an image
# Draw a solid and a dotted line and also an angle on the image and save it
import numpy as np
import cv2
import pandas as pd
import math
import os


def proj_point(p, line):  # projection of point p onto line
    a_x = line[0][0]
    a_y = line[0][1]
    b_x = line[1][0]
    b_y = line[1][1]

    v = np.array([b_x - a_x, b_y - a_y])
    # line = np.array(line)
    u = np.array([p[0] - a_x, p[1] - a_y])
    # u = p
    proj = (np.dot(u, v) / (np.linalg.norm(v) ** 2)) * v

    proj = proj.tolist()
    proj[0] = proj[0] + a_x
    proj[1] = proj[1] + a_y
    # m = (a_y-b_y)/(a_x-b_x)
    # k = a_y - m*a_x

    # ceta = math.atan(m)

    # p2 = [0,p[0]+p[1]* math.cos(ceta)]

    # proj_p = cutting_point([p,p2],line)

    return proj


def cutting_point(line1, line2):  # intersection point
    a_x = line1[0][0]
    a_y = line1[0][1]
    b_x = line1[1][0]
    b_y = line1[1][1]
    c_x = line2[0][0]
    c_y = line2[0][1]
    d_x = line2[1][0]
    d_y = line2[1][1]

    # print(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)

    # [(b1 * c2 - b2 * c1) / (a1 * b2 - b1 * a2) , (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)]

    m_1 = (a_y - b_y) / (a_x - b_x)
    k_1 = a_y - m_1 * a_x

    m_2 = (c_y - d_y) / (c_x - d_x)
    k_2 = c_y - m_2 * c_x
    # print(m_1, k_1, m_2, k_2)

    b1 = -1
    b2 = -1
    a1 = m_1
    a2 = m_2
    c1 = k_1
    c2 = k_2

    x = (b1 * c2 - b2 * c1) / (a1 * b2 - b1 * a2)
    y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)

    # x = (k_2-k_1)/(m_1-m_2)
    # y = m_1*x + k_1

    # print(x, y)
    p = [x, y]
    return p


def getPoint(pose_no, joint_no):
    df = pd.read_csv("landmarks.csv")
    joint_x = "Joint_%s_x" % joint_no
    joint_y = "Joint_%s_y" % joint_no
    joint_z = "Joint_%s_z" % joint_no
    px = df.loc[pose_no, joint_x]
    py = df.loc[pose_no, joint_y]
    return [px, py]


# initialize the three points
# P1 is the mid point
# P2 is the point to draw solid
# P3 is the point to draw dotted lines
def drawLineOnImage(image_index, p1, p2, color=(0, 0, 255), offset="", from_offset=False, delete=False):
    """
    image_index is the image name
    p1 and p2 are the two points
    offset renames the file with original name + "_offset"
    if from_offset is true it will draw line on the image file with the offset in its name i.e.
    it will edit 13_1.jpg instead of 13.jpg if the image index = 13 and offset = 1.
    """

    # p1 = getPoint(0, 0) #take only x y coordinates leave out z
    # p2 = getPoint(0, 12)

    # Load the image
    img_ind = image_index
    original_path = "to_process/%s.jpg" % img_ind
    if not from_offset:
        image_path = "to_process/%s.jpg" % img_ind
    else:
        image_path = "to_process/%s_%s.jpg" % (img_ind, offset)
    image = cv2.imread(image_path)

    # Define the starting and ending points of the line
    x1, y1 = int(p1[0]), int(p1[1])  # Replace with your desired coordinates
    x2, y2 = int(p2[0]), int(p2[1])  # Replace with your desired coordinates
    # Draw the line on the image
    thickness = 2  # Line thickness
    cv2.line(image, (x1, y1), (x2, y2), color, thickness)

    if offset != "":
        offset = "_" + offset
    image_path = "to_process/%s%s.jpg" % (img_ind, offset)

    # Display the image with the drawn line

    # cv2.imshow("Image with Line", image)
    cv2.imwrite(image_path, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if delete:
        # delete the file
        os.remove(original_path)


# call the method and give it
# which image to draw on, from Point p1, to point p2, and color of image

# for two hands
for i in range(2):
    # 0
    currImg = 1 + i * 36
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(currImg - 1, 9), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(currImg, 9), color=(0, 255, 0))

    # 1
    currImg = 3 + i * 36
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(2, 9), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(3, 9), color=(0, 255, 0))

    # 2
    currImg = 5 + i * 36
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(currImg - 1, 9), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(currImg, 9), color=(0, 255, 0))

    # 3
    currImg = 7 + i * 36
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(currImg - 1, 9), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg - 1, 0), getPoint(currImg, 9), color=(0, 255, 0))

    # 4
    # for cutting point we use the basic axis and moving axis
    currImg = 9 + i * 36
    line1 = [getPoint(currImg, 5), getPoint(currImg, 8)]
    line2 = [getPoint(currImg, 1), getPoint(currImg, 4)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 8), color=(0, 0, 255))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 4), color=(0, 255, 0))

    # 5
    currImg = 11 + i * 36
    line = [getPoint(currImg, 8), getPoint(currImg, 5)]
    proj1 = proj_point(getPoint(currImg, 0), line)
    line2 = [getPoint(11, 4), getPoint(11, 1)]
    proj2 = proj_point(getPoint(currImg, 0), line2)
    # print(proj2, type(proj2))
    drawLineOnImage(currImg, proj1, getPoint(currImg, 8), color=(0, 0, 255))
    drawLineOnImage(currImg, proj2, getPoint(currImg, 4), color=(0, 255, 0))

    # 6
    currImg = 13 + i * 36
    line1 = [getPoint(currImg, 5), getPoint(currImg, 8)]
    line2 = [getPoint(currImg, 1), getPoint(currImg, 4)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 8), color=(0, 0, 255))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 4), color=(0, 255, 0))

    # 7
    currImg = 15 + i * 36
    line1 = [getPoint(currImg, 8), getPoint(currImg, 5)]
    proj1 = proj_point(getPoint(currImg, 0), line1)
    line2 = [getPoint(15, 1), getPoint(currImg, 4)]
    proj2 = proj_point(getPoint(currImg, 0), line2)
    drawLineOnImage(currImg, proj1, getPoint(currImg, 8), color=(0, 0, 255))
    drawLineOnImage(currImg, proj2, getPoint(currImg, 4), color=(0, 255, 0))

    # 8
    currImg = 17 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 1), getPoint(currImg, 2), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg, 2), getPoint(currImg, 3), color=(0, 255, 0))
    np_1 = np.array(getPoint(currImg, 1))
    np_2 = np.array(getPoint(currImg, 2))
    temp = np_2 - (np_1 - np_2)
    drawLineOnImage(currImg, getPoint(currImg, 2), temp.tolist(), color=(0, 255, 0))

    # 9
    currImg = 19 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 1), getPoint(currImg, 2), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg, 2), getPoint(currImg, 3), color=(0, 255, 0))
    np_1 = np.array(getPoint(currImg, 1))
    np_2 = np.array(getPoint(currImg, 2))
    temp = np_2 - (np_1 - np_2)
    drawLineOnImage(currImg, getPoint(currImg, 2), temp.tolist(), color=(0, 0, 255))

    # 10
    currImg = 21 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 3), getPoint(currImg, 2), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg, 3), getPoint(currImg, 4), color=(0, 255, 0))
    np_1 = np.array(getPoint(currImg, 2))
    np_2 = np.array(getPoint(currImg, 3))
    temp = np_2 - (np_1 - np_2)
    drawLineOnImage(currImg, getPoint(currImg, 3), temp.tolist(), color=(0, 0, 255))

    # 11
    currImg = 23 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 3), getPoint(currImg, 2), color=(0, 0, 255))
    drawLineOnImage(currImg, getPoint(currImg, 3), getPoint(currImg, 4), color=(0, 255, 0))
    np_1 = np.array(getPoint(currImg, 2))
    np_2 = np.array(getPoint(currImg, 3))
    temp = np_2 - (np_1 - np_2)
    drawLineOnImage(currImg, getPoint(currImg, 3), temp.tolist(), color=(0, 0, 255))

    # 12
    currImg = 25 + i * 36
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 5), getPoint(currImg, 6)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(0))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 6), color=(0, 255, 0), offset=str(0), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(0), from_offset=True)

    # 13
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 9), getPoint(currImg, 10)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(1))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 10), color=(0, 255, 0), offset=str(1), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(1), from_offset=True)

    # 14
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 13), getPoint(currImg, 14)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(2))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 14), color=(0, 255, 0), offset=str(2), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(2), from_offset=True)

    # 15
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 17), getPoint(currImg, 18)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(3))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 18), color=(0, 255, 0), offset=str(3), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(3), from_offset=True, delete=True)

    # 16
    currImg = 27 + i * 36
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 5), getPoint(currImg, 6)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(0))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 6), color=(0, 255, 0), offset=str(0), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(0), from_offset=True)

    # 17
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 9), getPoint(currImg, 10)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(1))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 10), color=(0, 255, 0), offset=str(1), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(1), from_offset=True)

    # 18
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 13), getPoint(currImg, 14)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(2))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 14), color=(0, 255, 0), offset=str(2), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(2), from_offset=True)

    # 19
    line1 = [getPoint(currImg, 0), getPoint(currImg, 9)]
    line2 = [getPoint(currImg, 17), getPoint(currImg, 18)]
    cut_p = cutting_point(line1, line2)
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 0), color=(0, 0, 255), offset=str(3))
    drawLineOnImage(currImg, cut_p, getPoint(currImg, 18), color=(0, 255, 0), offset=str(3), from_offset=True)
    np_1 = np.array(cut_p)
    np_2 = np.array(getPoint(currImg, 0))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, cut_p, temp.tolist(), color=(0, 0, 255), offset=str(3), from_offset=True, delete=True)

    # 20
    currImg = 29 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 6), getPoint(currImg, 5), color=(0, 0, 255), offset=str(0))
    drawLineOnImage(
        currImg, getPoint(currImg, 6), getPoint(currImg, 7), color=(0, 255, 0), offset=str(0), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 6))
    np_2 = np.array(getPoint(currImg, 5))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 6), temp.tolist(), color=(0, 0, 255), offset=str(0), from_offset=True)

    # 21
    drawLineOnImage(currImg, getPoint(currImg, 10), getPoint(currImg, 9), color=(0, 0, 255), offset=str(1))
    drawLineOnImage(
        currImg, getPoint(currImg, 11), getPoint(currImg, 10), color=(0, 255, 0), offset=str(1), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 10))
    np_2 = np.array(getPoint(currImg, 9))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 10), temp.tolist(), color=(0, 0, 255), offset=str(1), from_offset=True)

    # 22
    drawLineOnImage(currImg, getPoint(currImg, 14), getPoint(currImg, 13), color=(0, 0, 255), offset=str(2))
    drawLineOnImage(
        currImg, getPoint(currImg, 14), getPoint(currImg, 15), color=(0, 255, 0), offset=str(2), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 14))
    np_2 = np.array(getPoint(currImg, 13))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 14), temp.tolist(), color=(0, 0, 255), offset=str(2), from_offset=True)

    # 23
    drawLineOnImage(currImg, getPoint(currImg, 18), getPoint(currImg, 17), color=(0, 0, 255), offset=str(3))
    drawLineOnImage(
        currImg, getPoint(currImg, 18), getPoint(currImg, 19), color=(0, 255, 0), offset=str(3), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 18))
    np_2 = np.array(getPoint(currImg, 17))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(
        currImg, getPoint(currImg, 18), temp.tolist(), color=(0, 0, 255), offset=str(3), from_offset=True, delete=True
    )

    # 24
    currImg = 31 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 6), getPoint(currImg, 5), color=(0, 0, 255), offset=str(0))
    drawLineOnImage(
        currImg, getPoint(currImg, 6), getPoint(currImg, 7), color=(0, 255, 0), offset=str(0), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 6))
    np_2 = np.array(getPoint(currImg, 5))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 6), temp.tolist(), color=(0, 0, 255), offset=str(0), from_offset=True)

    # 25
    drawLineOnImage(currImg, getPoint(currImg, 9), getPoint(currImg, 10), color=(0, 0, 255), offset=str(1))
    drawLineOnImage(
        currImg, getPoint(currImg, 10), getPoint(currImg, 11), color=(0, 255, 0), offset=str(1), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 10))
    np_2 = np.array(getPoint(currImg, 9))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 10), temp.tolist(), color=(0, 0, 255), offset=str(1), from_offset=True)

    # 26
    drawLineOnImage(currImg, getPoint(currImg, 14), getPoint(currImg, 13), color=(0, 0, 255), offset=str(2))
    drawLineOnImage(
        currImg, getPoint(currImg, 14), getPoint(currImg, 15), color=(0, 255, 0), offset=str(2), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 14))
    np_2 = np.array(getPoint(currImg, 13))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 14), temp.tolist(), color=(0, 0, 255), offset=str(2), from_offset=True)

    # 27
    drawLineOnImage(currImg, getPoint(currImg, 18), getPoint(currImg, 17), color=(0, 0, 255), offset=str(3))
    drawLineOnImage(
        currImg, getPoint(currImg, 18), getPoint(currImg, 19), color=(0, 255, 0), offset=str(3), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 18))
    np_2 = np.array(getPoint(currImg, 17))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(
        currImg, getPoint(currImg, 18), temp.tolist(), color=(0, 0, 255), offset=str(3), from_offset=True, delete=True
    )

    # 28
    currImg = 33 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 7), getPoint(currImg, 6), color=(0, 0, 255), offset=str(0))
    drawLineOnImage(
        currImg, getPoint(currImg, 7), getPoint(currImg, 8), color=(0, 255, 0), offset=str(0), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 7))
    np_2 = np.array(getPoint(currImg, 6))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 7), temp.tolist(), color=(0, 0, 255), offset=str(0), from_offset=True)

    # 29
    drawLineOnImage(currImg, getPoint(currImg, 11), getPoint(currImg, 10), color=(0, 0, 255), offset=str(1))
    drawLineOnImage(
        currImg, getPoint(currImg, 11), getPoint(currImg, 12), color=(0, 255, 0), offset=str(1), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 11))
    np_2 = np.array(getPoint(currImg, 10))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 11), temp.tolist(), color=(0, 0, 255), offset=str(1), from_offset=True)

    # 30
    drawLineOnImage(currImg, getPoint(currImg, 15), getPoint(currImg, 14), color=(0, 0, 255), offset=str(2))
    drawLineOnImage(
        currImg, getPoint(currImg, 15), getPoint(currImg, 16), color=(0, 255, 0), offset=str(2), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 15))
    np_2 = np.array(getPoint(currImg, 14))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(currImg, getPoint(currImg, 15), temp.tolist(), color=(0, 0, 255), offset=str(2), from_offset=True)

    # 31
    drawLineOnImage(currImg, getPoint(currImg, 19), getPoint(currImg, 18), color=(0, 0, 255), offset=str(3))
    drawLineOnImage(
        currImg, getPoint(currImg, 19), getPoint(currImg, 20), color=(0, 255, 0), offset=str(3), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 19))
    np_2 = np.array(getPoint(currImg, 18))
    temp = np_1 - (np_2 - np_1)
    drawLineOnImage(
        currImg, getPoint(currImg, 19), temp.tolist(), color=(0, 0, 255), offset=str(3), from_offset=True, delete=True
    )

    # 32
    currImg = 35 + i * 36
    drawLineOnImage(currImg, getPoint(currImg, 7), getPoint(currImg, 6), color=(0, 0, 255), offset=str(0))
    drawLineOnImage(
        currImg, getPoint(currImg, 7), getPoint(currImg, 8), color=(0, 255, 0), offset=str(0), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 7))
    np_2 = np.array(getPoint(currImg, 6))
    temp = np_1 - (np_2 - np_1)
    # drawLineOnImage(currImg, getPoint(currImg, 7), temp.tolist(), color = (0, 0, 255),  offset=str(0), from_offset=True)
    drawLineOnImage(currImg, getPoint(currImg, 7), temp.tolist(), color=(0, 0, 255), offset=str(0), from_offset=True)

    ##33
    drawLineOnImage(currImg, getPoint(currImg, 11), getPoint(currImg, 10), color=(0, 0, 255), offset=str(1))
    drawLineOnImage(
        currImg, getPoint(currImg, 11), getPoint(currImg, 12), color=(0, 255, 0), offset=str(1), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 11))
    np_2 = np.array(getPoint(currImg, 10))
    temp = np_1 - (np_2 - np_1)
    # drawLineOnImage(currImg, getPoint(currImg, 11), temp.tolist(), color = (0, 0, 255),  offset=str(1), from_offset=True)
    drawLineOnImage(currImg, getPoint(currImg, 11), temp.tolist(), color=(0, 0, 255), offset=str(1), from_offset=True)

    ##34
    drawLineOnImage(currImg, getPoint(currImg, 15), getPoint(currImg, 14), color=(0, 0, 255), offset=str(2))
    drawLineOnImage(
        currImg, getPoint(currImg, 15), getPoint(currImg, 16), color=(0, 255, 0), offset=str(2), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 15))
    np_2 = np.array(getPoint(currImg, 14))
    temp = np_1 - (np_2 - np_1)
    # drawLineOnImage(currImg, getPoint(currImg, 15), temp.tolist(), color = (0, 0, 255),  offset=str(2), from_offset=True)
    drawLineOnImage(currImg, getPoint(currImg, 15), temp.tolist(), color=(0, 0, 255), offset=str(2), from_offset=True)

    # 35
    drawLineOnImage(currImg, getPoint(currImg, 19), getPoint(currImg, 18), color=(0, 0, 255), offset=str(3))
    drawLineOnImage(
        currImg, getPoint(currImg, 19), getPoint(currImg, 20), color=(0, 255, 0), offset=str(3), from_offset=True
    )
    np_1 = np.array(getPoint(currImg, 19))
    np_2 = np.array(getPoint(currImg, 18))
    temp = np_1 - (np_2 - np_1)
    # drawLineOnImage(currImg, getPoint(currImg, 19), temp.tolist(), color = (0, 0, 255),  offset=str(3), from_offset=True, delete = True)
    drawLineOnImage(
        currImg, getPoint(currImg, 19), temp.tolist(), color=(0, 0, 255), offset=str(3), from_offset=True, delete=True
    )

# #write angles:
angleDf = pd.read_csv("to_process/angle.csv")
angles = angleDf["Angle"].values.tolist()
file = pd.Series(data=angles, index=angleDf["Pose"])
for name, ang in file.items():
    image_path = "to_process/" + str(name).strip() + ".jpg"
    image = cv2.imread(image_path)
    new_image = cv2.putText(
        img=image,
        text=str(round(ang, 1)) + " deg",
        org=(100, 200),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=1.0,
        color=(125, 246, 55),
        thickness=3,
    )
    cv2.imwrite(image_path, new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
