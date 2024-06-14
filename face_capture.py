import os
import shutil
import torch
from sklearn.model_selection import train_test_split
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])


source_dir = './img_align_celeba/img_align_celeba'
target_dir = './data'


os.makedirs(target_dir, exist_ok=True)


images = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]


# Splitting data into train, validation, and test sets
train_files, temp_files = train_test_split(images, random_state=42)
valid_test_files, test_files = train_test_split(temp_files,  random_state=42)

# Further split 20% of the train data into validation and test sets
valid_files, test_files = train_test_split(valid_test_files, random_state=42)

def copy_files(files, split_type):
    split_dir = os.path.join(target_dir, split_type)
    os.makedirs(split_dir, exist_ok=True)
    for file in files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(split_dir, file))


copy_files(train_files, 'train')
copy_files(valid_files, 'valid')
copy_files(test_files, 'test')


train_dataset = datasets.ImageFolder(root='./data/train', transform=transform)
valid_dataset = datasets.ImageFolder(root='./data/valid', transform=transform)
test_dataset = datasets.ImageFolder(root='./data/test', transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
