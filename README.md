# Automatic-Number-Plate-Detection-System
This project implements an automated system for detecting and recognizing vehicle license plates from images using OpenCV and Tesseract OCR. The system processes the input image to detect contours, isolates the license plate, and extracts the text using Optical Character Recognition (OCR).

Key Features:
- Image Preprocessing: Resizes, converts to grayscale, and smooths the image using bilateral filtering for edge detection.
- Contour Detection: Finds and sorts contours to identify the license plate region.
- License Plate Extraction: Isolates the license plate area and crops the image for further processing.
- Text Recognition: Uses Tesseract OCR to extract and display the license plate text from the cropped image.
- Visual Output: Displays various stages of image processing (original, grayscale, smoothed, contours, and detected plate).
Technologies Used:
- Python (OpenCV, Pytesseract, Imutils)
- Tesseract OCR for text recognition

