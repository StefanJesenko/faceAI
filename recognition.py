import cv2
import torch
import torch.nn as nn
from torchvision import transforms
from model import face_ai_model
from PIL import Image
import torch.nn.functional as F

# Load the trained model
model = face_ai_model()
model.load_state_dict(torch.load('face_ai_model.pth'))
model.eval()

# Define the transformation for the input image
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Initialize the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Convert the frame to a PIL image
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Preprocess the frame
    input_image = transform(pil_image).unsqueeze(0)

    # Make prediction
    with torch.no_grad():
        output = model(input_image)
        probabilities = F.softmax(output, dim=1)
        face_confidence = probabilities[0][1].item()  # Assuming the face class is at index 1
    
    # Display the result
    confidence_text = f"Face Confidence: {face_confidence * 100:.2f}%"
    
    # Put the result text on the frame
    cv2.putText(frame, confidence_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close the window
cap.release()
cv2.destroyAllWindows()
