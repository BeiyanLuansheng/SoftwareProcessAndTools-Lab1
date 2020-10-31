import torch
import image
import network
import os

IMAGE_PATH = "./digit.jpg"
model = torch.load("./model.pkl")
pred = image.predict(model=model, image=image.get_image(image_path=IMAGE_PATH))
os.system('cls')
print("The number in the picture is : ", pred.idxmax()[0])
input()