import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.haarcascades')
smile_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_smile.haarcascades')

# 設定 img 位置
#img = cv2.imread('./image/test.jpg')
img = cv2.imread('./image/people.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 畫出每一個臉的範圍
faces = face_cascade.detectMultiScale(
    gray,  # 待檢測圖片,一般設定灰度圖像可以加快檢測數度
    scaleFactor=1.1,  # 檢測粒度,若粒度增加會加速檢測速度,但會影響準確率
    minNeighbors=10,  # 每個目標至少要檢測到幾次以上,才被認定是真數據
    minSize=(30, 30),  # 數據搜尋的最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE

)
# 在臉部周圍畫矩形框
for (x, y, w, h) in faces:
    # 繪文字putText(來源, 文字, 左下座標, 字型大小, 文字顏色, 文字線條寬度)
    #cv2.putText(img, 'Anika', (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 255, 0), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)

    roi_gray = gray[y:y + h, x:x + w]
    roi_frame = img[y:y + h, x:x + w]

    # 獲取Smile (ROI(region of interest))
    smile = smile_cascade.detectMultiScale(
        roi_gray,  # 待檢測圖片，一般來說設定成灰度圖像可以加快檢測速度
        scaleFactor=1.1,  # 檢測粒度。若粒度增加會加速檢測速度，但會影響準確率
        minNeighbors=1,  # 每個目標至少要檢測到幾次以上，才被認定是真數據
        minSize=(30, 30),  # 數據搜尋的最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("smile:", len(smile), smile)
    for (sx, sy, sw, sh) in smile:
            cv2.putText(roi_frame, 'smile', (sx, sy - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(roi_frame, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 5)

print("face:",len(faces), faces)

cv2.imshow('Face',img)
#按任意鍵離開
c= cv2.waitKey(0)
