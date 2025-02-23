import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
from ultralytics import YOLO
from collections import deque


class CheatingDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exam Hall Cheating Detection")

        self.label = tk.Label(root, text="Choose an Option", font=("Arial", 14))
        self.label.pack()

        self.upload_btn = tk.Button(root, text="Upload Video", command=self.upload_video)
        self.upload_btn.pack()

        self.camera_btn = tk.Button(root, text="Use Camera", command=self.use_camera)
        self.camera_btn.pack()

        self.canvas = tk.Canvas(root, width=1280, height=720)  # Adjusted for Full HD video
        self.canvas.pack()

        self.cap = None
        self.video_source = None
        self.fps = 30

        # Load YOLOv8 model
        self.model = YOLO("yolov8n.pt")  # Pre-trained YOLO model
        self.tracked_hands = deque(maxlen=30)  # Track hand movements

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if file_path:
            self.video_source = file_path
            self.start_detection()

    def use_camera(self):
        self.video_source = 0
        self.start_detection()

    def start_detection(self):
        if self.cap:
            self.cap.release()

        self.cap = cv2.VideoCapture(self.video_source)
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS)) or 30
        self.detect_cheating()

    def detect_cheating(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (1280, 720))  # Adjusted for HD display
            results = self.model(frame)

            detected_hands = []
            for result in results:
                for box in result.boxes:
                    cls_id = int(box.cls.item())
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    label = self.model.names[cls_id]

                    if label == "person":
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    elif label in ["cell phone", "book", "laptop", "tablet"]:  # Expanded cheating tools
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.putText(frame, "Cheating Suspected!", (50, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    elif label == "hand":
                        detected_hands.append((x1, y1, x2, y2))
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Analyze hand movement
            self.tracked_hands.append(detected_hands)
            if len(self.tracked_hands) > 1:
                for (hx1, hy1, hx2, hy2) in detected_hands:
                    for (px1, py1, px2, py2) in self.tracked_hands[-2]:
                        if abs(hx1 - px1) > 30 or abs(hy1 - py1) > 30:  # Adjusted threshold for better accuracy
                            cv2.putText(frame, "Suspicious Hand Movement!", (50, 100),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)
                            break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas.img_tk = img_tk

        self.root.after(int(1000 / self.fps), self.detect_cheating)

    def __del__(self):
        if self.cap:
            self.cap.release()


if __name__ == "__main__":
    root = tk.Tk()
    app = CheatingDetectionApp(root)
    root.mainloop()

