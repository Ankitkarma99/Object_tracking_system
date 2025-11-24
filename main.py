import ultralytics

import cv2
from ultralytics import YOLO

def track(path):
    model = YOLO("yolo11n.pt")
    cap = cv2.VideoCapture(path)
    ret = True
    while ret :
        ret,frame = cap.read()

        if ret:
            result = model.track(frame, persist = True)
            result_frame = result[0].plot()
            cv2.imshow("Video", result_frame)

            if cv2.waitKey(1) & 0xFF==ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

track("vid2.mp4")