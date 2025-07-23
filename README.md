# YOLOv11n-train

โปรเจกต์นี้ใช้ Ultralytics YOLO สำหรับงาน Object Detection

## วิธีติดตั้ง

1. ติดตั้ง PyTorch ที่รองรับ CUDA (เลือกเวอร์ชันให้ตรงกับเครื่อง)
   ```sh
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   # หรือถ้าใช้ CUDA 11.8
   # pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```
2. ติดตั้ง dependencies อื่น ๆ
   ```sh
   pip install -r requirements.txt
   ```

## การใช้งาน

- ตรวจจับวัตถุ:
  ```sh
  python detect.py
  ```
- เทรนโมเดล:
  ```sh
  python train.py
  ```

## หมายเหตุ
- ตรวจสอบว่าไฟล์โมเดล (เช่น yolo11n.pt) อยู่ในโฟลเดอร์เดียวกับ detect.py
- ปรับ path dataset และโมเดลให้ตรงกับเครื่องของคุณ 