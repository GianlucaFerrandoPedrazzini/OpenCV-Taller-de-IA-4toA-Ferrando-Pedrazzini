import cv2 as cv

img = cv.imread('hollow knight.jpeg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape
 
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),180,1)
dst = cv.warpAffine(img,M,(cols,rows))
antes = cv.imread('hollow knight.jpeg')

cv.imshow("Imagen rotada antes", antes)
cv.imshow("Imagen rotada después", dst)
cv.waitKey(0)
cv.destroyAllWindows()