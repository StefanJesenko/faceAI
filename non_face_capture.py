import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import os
import requests, zipfile, io, os
from torchvision.datasets.folder import ImageFolder
from tqdm import tqdm

# Download and extract Tiny ImageNet
url = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
print("Starting download of Tiny ImageNet dataset...")
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))
block_size = 1024
t = tqdm(total=total_size, unit='iB', unit_scale=True)

with open('tiny-imagenet-200.zip', 'wb') as file:
    for data in response.iter_content(block_size):
        t.update(len(data))
        file.write(data)
t.close()
print("Download completed.")

print("Extracting Tiny ImageNet dataset...")
with zipfile.ZipFile('tiny-imagenet-200.zip', 'r') as z:
    z.extractall('./data/tiny-imagenet-200')
print("Extraction completed.")

# Transform to resize images
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Load Tiny ImageNet dataset
tiny_imagenet_train = ImageFolder('./data/tiny-imagenet-200/train', transform=transform)
tiny_imagenet_loader = DataLoader(tiny_imagenet_train, batch_size=32, shuffle=True)

# Create directories for Tiny ImageNet images
os.makedirs('./data/train/non_face', exist_ok=True)
os.makedirs('./data/valid/non_face', exist_ok=True)
os.makedirs('./data/test/non_face', exist_ok=True)

# Save Tiny ImageNet images to appropriate directories
def save_tiny_imagenet_images():
    train_count = 80000  # 80% of 100,000
    valid_count = 10000  # 10% of 100,000
    test_count = 10000   # 10% of 100,000

    print("Processing and saving Tiny ImageNet images...")
    for idx, (images, labels) in enumerate(tiny_imagenet_loader):
        for i, image in enumerate(images):
            if idx * 32 + i >= train_count + valid_count + test_count:
                break
            image_pil = transforms.ToPILImage()(image)
            if idx * 32 + i < train_count:
                target_dir = './data/train/non_face'
            elif idx * 32 + i < train_count + valid_count:
                target_dir = './data/valid/non_face'
            else:
                target_dir = './data/test/non_face'
            image_pil.save(f'{target_dir}/tiny_imagenet_{idx * 32 + i}.png')
        if (idx + 1) % 100 == 0:
            print(f"Processed {idx * 32 + i} images")

save_tiny_imagenet_images()
print("Finished processing Tiny ImageNet images.")
