import csv


fn = "hands_pose_direction_01.csv"


def description(pose_num, frame_num) :

    with open(fn) as f :
        reader = csv.reader(f)
        for row in reader :
            if row[0] == "direction"
                tx = row[1:]
                break
        return( tx[pose_num*2+frame_num] )
        
        







