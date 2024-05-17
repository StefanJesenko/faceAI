import os
import random
import shutil

# Define source and target directories
source_train_dir = './data/train'
target_valid_dir = './data/test'

# Create validation directory if it doesn't exist
os.makedirs(target_valid_dir, exist_ok=True)

# Get list of JPG files in the train directory
train_files = [f for f in os.listdir(source_train_dir) if f.endswith('.jpg')]

# Calculate number of files to move for validation (10%)
num_files_to_move = int(0.1 * len(train_files))

# Randomly select files to move
files_to_move = random.sample(train_files, num_files_to_move)

# Move selected files to validation directory
for file in files_to_move:
    src = os.path.join(source_train_dir, file)
    dst = os.path.join(target_valid_dir, file)
    shutil.move(src, dst)

print(f"{num_files_to_move} JPG files moved from train to validation folder.")
