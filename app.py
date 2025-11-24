import streamlit as st
import cv2
from ultralytics import YOLO
import os

st.title("Object Tracking System")

file = st.file_uploader('Upload Video')
if file:
    data = file.read()
    with open('temp.mp4', 'wb') as f:
        f.write(data)
    cap = cv2.VideoCapture('temp.mp4')

    if cap:
        model = YOLO('yolo11n.pt')
        frame_destroyer = st.empty()
        ret = True
        while ret:
            ret, frame = cap.read()
            if ret:
                result = model.track(frame)
                result_frame = result[0].plot()
                img = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
                frame_destroyer.image(img)
    cap.release()
    os.remove('temp.mp4')