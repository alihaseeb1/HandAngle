import numpy as np
import csv
import pandas as pd

def get_3D_angle(p1, p2, p3, p4):
    # Calculate the vectors between the points
    v1 = p2 - p1
    v2 = p4 - p3

    # Calculate the dot product of the vectors
    dot_product_v1v2 = np.dot(v1, v2)

    # Calculate the magnitudes of the vectors
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)

    # Calculate the cosine of the angle
    cos_angle_v1v2 = dot_product_v1v2 / (magnitude_v1 * magnitude_v2)

    # Ensure cos_angle_v1v2 is within [-1, 1] to avoid invalid input to arccos
    cos_angle_v1v2 = min(1.0, max(-1.0, cos_angle_v1v2))

    # Calculate the angle in radians
    angle_rad_v1v2 = np.arccos(cos_angle_v1v2)

    # Convert the angle to degrees
    angle_deg_v1v2 = np.degrees(angle_rad_v1v2)

    return angle_deg_v1v2


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('landmarks.csv')

#Joint_0_x = df.at[0, 'Joint_0_x']
#Joint_0_y = df.at[0, 'Joint_0_y']
#Joint_0_z = df.at[0, 'Joint_0_z']

################### Left Hand ###########################

################### Pose 0 1 ###########################
pose = 0

i = 0
Joint00 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint09 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 1

i = 0
Joint10 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i=5
Joint15 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p00 = np.array(Joint00)
p09 = np.array(Joint09)
p10 = np.array(Joint10)
p15 = np.array(Joint15)

# Calculate the angle between v1 and v2
angle_deg_p01 = get_3D_angle(p00, p09, p10, p15)

################### Pose 2 3 ###########################
pose = 2

i = 0
Joint20 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint29 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 3

i = 0
Joint30 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i=5
Joint35 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p20 = np.array(Joint20)
p29 = np.array(Joint29)
p30 = np.array(Joint30)
p35 = np.array(Joint35)

# Calculate the angle between v1 and v2
angle_deg_p23 = get_3D_angle(p20, p29, p30, p35)

################### Pose 4 5 ###########################
pose = 4

i = 0
Joint40 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint49 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 5

i = 0
Joint50 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 9
Joint59 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p40 = np.array(Joint40)
p49 = np.array(Joint49)
p50 = np.array(Joint50)
p59 = np.array(Joint59)

# Calculate the angle between v1 and v2
angle_deg_p45 = get_3D_angle(p40, p49, p50, p59)

################### Pose 6 7 ###########################
pose = 6

i = 0
Joint60 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint69 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 7

i = 0
Joint70 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 9
Joint79 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p60 = np.array(Joint60)
p69 = np.array(Joint69)
p70 = np.array(Joint70)
p79 = np.array(Joint79)

# Calculate the angle between v1 and v2
angle_deg_p67 = get_3D_angle(p60, p69, p70, p79)

################### Pose 9 ###########################
pose = 9

i = 5
Joint85 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint88 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint81 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint84 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p85 = np.array(Joint85)
p88 = np.array(Joint88)
p81 = np.array(Joint81)
p84 = np.array(Joint84)

# Calculate the angle between v1 and v2
angle_deg_p8 = get_3D_angle(p85, p88, p81, p84)

################### Pose 11 ###########################
pose = 11

i = 5
Joint95 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint98 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint91 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint94 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p95 = np.array(Joint95)
p98 = np.array(Joint98)
p91 = np.array(Joint91)
p94 = np.array(Joint94)

# Calculate the angle between v1 and v2
angle_deg_p9 = get_3D_angle(p95, p98, p91, p94)

################### Pose 13 ###########################
pose = 13

i = 5
Joint105 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint108 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint101 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint104 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p105 = np.array(Joint105)
p108 = np.array(Joint108)
p101 = np.array(Joint101)
p104 = np.array(Joint104)

# Calculate the angle between v1 and v2
angle_deg_p10 = get_3D_angle(p105, p108, p101, p104)

################### Pose 15 ###########################
pose = 15

i = 5
Joint115 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint118 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint111 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint114 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p115 = np.array(Joint115)
p118 = np.array(Joint118)
p111 = np.array(Joint111)
p114 = np.array(Joint114)

