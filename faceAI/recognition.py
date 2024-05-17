import cv2
from pathlib import Path
import torch
from model import LeNet

def main():
    recognition()

def recognition():
    storage = {
        0: 'face'
    }
    storage_invert = {
        'face':0
    }

model_path = Path.home().joinpath('example')

model = LeNet.load_from_checkpoint(model_path)
model.eval()