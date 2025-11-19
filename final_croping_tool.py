import cv2
import numpy as np
import os

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

def process_image(image_path, save_path):
    # Read grayscale image
    image = cv2.imread(image_path, 0)
    if image is None:
        print(f"Failed to load {image_path}")
        return

    # Threshold to binary
    _, binary = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

    # Connected components
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(binary)

    if num_labels <= 1:
        print(f"No foreground found in {image_path}")
        return
    # print("Component areas (excluding background):", stats[1:, cv2.CC_STAT_AREA])
    # Find largest connected component ignoring background
    largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    x, y, w, h, area = stats[largest_label]

    # Extract ROI
    roi = image[y:y+h, x:x+w]

    # Blackout corners
    # roi = blackout_corners(roi, size=corner_size)

    # Save processed image
    cv2.imwrite(save_path, roi)
    print(f"Processed and saved: {save_path}")

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Supported image extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            process_image(input_path, output_path)

# Usage example:
input_folder = "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone"
output_folder = "processed_images"
slist = ["Normal", "Stone", "Tumor"]
for i in slist:
    process_folder(f"{input_folder}/{i}", f"{output_folder}/{i}")