# Calculate the angle between v1 and v2
angle_deg_p11 = get_3D_angle(p115, p118, p111, p114)

################### Pose 17 ###########################
pose = 17

i = 1
Joint121 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 2
Joint122 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 3
Joint123 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p121 = np.array(Joint121)
p122 = np.array(Joint122)
p123 = np.array(Joint122)
p124 = np.array(Joint123)

# Calculate the angle between v1 and v2
angle_deg_p12 = get_3D_angle(p121, p122, p123, p124)

################### Pose 19 ###########################
pose = 19

i = 1
Joint131 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 2
Joint132 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 3
Joint133 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p131 = np.array(Joint131)
p132 = np.array(Joint132)
p134 = np.array(Joint133)

# Calculate the angle between v1 and v2
angle_deg_p13 = get_3D_angle(p131, p132, p132, p134)

################### Pose 21 ###########################
pose = 21

i = 2
Joint142 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 3
Joint143 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 4
Joint144 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p142 = np.array(Joint142)
p143 = np.array(Joint143)
p144 = np.array(Joint144)

# Calculate the angle between v1 and v2
angle_deg_p14 = get_3D_angle(p142, p143, p143, p144)

################### Pose 23 ###########################
pose = 23

i = 2
Joint152 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 3
Joint153 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 4
Joint154 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p152 = np.array(Joint152)
p153 = np.array(Joint153)
p154 = np.array(Joint154)

# Calculate the angle between v1 and v2
angle_deg_p15 = get_3D_angle(p152, p153, p153, p154)

################### Pose 25 ###########################
pose = 25

i = 0
Joint160 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint169 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 5
Joint165 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 6
Joint166 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1610 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1613 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1614 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1617 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1618 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p160 = np.array(Joint160)
p169 = np.array(Joint169)
p165 = np.array(Joint165)
p166 = np.array(Joint166)
p1610 = np.array(Joint1610)
p1613 = np.array(Joint1613)
p1614 = np.array(Joint1614)
p1617 = np.array(Joint1617)
p1618 = np.array(Joint1618)

# Calculate the angle between v1 and v2
angle_deg_p161 = get_3D_angle(p160, p169, p165, p166)
angle_deg_p162 = get_3D_angle(p160, p169, p169, p1610)
angle_deg_p163 = get_3D_angle(p160, p169, p1613, p1614)
angle_deg_p164 = get_3D_angle(p160, p169, p1617, p1618)

################### Pose 27 ###########################
pose = 27

i = 0
Joint170 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint179 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 5
Joint175 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 6
Joint176 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1710 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1713 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1714 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1717 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1718 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p170 = np.array(Joint170)
p179 = np.array(Joint179)
p175 = np.array(Joint175)
p176 = np.array(Joint176)
p1710 = np.array(Joint1710)
p1713 = np.array(Joint1713)
p1714 = np.array(Joint1714)
p1717 = np.array(Joint1717)
p1718 = np.array(Joint1718)

# Calculate the angle between v1 and v2
angle_deg_p171 = get_3D_angle(p170, p179, p175, p176)
angle_deg_p172 = get_3D_angle(p170, p179, p179, p1710)
angle_deg_p173 = get_3D_angle(p170, p179, p1713, p1714)
angle_deg_p174 = get_3D_angle(p170, p179, p1717, p1718)

################### Pose 29 ###########################
pose = 29

i = 5
Joint185 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 6
Joint186 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint187 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 9
Joint189 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1810 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint1811 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1813 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1817 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1814 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint1815 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1817 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1818 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint1819 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p185 = np.array(Joint185)
p186 = np.array(Joint186)
p187 = np.array(Joint187)
p189 = np.array(Joint189)
p1810 = np.array(Joint1810)
p1811 = np.array(Joint1811)
p1813 = np.array(Joint1813)
p1814 = np.array(Joint1814)
p1815 = np.array(Joint1815)
p1817 = np.array(Joint1817)
p1818 = np.array(Joint1818)
p1819 = np.array(Joint1819)

# Calculate the angle between v1 and v2
angle_deg_p181 = get_3D_angle(p185, p186, p186, p187)
angle_deg_p182 = get_3D_angle(p189, p1810, p1810, p1811)
angle_deg_p183 = get_3D_angle(p1813, p1814, p1814, p1815)
angle_deg_p184 = get_3D_angle(p1817, p1818, p1818, p1819)

