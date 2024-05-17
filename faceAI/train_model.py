import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from model import LeNet  
import torchvision.datasets as datasets
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

train_dataset = datasets.ImageFolder(root='./data/train', transform=transform)
valid_dataset = datasets.ImageFolder(root='./data/valid', transform=transform)
test_dataset = datasets.ImageFolder(root='./data/test', transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
valid_loader = DataLoader(valid_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

model = LeNet()

criterion = nn.BCELoss()  
optimizer = optim.Adam(model.parameters(), lr=0.001)  

num_epochs = 10
for epoch in range(num_epochs):
    total_loss = 0.0
   
    model.train()  
    for i, (inputs, labels) in enumerate(train_loader):
        optimizer.zero_grad()  

        outputs = model(inputs) 
        loss = criterion(outputs, labels.float().unsqueeze(1)) 
        loss.backward() 
        optimizer.step()

        total_loss += loss.item()
        
        if (i+1) % 100 == 0:  # Print every 100 mini-batches
            print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

    average_loss = total_loss / len(train_loader)
    print(f'Epoch [{epoch+1}/{num_epochs}], Train Loss: {average_loss:.4f}')

    model.eval()
    with torch.no_grad():  
        total_correct = 0
        total_samples = 0
        for inputs, labels in valid_loader:
            outputs = model(inputs)
            predicted = torch.round(outputs)  
            total_correct += (predicted == labels.unsqueeze(1)).sum().item()
            total_samples += labels.size(0)
        accuracy = total_correct / total_samples
        print(f'Epoch [{epoch+1}/{num_epochs}], Validation Accuracy: {accuracy:.4f}')

print('Training complete!')
