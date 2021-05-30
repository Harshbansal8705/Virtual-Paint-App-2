import cv2
from HandTrackingModule import FindHands

eraser = cv2.imread("eraser.png")

cap = cv2.VideoCapture(0)
detector = FindHands(detection_con=0.75, tracking_con=0.75)

red = 0,0,255
blue = 255,0,0
green = 0,255,0
pink = 255,0,255
yellow = 0,255,255
white = 255,255,255
grey = 128,128,128
black = 0,0,0
brown = 19,69,139
orange = 0,165,255
purple = 128,0,128
violet = 238,130,238

total_points = []

color = black

while True:
    succeed, img = cap.read()
    imgCanvas = img.copy()
    imgCanvas[:] = (0,0,0)
    pos = detector.getPosition(img, [8], draw=False)
    if detector.middle_finger_up(img) and detector.index_finger_up(img):
        if len(pos) >= 1:
            if pos[0][1] < 50:
                positionX = pos[0][0]
                if positionX < 50:
                    color = red
                elif positionX >= 50 and positionX < 100:
                    color = blue
                elif positionX >= 100 and positionX < 150:
                    color = green
                elif positionX >= 150 and positionX < 200:
                    color = pink
                elif positionX >= 200 and positionX < 250:
                    color = yellow
                elif positionX >= 250 and positionX < 300:
                    color = white
                elif positionX >= 300 and positionX < 350:
                    color = grey
                elif positionX >= 350 and positionX < 400:
                    color = violet
                elif positionX >= 400 and positionX < 450:
                    color = brown
                elif positionX >= 450 and positionX < 500:
                    color = orange
                elif positionX >= 500 and positionX < 550:
                    color = purple
                elif positionX >= 550 and positionX < 590:
                    color = black
            if color != "eraser":
                cv2.circle(img, pos[0], 10, color, cv2.FILLED)
    else:
        cv2.circle(img, pos[0], 10, color, cv2.FILLED)
        total_points.append((color, pos[0]))
    for clr, pt in total_points:
        cv2.circle(imgCanvas, pt, 10, clr, cv2.FILLED)
    img[:50,:50] = red
    img[:50,50:100] = blue
    img[:50,100:150] = green
    img[:50,150:200] = pink
    img[:50,200:250] = yellow
    img[:50,250:300] = white
    img[:50,300:350] = grey
    img[:50,350:400] = violet
    img[:50,400:450] = brown
    img[:50,450:500] = orange
    img[:50,500:550] = purple
    img[:50,550:590] = eraser

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    combined = cv2.bitwise_and(img, imgInv)
    combined = cv2.bitwise_or(combined, imgCanvas)

    combined = cv2.flip(combined, 1)

    cv2.imshow("Virtual Paint 2", combined)

    k = cv2.waitKey(1)
    if k == ord('c'):
        total_points = []
    if k == ord('q'):
        break
