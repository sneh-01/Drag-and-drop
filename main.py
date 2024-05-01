import cv2
from cvzone.HandTrackingModule import HandDetector
# from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 728)
detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)

    # Find the hand and its landmarks
    hands, img = detector.findHands(img)

    cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 255), cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


