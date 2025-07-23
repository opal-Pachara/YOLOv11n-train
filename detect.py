from ultralytics import YOLO

model = YOLO('yolo11n.pt')

result = model("C:/Users/opal_/OneDrive/Desktop/yolov11n/test/08a0dce0-06a3-11ee-b704-e11b1c7d3a39_original.jpg")
result[0].show()







