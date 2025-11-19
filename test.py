import numpy as np
from tensorflow.keras.models import load_model
import cv2


def extract_histogram_features_fixed_resize(image_path, resize_shape=(200, 200), gray_levels=8, grid_size=(10, 10)):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, resize_shape)

    patch_h = resize_shape[0] // grid_size[0]
    patch_w = resize_shape[1] // grid_size[1]

    features = []

    grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = cv2.magnitude(grad_x, grad_y)

    gray_bin_size = 256 // gray_levels
    grad_max = gradient_magnitude.max()
    grad_bin_size = grad_max / gray_levels if grad_max != 0 else 1

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            y1, y2 = i * patch_h, (i + 1) * patch_h
            x1, x2 = j * patch_w, (j + 1) * patch_w

            patch = img[y1:y2, x1:x2]
            grad_patch = gradient_magnitude[y1:y2, x1:x2]

            hist_intensity, _ = np.histogram(patch, bins=gray_levels, range=(0, 256))
            hist_intensity = hist_intensity.astype(np.float32) / (patch.size + 1e-6)

            hist_grad, _ = np.histogram(grad_patch, bins=gray_levels, range=(0, grad_max))
            hist_grad = hist_grad.astype(np.float32) / (grad_patch.size + 1e-6)

            patch_features = np.concatenate([hist_intensity, hist_grad])
            features.append(patch_features)

    return np.concatenate(features)

model = load_model("best_model_lstm.keras")
class_names = ['Tumor', 'Stone', 'Normal', 'Cyst']
def test(img_path):
    features = extract_histogram_features_fixed_resize(img_path)  # خروجی: (1600,)
    features = features.reshape(1, 100, 16)
    prediction = model.predict(features)
    print("Prediction:", prediction)
    prediction = np.array(prediction)
    predicted_class = np.argmax(prediction)
    return class_names[predicted_class]

dataset = {
    'Cyst': "processed_images/Cyst/Cyst- (999).jpg",
    'Normal': "processed_images/Normal/Normal- (19).jpg",
    'Stone': "processed_images/Stone/Stone- (29).jpg",
    'Tumor': "processed_images/Tumor/Tumor- (39).jpg",
    'Cyst1': "processed_images/Cyst/Cyst- (1050).jpg",
    'Cyst2': "processed_images/Cyst/Cyst- (1060).jpg",
    'Cyst3': "processed_images/Cyst/Cyst- (1070).jpg",
    'Cyst4': "processed_images/Cyst/Cyst- (1080).jpg",
    'Cyst5': "processed_images/Cyst/Cyst- (1090).jpg",
    'Cyst6': "processed_images/Cyst/Cyst- (1100).jpg",
    'Stone1': "processed_images/Stone/Stone- (30).jpg",
    'Stone2': "processed_images/Stone/Stone- (40).jpg",
    'Stone3': "processed_images/Stone/Stone- (50).jpg",
    'Stone4': "processed_images/Stone/Stone- (60).jpg",
    'Normal1': "processed_images/Normal/Normal- (500).jpg",
    'Normal2': "processed_images/Normal/Normal- (550).jpg",
    'Normal3': "processed_images/Normal/Normal- (600).jpg",
    'Normal4': "processed_images/Normal/Normal- (650).jpg",
}

for img, path in dataset.items():
    print(f"image: {img}, prediction: {test(path)}")