################### Pose 31 ###########################
pose = 31

i = 5
Joint195 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 6
Joint196 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint197 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 9
Joint199 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1910 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint1911 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1913 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1917 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1914 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint1915 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1917 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1918 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint1919 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p195 = np.array(Joint195)
p196 = np.array(Joint196)
p197 = np.array(Joint197)
p199 = np.array(Joint199)
p1910 = np.array(Joint1910)
p1911 = np.array(Joint1911)
p1913 = np.array(Joint1913)
p1914 = np.array(Joint1914)
p1915 = np.array(Joint1915)
p1917 = np.array(Joint1917)
p1918 = np.array(Joint1918)
p1919 = np.array(Joint1919)

# Calculate the angle between v1 and v2
angle_deg_p191 = get_3D_angle(p195, p196, p196, p197)
angle_deg_p192 = get_3D_angle(p199, p1910, p1910, p1911)
angle_deg_p193 = get_3D_angle(p1913, p1914, p1914, p1915)
angle_deg_p194 = get_3D_angle(p1917, p1918, p1918, p1919)

################### Pose 33 ###########################
pose = 33

i = 6
Joint206 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint207 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 8
Joint208 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint2010 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint2011 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 12
Joint2012 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint2014 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint2015 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 16
Joint2016 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint2018 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint2019 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 20
Joint2020 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p206 = np.array(Joint206)
p207 = np.array(Joint207)
p208 = np.array(Joint208)
p2010 = np.array(Joint2010)
p2011 = np.array(Joint2011)
p2012 = np.array(Joint2012)
p2014 = np.array(Joint2014)
p2015 = np.array(Joint2015)
p2016 = np.array(Joint2016)
p2018 = np.array(Joint2018)
p2019 = np.array(Joint2019)
p2020 = np.array(Joint2020)

# Calculate the angle between v1 and v2
angle_deg_p201 = get_3D_angle(p206, p207, p207, p208)
angle_deg_p202 = get_3D_angle(p2010, p2011, p2011, p2012)
angle_deg_p203 = get_3D_angle(p2014, p2015, p2015, p2016)
angle_deg_p204 = get_3D_angle(p2018, p2019, p2019, p2020)

################### Pose 35 ###########################
pose = 35

i = 6
Joint216 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint217 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 8
Joint218 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint2110 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint2111 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 12
Joint2112 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint2114 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint2115 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 16
Joint2116 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint2118 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint2119 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 20
Joint2120 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p216 = np.array(Joint216)
p217 = np.array(Joint217)
p218 = np.array(Joint218)
p2110 = np.array(Joint2110)
p2111 = np.array(Joint2111)
p2112 = np.array(Joint2112)
p2114 = np.array(Joint2114)
p2115 = np.array(Joint2115)
p2116 = np.array(Joint2116)
p2118 = np.array(Joint2118)
p2119 = np.array(Joint2119)
p2120 = np.array(Joint2120)

# Calculate the angle between v1 and v2
angle_deg_p211 = get_3D_angle(p216, p217, p217, p218)
angle_deg_p212 = get_3D_angle(p2110, p2111, p2111, p2112)
angle_deg_p213 = get_3D_angle(p2114, p2115, p2115, p2116)
angle_deg_p214 = get_3D_angle(p2118, p2119, p2119, p2120)


################### Right Hand ###########################

################### Pose 36 37 ###########################
pose = 36

i = 0
Joint00 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint09 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 37

i = 0
Joint10 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i=5
Joint15 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p00 = np.array(Joint00)
p09 = np.array(Joint09)
p10 = np.array(Joint10)
p15 = np.array(Joint15)

# Calculate the angle between v1 and v2
angle_deg_p01r = get_3D_angle(p00, p09, p10, p15)

################### Pose 38 39 ###########################
pose = 38

i = 0
Joint20 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint29 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 39

i = 0
Joint30 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i=5
Joint35 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p20 = np.array(Joint20)
p29 = np.array(Joint29)
p30 = np.array(Joint30)
p35 = np.array(Joint35)

