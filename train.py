from ultralytics import YOLO

model = YOLO('yolo11n.pt')

train_results = model.train(
    data="Data/data2.yaml",  # Path to dataset configuration file
    epochs=100,  # Number of training epochs
    imgsz=418,  # Image size for training
    device=0,
    workers=0  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
)

mertrics = model.val()