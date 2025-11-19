# import cv2
# import  numpy as np
# def crop_black_borders(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)
#     img[(img >= 250) & (img <= 255)] = 0
#     coords = cv2.findNonZero(thresh)
#     x, y, w, h = cv2.boundingRect(coords)
#     cropped = img[y:y+h, x:x+w]
#     return cropped
# def crop_black_borders(img):
#     # Remove white-ish pixels by setting them to black
#     mask = np.all((img >= 140) & (img <= 255), axis=2)
#     img[mask] = [0, 0, 0]

#     # Convert to grayscale and threshold to isolate non-black areas
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)

#     # Find bounding box of non-black area
#     coords = cv2.findNonZero(thresh)
#     if coords is not None:
#         x, y, w, h = cv2.boundingRect(coords)
#         cropped = img[y:y+h, x:x+w]
#         return cropped
#     else:
#         return img  # Return original if no non-black pixels found

# --- Load, crop, and save image ---
# def crop_black_and_white_borders(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     # Keep only pixels with intensity between 6 and 249
#     mask = cv2.inRange(gray, 10, 240)
    
#     coords = cv2.findNonZero(mask)
#     if coords is None:
#         return img  # fallback: no content found
    
#     x, y, w, h = cv2.boundingRect(coords)
#     cropped = img[y:y+h, x:x+w]
#     return cropped
# def crop_black_borders_clean(img):
#     # Step 1: Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Step 2: Zero out near-white pixels (to suppress bright noise)
#     mask = (gray >= 250)
#     gray[mask] = 0  # remove white lines

#     # Step 3: Apply a binary threshold to find content
#     _, thresh = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY)

#     # Step 4: Morphological opening to remove small noise (bright specks)
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#     cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

#     # Step 5: Find bounding box of non-zero regions
#     coords = cv2.findNonZero(cleaned)
#     if coords is not None:
#         x, y, w, h = cv2.boundingRect(coords)
#         cropped = img[y:y+h, x:x+w]
#         return cropped
#     else:
#         return img  # fallback: no content found

# def crop_main_content_shape_filtered(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Keep mid-range intensity pixels only
#     cleaned = cv2.inRange(gray, 6, 249)

#     # Find connected components
#     num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(cleaned, connectivity=8)

#     # Create mask for components that meet shape criteria
#     mask = np.zeros_like(cleaned)

#     for i in range(1, num_labels):  # skip background
#         x, y, w, h, area = stats[i]

#         aspect_ratio = min(w / h, h / w)  # e.g., 0.5 is a square-ish shape

#         if (w >= 50 and h >= 50):
#             mask[labels == i] = 255
        
#         else:
#             mask[labels == i] = 0

#     coords = cv2.findNonZero(mask)
#     if coords is None:
#         return img  # fallback

#     x, y, w, h = cv2.boundingRect(coords)
#     return img[y:y+h, x:x+w]


# # Path to your image file
# input_path = 'CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Normal/Normal- (5).jpg'
# output_path = 'cropped_output_img5.jpg'

# # Read image
# image = cv2.imread(input_path)

# # Check if image is loaded successfully
# if image is None:
#     print(f"Error: Could not load image at {input_path}")
# else:
#     # Crop black borders
#     cropped_image = crop_main_content_shape_filtered(image)

#     # Save the cropped image
#     cv2.imwrite(output_path, cropped_image)
#     print(f"Cropped image saved to {output_path}")
import cv2
import numpy as np

image = cv2.imread("CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Normal/Normal- (5).jpg", 0)  # Grayscale
_, binary = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(binary)

# Ignore background
print("Component areas (excluding background):", stats[1:, cv2.CC_STAT_AREA])
for i, area in enumerate(stats[1:, cv2.CC_STAT_AREA], start=1):
    print(f"Label {i}: Area = {area}")

largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
print(f"Largest label: {largest_label}")
x, y, w, h, area = stats[largest_label]
# def blackout_corners(img, size=30):
#     h, w = img.shape[:2]

#     # Top-left corner
#     img[0:size, 0:size] = 0

#     # Top-right corner
#     img[0:size, w-size:w] = 0

#     # Bottom-left corner
#     img[h-size:h, 0:size] = 0

#     # Bottom-right corner
#     img[h-size:h, w-size:w] = 0

#     return img
roi = image[y:y+h, x:x+w]
# roi = blackout_corners(roi, size=30)  # size = how deep the black corner goes

cv2.imwrite("newimg5.jpg", roi)