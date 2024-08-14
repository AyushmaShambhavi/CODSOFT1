import cv2
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import os
import csv
import time
from datetime import datetime

from win32com.client import Dispatch

def speak(strl):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(strl)

# Initialize video capture and face detection
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")

# Load face data and labels
face_data_path = 'dataset/faces_data.pkl'
labels_path = 'dataset/labels.pkl'

if not os.path.exists(face_data_path) or not os.path.exists(labels_path):
    print(f"Error: {face_data_path} or {labels_path} not found.")
    exit()

with open(face_data_path, 'rb') as f:
    faces_data = pickle.load(f)
with open(labels_path, 'rb') as f:
    labels = pickle.load(f)

# Convert lists to numpy arrays
faces_data = np.array(faces_data)
labels = np.array(labels)

# Debug: Print the shape of faces_data and labels to ensure they are correct
print("Faces data shape:", faces_data.shape)
print("Labels shape:", labels.shape)

# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(faces_data, labels)

imgbackground = cv2.imread("background.png")
COL_NAMES = ['NAME', 'TIME']

# Ensure the Attendance directory exists
os.makedirs("Attendance", exist_ok=True)

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        
        # Debug: Print the shape of resized_img to ensure it matches the training data
        print("Resized image shape:", resized_img.shape)
        
        output = knn.predict(resized_img)
        
        # Debug: Print the predicted output
        print("Predicted output:", output)
        
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        csv_file_path = f"Attendance/Attendance_{date}.csv"
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        attendance = [str(output[0]), str(timestamp)]

    # Resize the frame to match the target area in the background image
    resized_frame = cv2.resize(frame, (436, 633))
    
    # Place the resized frame into the background image
    imgbackground[51:51+633, 787:787+436] = resized_frame

    cv2.imshow("Frame", imgbackground)
    
    k = cv2.waitKey(1)
    if k == ord('o'):
        speak("Attendance Taken..")
        time.sleep(5)
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not os.path.isfile(csv_file_path) or os.stat(csv_file_path).st_size == 0:
                writer.writerow(COL_NAMES)
            writer.writerow(attendance)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("Video capture ended.")