# Calculate the angle between v1 and v2
angle_deg_p23r = get_3D_angle(p20, p29, p30, p35)

################### Pose 40 41 ###########################
pose = 40

i = 0
Joint40 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint49 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 41

i = 0
Joint50 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 9
Joint59 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p40 = np.array(Joint40)
p49 = np.array(Joint49)
p50 = np.array(Joint50)
p59 = np.array(Joint59)

# Calculate the angle between v1 and v2
angle_deg_p45r = get_3D_angle(p40, p49, p50, p59)

################### Pose 42 43 ###########################
pose = 42

i = 0
Joint60 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint69 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

pose = 43

i = 0
Joint70 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 9
Joint79 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p60 = np.array(Joint60)
p69 = np.array(Joint69)
p70 = np.array(Joint70)
p79 = np.array(Joint79)

# Calculate the angle between v1 and v2
angle_deg_p67r = get_3D_angle(p60, p69, p70, p79)

################### Pose 45 ###########################
pose = 45

i = 5
Joint85 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint88 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint81 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint84 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p85 = np.array(Joint85)
p88 = np.array(Joint88)
p81 = np.array(Joint81)
p84 = np.array(Joint84)

# Calculate the angle between v1 and v2
angle_deg_p8r = get_3D_angle(p85, p88, p81, p84)

################### Pose 47 ###########################
pose = 47

i = 5
Joint95 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint98 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint91 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint94 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p95 = np.array(Joint95)
p98 = np.array(Joint98)
p91 = np.array(Joint91)
p94 = np.array(Joint94)

# Calculate the angle between v1 and v2
angle_deg_p9r = get_3D_angle(p95, p98, p91, p94)

################### Pose 49 ###########################
pose = 49

i = 5
Joint105 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint108 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint101 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint104 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p105 = np.array(Joint105)
p108 = np.array(Joint108)
p101 = np.array(Joint101)
p104 = np.array(Joint104)

# Calculate the angle between v1 and v2
angle_deg_p10r = get_3D_angle(p105, p108, p101, p104)

################### Pose 51 ###########################
pose = 51

i = 5
Joint115 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 8
Joint118 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i = 1
Joint111 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i= 4
Joint114 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p115 = np.array(Joint115)
p118 = np.array(Joint118)
p111 = np.array(Joint111)
p114 = np.array(Joint114)

# Calculate the angle between v1 and v2
angle_deg_p11r = get_3D_angle(p115, p118, p111, p114)

################### Pose 53 ###########################
pose = 53

i = 1
Joint121 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 2
Joint122 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 3
Joint123 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p121 = np.array(Joint121)
p122 = np.array(Joint122)
p123 = np.array(Joint122)
p124 = np.array(Joint123)

# Calculate the angle between v1 and v2
angle_deg_p12r = get_3D_angle(p121, p122, p123, p124)

################### Pose 55 ###########################
pose = 55

i = 1
Joint131 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 2
Joint132 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 3
Joint133 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p131 = np.array(Joint131)
p132 = np.array(Joint132)
p134 = np.array(Joint133)

# Calculate the angle between v1 and v2
angle_deg_p13r = get_3D_angle(p131, p132, p132, p134)

################### Pose 57 ###########################
pose = 57

i = 2
Joint142 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 3
Joint143 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 4
Joint144 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p142 = np.array(Joint142)
p143 = np.array(Joint143)
p144 = np.array(Joint144)

# Calculate the angle between v1 and v2
angle_deg_p14r = get_3D_angle(p142, p143, p143, p144)

################### Pose 59 ###########################
pose = 59

i = 2
Joint152 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 3
Joint153 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 4
Joint154 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p152 = np.array(Joint152)
p153 = np.array(Joint153)
p154 = np.array(Joint154)

# Calculate the angle between v1 and v2
angle_deg_p15r = get_3D_angle(p152, p153, p153, p154)

################### Pose 61 ###########################
pose = 61

i = 0
Joint160 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint169 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 5
Joint165 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 6
Joint166 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1610 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1613 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1614 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1617 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1618 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p160 = np.array(Joint160)
p169 = np.array(Joint169)
p165 = np.array(Joint165)
p166 = np.array(Joint166)
p1610 = np.array(Joint1610)
p1613 = np.array(Joint1613)
p1614 = np.array(Joint1614)
p1617 = np.array(Joint1617)
p1618 = np.array(Joint1618)

