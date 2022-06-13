from tkinter import Frame
import cv2
import os


current_dir = os.getcwd()
if not os.path.exists(current_dir + '/training_images/'):
    os.mkdir(current_dir + '/training_images/')

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

# To use a video file as input
#cap = cv2.VideoCapture('/Users/poojabajagain/Downloads/filename.mov')
img_counter = 0

while True:
    # Read the frame
    ret, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1,9)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0),5)
        faces = img[y:y + h, x:x + w]
        new_img = cv2.resize(faces, (w, h))
        cv2.imshow("face",img)

    if not ret:
        print("failed to grab frame")
        break
    #cv2.imshow("test",img)

    k = cv2.waitKey(1)
    if k %256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        name = current_dir + '/training_images/user' + str(img_counter) + '.png'
        print('Creating...' + name)
        save_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(name, save_img)
        print("{} written!".format(name))
        img_counter += 1
        
#Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()