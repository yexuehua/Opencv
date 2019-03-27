# USAGE
# python drawing.py

# Import the necessary packages
import numpy as np
import cv2

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)    
# Draw a green line from the top-left corner of our canvas
# to the bottom-right
def drawline1(color=green):
    cv2.line(canvas, (0, 0), (300, 300), color)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(2500)

# Now, draw a 3 pixel thick red line from the top-right
# corner to the bottom-left
def drawline2(color=red):
    cv2.line(canvas, (300, 0), (0, 300), color, 3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(2500)

# Draw a green 50x50 pixel square, starting at 10x10 and
# ending at 60x60
def drawsquare(color=green):
    cv2.rectangle(canvas,(10, 10), (60, 60), color)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(2500)

# Draw another rectangle, this time we'll make it red and
# 5 pixels thick
def drawrect(color=red):
    cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(2500)

# Let's draw one last rectangle: blue and filled in
def drawrectfill(color=blue):
    cv2.rectangle(canvas, (200, 50), (225, 125), color, -1)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(2500)

# Reset our canvas and draw a white circle at the center
# of the canvas with increasing radii - from 25 pixels to
# 150 pixels
def drawcircle(color=white):
    canvas = np.zeros((300, 300, 3), dtype = "uint8")
    centerX, centerY = (canvas.shape[1] // 2, canvas.shape[0] // 2)
    for r in range(0, 175, 25):
        cv2.circle(canvas, (centerX, centerY), r, color)
    cv2.imshow("Canvas", canvas)

cv2.waitKey(2500)

# Let's go crazy and draw 25 random circles
def drawcrazy():
    for i in range(0, 25):
        # randomly generate a radius size between 5 and 200,
        # generate a random color, and then pick a random
        # point on our canvas where the circle will be drawn
        radius = np.random.randint(5, high = 200)
        color = np.random.randint(0, high = 256, size = (3,)).tolist()
        pt = np.random.randint(0, high = 300, size = (2,))
        # draw our random circle
        cv2.circle(canvas, tuple(pt), radius, color, -1)

    
    # Show our masterpiece
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(5000)
drawline1(blue)
drawline2()
drawrect()
drawrectfill()
drawsquare()
drawcircle(red)
drawcrazy()
