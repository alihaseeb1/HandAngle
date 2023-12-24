import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import pandas as pd


# First step is to initialize the Hands class an store it in a variable
mp_hands = mp.solutions.hands

# Now second step is to set the hands function which will hold the landmarks points
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.3)

# Last step is to set up the drawing function of hands landmarks on the image
mp_drawing = mp.solutions.drawing_utils

NUM_OF_POSES = 72
poses = np.zeros((NUM_OF_POSES, 21, 3))

for i in range(NUM_OF_POSES):  # Number of poses
    # POSE_NAMES.append("\\to_process\\" + str(i) +".jpg");
    # Reading the sample image on which we will perform the detection
    sample_img = cv2.imread("to_process/%s.jpg" % i)

    # Here we are specifing the size of the figure i.e. 10 -height; 10- width.
    # plt.figure(figsize=[10, 10])

    # Here we will display the sample image as the output.
    # plt.title("" + str(i) + "_unprocessed");plt.axis('off');plt.imshow(sample_img[:,:,::-1]);plt.show()

    results = hands.process(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))

    image_height, image_width, _ = sample_img.shape
    # Create original coordinates
    if results.multi_hand_landmarks:
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            joints = np.zeros((21, 3))
            for j in range(21):
                # save each joint as an array
                # remove the multiplying by image_width, image_height to normalize it
                joint = np.array(
                    (
                        hand_landmarks.landmark[mp_hands.HandLandmark(j).value].x * image_width,
                        hand_landmarks.landmark[mp_hands.HandLandmark(j).value].y * image_height,
                        hand_landmarks.landmark[mp_hands.HandLandmark(j).value].z * image_width,
                    )
                )
                joints[j] = joint

                # print(f'{mp_hands.HandLandmark(i).name}:')
            # print("ID :", i)
            # print(f'{hand_landmarks.landmark[mp_hands.HandLandmark(i).value]}')

    # Image with landmarks
    img_copy = sample_img.copy()

    if results.multi_hand_landmarks:
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(
                image=img_copy, landmark_list=hand_landmarks, connections=mp_hands.HAND_CONNECTIONS
            )
        plt.figure(figsize=[10, 10])
        fig = plt.figure(figsize=[10, 10])

        plt.title("" + str(i) + "_landmarked")
        plt.axis("off")
        plt.imshow(img_copy[:, :, ::-1])
        plt.savefig(
            "landmarked_img/" + str(i) + "_landmarked.jpg", bbox_inches="tight"
        )  # plt.show must follow savefig else blank file
        # plt.show()
        plt.close("all")
        # cv2.imwrite("" + str(i) + "_processed", img_copy)

    # one pose done
    # print(i, joints)
    poses[i, :, :] = joints

# Save poses as csv
# print(poses.shape)
axis = ["x", "y", "z"]
cols = ["Joint_" + str(col) + "_" + str(axis[x]) for col in range(0, 21) for x in range(3)]
poses = poses.reshape(NUM_OF_POSES, -1)
df = pd.DataFrame(poses, columns=cols)
df.to_csv("landmarks.csv")
