from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2
import threading

app = FastAPI()

# Load YOLO model
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

model = YOLO("YoloV8.pt")

# Camera stream
camera_url = 'http://192.168.1.6/cam-hi.jpg' #(NEED TO CHANGE!!!) Depend on your wifi, run the arduino IDE to the ESP32 cam to get the IP address

def generate_frames():
    cap = cv2.VideoCapture(camera_url)  # Open camera inside function to avoid global issues
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model.predict(frame, stream=True, verbose=False)

        for result in results:
            boxes = result.boxes
            annotator = Annotator(frame)

            for box in boxes:                                         
                r = box.xyxy[0]  # Bounding box coordinates                           
                c = box.cls  # Class index
                confidence = box.conf[0].item()  # Confidence score

                # Show confidence in terminal
                if confidence > 0.5:
                    print(f"Detected {model.names[int(c)]} with {confidence * 100:.2f}% confidence")

                # Draw bounding boxes
                annotator.box_label(r, label=model.names[int(c)], color=(0, 255, 0))

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.1.3", port=8000, log_level="info") #(NEED TO CHANGE!!!) Depend on your IP address, open cmd and ip config and copy the IPv4 Address to the host
