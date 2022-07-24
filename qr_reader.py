from pyzbar.pyzbar import decode
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    decoded_qrs = decode(img)
    if len(decoded_qrs) > 0:
        #decoded_qrs[0].data is binary of our link
        print(decoded_qrs[0].data)

    cv2.imshow("code detector", img)
    if (cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()