# Calculate the angle between v1 and v2
angle_deg_p161r = get_3D_angle(p160, p169, p165, p166)
angle_deg_p162r = get_3D_angle(p160, p169, p169, p1610)
angle_deg_p163r = get_3D_angle(p160, p169, p1613, p1614)
angle_deg_p164r = get_3D_angle(p160, p169, p1617, p1618)

################### Pose 63 ###########################
pose = 63

i = 0
Joint170 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 9
Joint179 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 5
Joint175 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 6
Joint176 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1710 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1713 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1714 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1717 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1718 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p170 = np.array(Joint170)
p179 = np.array(Joint179)
p175 = np.array(Joint175)
p176 = np.array(Joint176)
p1710 = np.array(Joint1710)
p1713 = np.array(Joint1713)
p1714 = np.array(Joint1714)
p1717 = np.array(Joint1717)
p1718 = np.array(Joint1718)

# Calculate the angle between v1 and v2
angle_deg_p171r = get_3D_angle(p170, p179, p175, p176)
angle_deg_p172r = get_3D_angle(p170, p179, p179, p1710)
angle_deg_p173r = get_3D_angle(p170, p179, p1713, p1714)
angle_deg_p174r = get_3D_angle(p170, p179, p1717, p1718)

################### Pose 65 ###########################
pose = 65

i = 5
Joint185 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 6
Joint186 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint187 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 9
Joint189 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1810 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint1811 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1813 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1817 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1814 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint1815 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1817 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1818 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint1819 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p185 = np.array(Joint185)
p186 = np.array(Joint186)
p187 = np.array(Joint187)
p189 = np.array(Joint189)
p1810 = np.array(Joint1810)
p1811 = np.array(Joint1811)
p1813 = np.array(Joint1813)
p1814 = np.array(Joint1814)
p1815 = np.array(Joint1815)
p1817 = np.array(Joint1817)
p1818 = np.array(Joint1818)
p1819 = np.array(Joint1819)

# Calculate the angle between v1 and v2
angle_deg_p181r = get_3D_angle(p185, p186, p186, p187)
angle_deg_p182r = get_3D_angle(p189, p1810, p1810, p1811)
angle_deg_p183r = get_3D_angle(p1813, p1814, p1814, p1815)
angle_deg_p184r = get_3D_angle(p1817, p1818, p1818, p1819)

################### Pose 67 ###########################
pose = 67

i = 5
Joint195 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])
i = 6
Joint196 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint197 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 9
Joint199 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint1910 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint1911 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 13
Joint1913 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1917 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint1914 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint1915 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 17
Joint1917 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint1918 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint1919 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p195 = np.array(Joint195)
p196 = np.array(Joint196)
p197 = np.array(Joint197)
p199 = np.array(Joint199)
p1910 = np.array(Joint1910)
p1911 = np.array(Joint1911)
p1913 = np.array(Joint1913)
p1914 = np.array(Joint1914)
p1915 = np.array(Joint1915)
p1917 = np.array(Joint1917)
p1918 = np.array(Joint1918)
p1919 = np.array(Joint1919)

# Calculate the angle between v1 and v2
angle_deg_p191r = get_3D_angle(p195, p196, p196, p197)
angle_deg_p192r = get_3D_angle(p199, p1910, p1910, p1911)
angle_deg_p193r = get_3D_angle(p1913, p1914, p1914, p1915)
angle_deg_p194r = get_3D_angle(p1917, p1918, p1918, p1919)

################### Pose 69 ###########################
pose = 69

i = 6
Joint206 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint207 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 8
Joint208 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint2010 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint2011 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 12
Joint2012 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint2014 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint2015 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 16
Joint2016 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint2018 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint2019 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 20
Joint2020 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p206 = np.array(Joint206)
p207 = np.array(Joint207)
p208 = np.array(Joint208)
p2010 = np.array(Joint2010)
p2011 = np.array(Joint2011)
p2012 = np.array(Joint2012)
p2014 = np.array(Joint2014)
p2015 = np.array(Joint2015)
p2016 = np.array(Joint2016)
p2018 = np.array(Joint2018)
p2019 = np.array(Joint2019)
p2020 = np.array(Joint2020)

