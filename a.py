from ultralytics import YOLO
import cv2
import telepot
model = YOLO("yolov8n.pt")
results = model("rtsp://admin:admin1234@192.168.1.15:554/cam/realmonitor?channel=1&subtype=0",stream=True,show=True)
def show_frame():
    cv2.rectangle(frame,(0,0),(800,500),(255,0,0),10)
    cv2.imshow("show",frame)
    cv2.waitKey(1)
for result,frame in results:
    show_frame()
    boxes=result[0].boxes
    for box in boxes.numpy():
        x=(box.xyxy[0][0]+box.xyxy[0][2])/2
        y=int(box.xyxy[0][1])+int(box.xyxy[0][3])/2
        b=(0,0)[0]<x<(800,500)[0] and (0,0)[1]<y<(800,500)[1]
        if b:
            token = "6275415240:AAF3yDdT45-VIn8GdBrQUHH0XmtMXo0MC28"
            receiver_id=5877612764
            bot = telepot.Bot(token)
            bot.sendPhoto(receiver_id,photo=open("a121.jpg", "rb"),caption="Có xâm nhập, nguy hiêm!")
