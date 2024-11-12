import streamlit as st
import cv2,datetime,time

st.title("Motion Detector")
start = st.button("Start Camera")
now = datetime.datetime.now()
day = now.strftime("%A")
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    print(now.strftime("%A"))

    while True:
        hour = time.strftime("%H:%M:%S", time.localtime())

        check,frame = camera.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=f"{day}", org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),
                    thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=f"{hour}", org=(50,100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),
                    thickness=2,lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)