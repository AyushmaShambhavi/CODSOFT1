import cv2
import os
import pickle


video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("model/haarcascade_frontalface_default.xml")


name = input("Enter the name: ")
print(f"Name entered: {name}")


if not os.path.exists('dataset'):
    os.makedirs('dataset')


face_data_path = os.path.join('dataset', 'faces_data.pkl')
labels_path = os.path.join('dataset', 'labels.pkl')


if os.path.exists(face_data_path) and os.path.exists(labels_path):
    with open(face_data_path, 'rb') as f:
        faces_data = pickle.load(f)
    with open(labels_path, 'rb') as f:
        labels = pickle.load(f)
else:
    faces_data = []
    labels = []

i = 0

print("Collecting faces. Press 'q' to quit or collect 100 faces.")

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50))
        flattened_img = resized_img.flatten()

        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(flattened_img)
            labels.append(name)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
    
    cv2.putText(frame, f'Faces: {len(faces_data)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow("Frame", frame)
    
    i += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q') or len(faces_data) == 100:
        break


with open(face_data_path, 'wb') as f:
    pickle.dump(faces_data, f)
with open(labels_path, 'wb') as f:
    pickle.dump(labels, f)

video.release()
cv2.destroyAllWindows()
print(f"Face data and labels saved to {face_data_path} and {labels_path}")
