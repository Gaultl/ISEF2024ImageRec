# Standard imports
import cv2 as cv
import numpy as np

# Read image
# im = cv.imread(r"C:\Users\laure\Pictures\longBlobs.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5756.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3588.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3587.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_3585.PNG", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\16072.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Pictures\QSYSLongBlobs.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5478.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5477.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\IMG_5476.jpg", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A018 - 20241019_225011.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A019 - 20241019_225120.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A020 - 20241019_225122.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A021 - 20241019_225129.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A022 - 20241019_225132.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A023 - 20241019_225143.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite\A024 - 20241019_225146.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A034 - 20241020_102804.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A035 - 20241020_102817.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A036 - 20241020_102819.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A037 - 20241020_102821.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A038 - 20241020_102822.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A039 - 20241020_102824.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A040 - 20241020_102826.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A041 - 20241020_102829.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A042 - 20241020_102831.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Downloads\dino_lite_2\A043 - 20241020_102833.bmp", 0)
# im = cv.imread(r"C:\Users\laure\Pictures\CroppedA041 - 20241020_102829.bmp", 0)
height, width = im.shape

params = cv.SimpleBlobDetector_Params()

color = 255

ret,thresh1 = cv.threshold(im,100,255,cv.THRESH_BINARY)
# params.minThreshold = 20
# params.maxThreshold = 255

params.filterByArea = True
params.minArea = 5
params.maxArea = 10000

params.filterByColor = True
params.blobColor = 255

params.filterByCircularity = False
# params.minCircularity = 0.785
# params.maxCircularity = 1

params.filterByInertia = True
params.minInertiaRatio = .001
params.maxInertiaRatio = 10


detector = cv.SimpleBlobDetector_create(params)

# down_width = int(width)
# down_height = int(height)
# down_points = (down_width, down_height)
# resized_down = cv.resize(im, down_points, interpolation= cv.INTER_LINEAR)

# Detect blobs.
keypoints = detector.detect(thresh1)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
blank = np.zeros((1, 1))
blobs = cv.drawKeypoints(thresh1, keypoints, blank, (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

down_width = int(width)
down_height = int(height)
down_points = (down_width, down_height)
resized_down = cv.resize(blobs, down_points, interpolation= cv.INTER_LINEAR)

print(len(keypoints))

# Show keypoints
cv.imshow("Blobs Using Color", resized_down)
cv.waitKey(0)
cv.destroyAllWindows()
