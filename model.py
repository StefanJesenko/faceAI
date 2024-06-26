import torch
import torch.nn as nn



class face_ai_model(nn.Module):
    def __init__(self, num_classes=2):
        super(face_ai_model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(in_features=64 * 56 * 56, out_features=1000)
        self.fc2 = nn.Linear(in_features=1000, out_features=num_classes)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 64 * 56 * 56)  
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    
