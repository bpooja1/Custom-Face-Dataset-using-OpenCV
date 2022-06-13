import tkinter as tk
import os
import cv2

current_dir = os.getcwd()

#argument 0 is given to use the default camera of the laptop
camera = cv2.VideoCapture(0)

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()

#creating a list of lables "You could add as many you want"
Labels = ["Ashok","Rohit"]

#Now create folders for each label to store images
for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)

for folder in Labels:
    #using count variable to name the images in the dataset.
    count = 0
    #Taking input to start the capturing
    print("Press 's' to start data collection for"+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()

    #clicking 200 images per label, you could change as you want.    
    while count<10:
        #read returns two values one is the exit code and other is the frame
        status, frame = camera.read()
        #check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break

        #convert the image into gray format for fast caculation
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1,9)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0),5)
            faces = frame[y:y + h, x:x + w]
            new_img = cv2.resize(faces, (w, h))

        #display window with gray image
        cv2.imshow("Video Window",frame)

        #convert the image into gray format for fast caculation
        save_image = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

        #Store the image to specific label folder
        cv2.imwrite('/Users/poojabajagain/Downloads/Test/'+folder+'/'+str(count)+'.png',save_image)
        count=count+1

        #to quite the display window press 'q'
        if cv2.waitKey(1) == ord('q'):
            break
# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()