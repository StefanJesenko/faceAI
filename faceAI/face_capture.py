import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define transformations for the input data
transformations = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Load the dataset
dataset = datasets.ImageFolder(root='path_to_celeba_dataset', transform=transformations)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
