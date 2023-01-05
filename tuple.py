_x_minDist = 5
_y_minDist = 6
_z_minDist = 9

minDist = [_x_minDist, _y_minDist, _z_minDist]
minDistTxt = [(str(x) + ', ') for x in minDist]
print("Min Distance = " + ''.join(minDistTxt))

pos3d1 = [1, 2, 3]
pos3d1Txt = [(str(x) + ', ') for x in pos3d1]
print("First Obj Position = " + ''.join(pos3d1Txt))

pos3d2 = [10, 20, 30]
pos3d2Txt = [(str(x) + ', ') for x in pos3d2]
print("Second Obj Position = " + ''.join(pos3d2Txt))


pos3dDistance = [(max(pos3d1[x], pos3d2[x]) - min(pos3d1[x], pos3d2[x])) for x in range(0, len(pos3d1))]
pos3dDistanceTxt = [(str(x) + ', ') for x in pos3dDistance]
print("Distance = " + ''.join(pos3dDistanceTxt))

if pos3dDistance[0] < _x_minDist:
    print("overlap in x dimension")
elif pos3dDistance[1] < _y_minDist:
    print("overlap in x dimension")
elif pos3dDistance[2] < _z_minDist:
    print("overlap in x dimension")
else:
    print("no overlap in the 3d space!!!")