# Calculate the angle between v1 and v2
angle_deg_p201r = get_3D_angle(p206, p207, p207, p208)
angle_deg_p202r = get_3D_angle(p2010, p2011, p2011, p2012)
angle_deg_p203r = get_3D_angle(p2014, p2015, p2015, p2016)
angle_deg_p204r = get_3D_angle(p2018, p2019, p2019, p2020)

################### Pose 71 ###########################
pose = 71

i = 6
Joint216 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 7
Joint217 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 8
Joint218 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 10
Joint2110 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 11
Joint2111 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 12
Joint2112 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 14
Joint2114 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 15
Joint2115 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 16
Joint2116 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 18
Joint2118 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 19
Joint2119 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

i= 20
Joint2120 = (df.at[pose, 'Joint_%s_x' % i], 
	df.at[pose, 'Joint_%s_y' % i], 
	df.at[pose, 'Joint_%s_z' % i])

p216 = np.array(Joint216)
p217 = np.array(Joint217)
p218 = np.array(Joint218)
p2110 = np.array(Joint2110)
p2111 = np.array(Joint2111)
p2112 = np.array(Joint2112)
p2114 = np.array(Joint2114)
p2115 = np.array(Joint2115)
p2116 = np.array(Joint2116)
p2118 = np.array(Joint2118)
p2119 = np.array(Joint2119)
p2120 = np.array(Joint2120)

# Calculate the angle between v1 and v2
angle_deg_p211r = get_3D_angle(p216, p217, p217, p218)
angle_deg_p212r = get_3D_angle(p2110, p2111, p2111, p2112)
angle_deg_p213r = get_3D_angle(p2114, p2115, p2115, p2116)
angle_deg_p214r = get_3D_angle(p2118, p2119, p2119, p2120)

