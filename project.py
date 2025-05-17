import cv2
import imutils
import pytesseract

# Ensure the correct path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image = cv2.imread('test1.jpg')
if image is None:
    print("Image not found!")
    exit()

image = imutils.resize(image, width=300)
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)

# Apply bilateral filter for smoothing
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
cv2.imshow("Smoothened Image", gray_image)
cv2.waitKey(0)

# Edge detection
edged = cv2.Canny(gray_image, 30, 200)
cv2.imshow("Edged Image", edged)
cv2.waitKey(0)

# Find contours
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours
image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
cv2.imshow("All Contours", image1)
cv2.waitKey(0)

# Sort contours based on area and keep the top 30
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

# Draw top 30 contours
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
cv2.imshow("Top 30 Contours", image2)
cv2.waitKey(0)

# Initialize variables
screenCnt = None
i = 7

# Loop over contours to find the license plate
for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)

    if len(approx) == 4:
        screenCnt = approx
        x, y, w, h = cv2.boundingRect(c)
        new_img = image[y:y+h, x:x+w]
        cv2.imwrite(f'./{i}.png', new_img)
        i += 1
        break

# If no plate is detected
if screenCnt is None:
    print("No license plate detected.")
    cv2.destroyAllWindows()
    exit()

# Draw the detected license plate contour
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Detected License Plate", image)
cv2.waitKey(0)

# Read the cropped license plate image
Cropped_loc = './7.png'
cropped_img = cv2.imread(Cropped_loc)
cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)

# Extract text from the license plate
plate = pytesseract.image_to_string(cropped_img, lang='eng')
print("Number plate is:", plate)

cv2.destroyAllWindows()
