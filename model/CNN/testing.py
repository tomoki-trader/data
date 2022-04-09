from pyexpat import model
from Res import *
import torch

model = ResNet(block, 1000)
x = torch.rand(4, 3, 224, 224)

X_shape = model(x).shape
print(X_shape)