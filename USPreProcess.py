import os

from PIL import Image
import numpy as np
import math


def de_noising(image_path, filter_threshold=20):
    # Load the image
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale

    # Convert image data to numpy array
    pixel_data = np.array(image)

    # Flatten the array to 1D
    # pixel_data = pixel_data.flatten()

    pixel_data[pixel_data < filter_threshold] = 0

    im = Image.fromarray(pixel_data)
    im.save(image_path)


def denoise_folder(folder_path, output_file='./output/output.txt', filter_threshold=20):
    # Open the output file
    with open(output_file, 'a') as file:
        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Construct full file path
                file_path = os.path.join(folder_path, filename)

                try:
                    # Calculate entropy
                    de_noising(file_path, filter_threshold=filter_threshold)
                    file.write(f"{filename}: Proceed with threshold = {filter_threshold}\n")
                    print(f"{filename}: Proceed with threshold = {filter_threshold}\n")

                    # Write the result to file
                    # file.write(f"{filename}: Shannon Entropy = {entropy} with threshold = {filter_threshold}\n")
                    # print(f"{filename}: Shannon Entropy = {entropy} with threshold = {filter_threshold}\n")

                except Exception as e:
                    print(f"Error processing {filename}: {e}")
        file.write("\n"*2)


if __name__ == "__main__":
    # Example usage
    # image_path = '../data/Selected/632.png'
    # image_path = '../data/Selected/1116.png'
    # image_path = '../data/Selected/1783.png'
    # image_path = '../data/Selected/2089.png'
    # entropy = calculate_entropy(image_path)

    filter_threshold = 20

    folder_path = './data/USImages/'
    output_file = os.path.join(folder_path, "output.txt")

    denoise_folder(folder_path, output_file, filter_threshold)
    # print(f"Shannon Entropy: {entropy}")


