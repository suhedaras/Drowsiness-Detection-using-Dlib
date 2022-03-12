# Drowsiness Detection using Dlib
 Simple code in python to detect Drowsiness using Dlib. The user's status is decided according to the EAR and MOR values.


 
### Get this repo 

`git clone https://github.com/suhedaras/Drowsiness-Detection-using-Dlib.git`

`cd Drowsiness-Detection-using-Dlib`

### Dependencies

1. python==3.8
2. dlib==19.19.0	
3. opencv-python==4.5.5.62	
4. scipy==1.6.2

**Run this command for drowsy detection**

```
drowsiness_detection.py
```

**Change the threshold values according to your need. In this project, threshold values 0.70 and 0.22 were used.**

```
            if MOR > 0.70:
                cv2.putText(frame, "You are yawning. Are you drowsy?", (5, 75),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            if EAR < 0.22:
                flag += 1
                if flag > frame_check:
                    cv2.putText(frame, "DROWSINESS ALERT", (25, 125),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
```

## Result

   ![drowsy_detection](https://user-images.githubusercontent.com/73580507/158033336-86bb2a7c-1eeb-4742-83cf-a94565d7c870.gif)
