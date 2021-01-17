import cv2
import numpy as np

# Create a function based on left button down
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),10)

# Open Image
img = cv2.imread('dog_backpack.jpg')

# This names the window for reference 
cv2.namedWindow(winname='dogpack')

# Connects the mouse button to the function
cv2.setMouseCallback('dogpack',draw_circle)

while True: 
    # Shows the image window
    cv2.imshow('dogpack',img)
    # Exit on 'Esc' key down
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
# Closes all windows
cv2.destroyAllWindows()
