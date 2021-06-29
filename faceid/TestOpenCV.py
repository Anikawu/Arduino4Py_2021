import cv2
#設定 webcam 位置

cap= cv2.VideoCapture(0)

#設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1024)#800,640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,768)#600,480

while True:
    #捕捉 fram-by-fram
    #ret: 讀到的fram若是正確會回傳true
    #fram:捕捉到的區域資料
    ret, frame=cap.read()
    print(ret,frame)
    #顯示在 fram UI上面
    cv2.imshow('My Video', frame)
    #按下 q 離開迴圈  waitKey(1)代表1秒鐘
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

#釋放資源
cap.release()