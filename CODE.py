import cv2,mediapipe as mp,numpy as np
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.8,min_tracking_confidence=0.8)
mp_draw=mp.solutions.drawing_utils
colors=[(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
col_idx,draw_col=0,colors[0]
eraser_col=(0,0,0)
canvas=np.zeros((720,1280,3),np.uint8)
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
draw,erase=False,False
px,py=0,0
while True:
    ret,frame=cap.read()
    if not ret:break
    frame=cv2.flip(frame,1)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    res=hands.process(rgb)
    if res.multi_hand_landmarks:
        for hand in res.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
            ix,iy=int(hand.landmark[8].x*1280),int(hand.landmark[8].y*720)
            cv2.circle(frame,(ix,iy),10,draw_col,cv2.FILLED)
            tx,ty=int(hand.landmark[4].x*1280),int(hand.landmark[4].y*720)
            if np.hypot(ix-tx,iy-ty)<50:
                draw=True
                if px==0 and py==0:px,py=ix,iy
                col=eraser_col if erase else draw_col
                thick=30 if erase else 8
                cv2.line(canvas,(px,py),(ix,iy),col,thick)
                px,py=ix,iy
            else:
                draw=False
                px,py=0,0
            mx,my=int(hand.landmark[12].x*1280),int(hand.landmark[12].y*720)
            if np.hypot(ix-mx,iy-my)<50 and not erase:
                col_idx=(col_idx+1)%len(colors)
                draw_col=colors[col_idx]
                cv2.putText(frame,'Color Changed',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,draw_col,2)
            tips=[4,8,12,16,20]
            fingers=[1 if hand.landmark[tip].y<hand.landmark[tip-2].y else 0 for tip in tips[1:]]
            fingers.insert(0,1 if hand.landmark[4].x<hand.landmark[3].x else 0)
            erase=True if sum(fingers)==5 else False
            if erase:
                cv2.putText(frame,'Eraser Mode',(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    frame=cv2.addWeighted(frame,0.5,canvas,0.5,0)
    cv2.imshow('Notepad',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):break
cap.release()
cv2.destroyAllWindows()
