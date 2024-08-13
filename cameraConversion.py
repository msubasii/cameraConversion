
#this code :
#simuntaneously mirrors the frames in the video and 
#convert to black and white and save it as savedVideo.avi

import cv2 as cv;

#opening camera
camera = cv.VideoCapture(0)

frame_width = int(camera.get(3)) 
frame_height = int(camera.get(4)) 
   
size = (frame_width, frame_height) 
result = cv.VideoWriter('materials\\savedVideo.mp4',cv.VideoWriter_fourcc(*'mp4v'),10,size) 

while(True): 

    ret, frame = camera.read()
    im_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', im_gray)
    #mirroring the image
    im_gray = cv.flip(im_gray, 1)
    im_gray = cv.cvtColor(im_gray, cv.COLOR_GRAY2BGR)
    #saves the image 
    result.write(im_gray)

    if cv.waitKey(1) & 0xFF == ord('q'): 
        break

#this will close the camera when you press close
camera.release() 
cv.destroyAllWindows()

print("Video saved as savedVideo.mp4")