# Open the CSV file in append mode and write the header if the file is empty
with open('to_process/angle.csv', 'a', newline='') as csvfile:
    fieldnames = ['Pose','Joint name' ,'Angle']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header if the file is empty
    if csvfile.tell() == 0:
        writer.writeheader()

    writer.writerow({'Pose': '1','Joint name' : 'R -Wrist - Flexion','Angle': angle_deg_p01})
    writer.writerow({'Pose': '3','Joint name' : 'R -Wrist - Extension', 'Angle': angle_deg_p23})
    writer.writerow({'Pose': '5','Joint name' : 'R -Wrist - Radial Deviation', 'Angle': angle_deg_p45})
    writer.writerow({'Pose': '7', 'Joint name' :'R -Wrist - Ulnar Deviation' ,'Angle': angle_deg_p67})
    writer.writerow({'Pose': '9', 'Joint name' :'R -Thumb - Radial Abduction' ,'Angle': angle_deg_p8})
    writer.writerow({'Pose': '11', 'Joint name' : 'R -Thumb - Ulnar Abduction', 'Angle': angle_deg_p9})
    writer.writerow({'Pose': '13', 'Joint name' : 'R -Thumb - Palmer Abduction' ,'Angle': angle_deg_p10})
    writer.writerow({'Pose': '15', 'Joint name' : 'R -Thumb - Palmer Abduction','Angle': angle_deg_p11})
    writer.writerow({'Pose': '17', 'Joint name' : 'R -Thumb - Flexion MCP','Angle': angle_deg_p12})
    writer.writerow({'Pose': '19', 'Joint name' : 'R -Thumb - Extension MCP','Angle': angle_deg_p13})
    writer.writerow({'Pose': '21', 'Joint name' : 'R -Thumb - Flexion IP','Angle': angle_deg_p14})
    writer.writerow({'Pose': '23', 'Joint name' : 'R -Thumb - Extension IP','Angle': angle_deg_p15})

    writer.writerow({'Pose': '25_0', 'Joint name' : 'R -Finger_0 - Flexion MCP','Angle': angle_deg_p161})
    writer.writerow({'Pose': '25_1', 'Joint name' : 'R -Finger_1 - Flexion MCP','Angle': angle_deg_p162})
    writer.writerow({'Pose': '25_2', 'Joint name' : 'R -Finger_2 - Flexion MCP','Angle': angle_deg_p163})
    writer.writerow({'Pose': '25_3', 'Joint name' : 'R -Finger_3 - Flexion MCP','Angle': angle_deg_p164})

    writer.writerow({'Pose': '27_0', 'Joint name' : 'R -Finger_0 - Extension MCP','Angle': angle_deg_p171})
    writer.writerow({'Pose': '27_1', 'Joint name' : 'R -Finger_1 - Extension MCP','Angle': angle_deg_p172})
    writer.writerow({'Pose': '27_2', 'Joint name' : 'R -Finger_2 - Extension MCP','Angle': angle_deg_p173})
    writer.writerow({'Pose': '27_3', 'Joint name' : 'R -Finger_3 - Extension MCP','Angle': angle_deg_p174})

    writer.writerow({'Pose': '29_0', 'Joint name' : 'R -Finger_0 - Flexion PIP','Angle': angle_deg_p181})
    writer.writerow({'Pose': '29_1', 'Joint name' : 'R -Finger_1 - Flexion PIP','Angle': angle_deg_p182})
    writer.writerow({'Pose': '29_2', 'Joint name' : 'R -Finger_2 - Flexion PIP','Angle': angle_deg_p183})
    writer.writerow({'Pose': '29_3', 'Joint name' : 'R -Finger_3 - Flexion PIP','Angle': angle_deg_p184})

    writer.writerow({'Pose': '31_0', 'Joint name' : 'R -Finger_0 - Extension PIP','Angle': angle_deg_p191})
    writer.writerow({'Pose': '31_1', 'Joint name' : 'R -Finger_1 - Extension PIP','Angle': angle_deg_p192})
    writer.writerow({'Pose': '31_2', 'Joint name' : 'R -Finger_2 - Extension PIP','Angle': angle_deg_p193})
    writer.writerow({'Pose': '31_3', 'Joint name' : 'R -Finger_3 - Extension PIP','Angle': angle_deg_p194})

    writer.writerow({'Pose': '33_0', 'Joint name' : 'R -Finger_0 - Flexion DIP','Angle': angle_deg_p201})
    writer.writerow({'Pose': '33_1', 'Joint name' : 'R -Finger_1 - Flexion DIP','Angle': angle_deg_p202})
    writer.writerow({'Pose': '33_2', 'Joint name' : 'R -Finger_2 - Flexion DIP','Angle': angle_deg_p203})
    writer.writerow({'Pose': '33_3', 'Joint name' : 'R -Finger_3 - Flexion DIP','Angle': angle_deg_p204})

    writer.writerow({'Pose': '35_0', 'Joint name' : 'R -Finger_0 - Extension DIP','Angle': angle_deg_p211})
    writer.writerow({'Pose': '35_1', 'Joint name' : 'R -Finger_1 - Extension DIP','Angle': angle_deg_p212})
    writer.writerow({'Pose': '35_2', 'Joint name' : 'R -Finger_2 - Extension DIP','Angle': angle_deg_p213})
    writer.writerow({'Pose': '35_3', 'Joint name' : 'R -Finger_3 - Extension DIP','Angle': angle_deg_p214})

