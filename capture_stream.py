import cv2
import sys

ip = sys.argv[1]

rtsp_url = f"rtsp://admin:admin%4012345@{ip}:554/cam/realmonitor?channel=1&subtype=0"

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Failed to open stream")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame failed")
        break

    cv2.imshow("LIVE", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()