######################################################################################

    writer.writerow({'Pose': '37','Joint name' : 'L -Wrist - Flexion','Angle': angle_deg_p01r})
    writer.writerow({'Pose': '39','Joint name' : 'L -Wrist - Extension', 'Angle': angle_deg_p23r})
    writer.writerow({'Pose': '41','Joint name' : 'L -Wrist - Radial Deviation', 'Angle': angle_deg_p45r})
    writer.writerow({'Pose': '43', 'Joint name' :'L -Wrist - Ulnar Deviation' ,'Angle': angle_deg_p67r})
    writer.writerow({'Pose': '45', 'Joint name' :'L -Thumb - Radial Abduction' ,'Angle': angle_deg_p8r})
    writer.writerow({'Pose': '47', 'Joint name' : 'L -Thumb - Ulnar Abduction', 'Angle': angle_deg_p9r})
    writer.writerow({'Pose': '49', 'Joint name' : 'L -Thumb - Palmer Abduction' ,'Angle': angle_deg_p10r})
    writer.writerow({'Pose': '51', 'Joint name' : 'L -Thumb - Palmer Abduction','Angle': angle_deg_p11r})
    writer.writerow({'Pose': '53', 'Joint name' : 'L -Thumb - Flexion MCP','Angle': angle_deg_p12r})
    writer.writerow({'Pose': '55', 'Joint name' : 'L -Thumb - Extension MCP','Angle': angle_deg_p13r})
    writer.writerow({'Pose': '57', 'Joint name' : 'L -Thumb - Flexion IP','Angle': angle_deg_p14r})
    writer.writerow({'Pose': '59', 'Joint name' : 'L -Thumb - Extension IP','Angle': angle_deg_p15r})

    writer.writerow({'Pose': '61_0', 'Joint name' : 'L -Finger_0 - Flexion MCP','Angle': angle_deg_p161r})
    writer.writerow({'Pose': '61_1', 'Joint name' : 'L -Finger_1 - Flexion MCP','Angle': angle_deg_p162r})
    writer.writerow({'Pose': '61_2', 'Joint name' : 'L -Finger_2 - Flexion MCP','Angle': angle_deg_p163r})
    writer.writerow({'Pose': '61_3', 'Joint name' : 'L -Finger_3 - Flexion MCP','Angle': angle_deg_p164r})

    writer.writerow({'Pose': '63_0', 'Joint name' : 'L -Finger_0 - Extension MCP','Angle': angle_deg_p171r})
    writer.writerow({'Pose': '63_1', 'Joint name' : 'L -Finger_1 - Extension MCP','Angle': angle_deg_p172r})
    writer.writerow({'Pose': '63_2', 'Joint name' : 'L -Finger_2 - Extension MCP','Angle': angle_deg_p173r})
    writer.writerow({'Pose': '63_3', 'Joint name' : 'L -Finger_3 - Extension MCP','Angle': angle_deg_p174r})

    writer.writerow({'Pose': '65_0', 'Joint name' : 'L -Finger_0 - Flexion PIP','Angle': angle_deg_p181r})
    writer.writerow({'Pose': '65_1', 'Joint name' : 'L -Finger_1 - Flexion PIP','Angle': angle_deg_p182r})
    writer.writerow({'Pose': '65_2', 'Joint name' : 'L -Finger_2 - Flexion PIP','Angle': angle_deg_p183r})
    writer.writerow({'Pose': '65_3', 'Joint name' : 'L -Finger_3 - Flexion PIP','Angle': angle_deg_p184r})

    writer.writerow({'Pose': '67_0', 'Joint name' : 'L -Finger_0 - Extension PIP','Angle': angle_deg_p191r})
    writer.writerow({'Pose': '67_1', 'Joint name' : 'L -Finger_1 - Extension PIP','Angle': angle_deg_p192r})
    writer.writerow({'Pose': '67_2', 'Joint name' : 'L -Finger_2 - Extension PIP','Angle': angle_deg_p193r})
    writer.writerow({'Pose': '67_3', 'Joint name' : 'L -Finger_3 - Extension PIP','Angle': angle_deg_p194r})

    writer.writerow({'Pose': '69_0', 'Joint name' : 'L -Finger_0 - Flexion DIP','Angle': angle_deg_p201r})
    writer.writerow({'Pose': '69_1', 'Joint name' : 'L -Finger_1 - Flexion DIP','Angle': angle_deg_p202r})
    writer.writerow({'Pose': '69_2', 'Joint name' : 'L -Finger_2 - Flexion DIP','Angle': angle_deg_p203r})
    writer.writerow({'Pose': '69_3', 'Joint name' : 'L -Finger_3 - Flexion DIP','Angle': angle_deg_p204r})

    writer.writerow({'Pose': '71_0', 'Joint name' : 'L -Finger_0 - Extension DIP','Angle': angle_deg_p211r})
    writer.writerow({'Pose': '71_1', 'Joint name' : 'L -Finger_1 - Extension DIP','Angle': angle_deg_p212r})
    writer.writerow({'Pose': '71_2', 'Joint name' : 'L -Finger_2 - Extension DIP','Angle': angle_deg_p213r})
    writer.writerow({'Pose': '71_3', 'Joint name' : 'L -Finger_3 - Extension DIP','Angle': angle_deg_p214r})

