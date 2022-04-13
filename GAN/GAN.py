import torch 
from torch import nn
from torch.nn import functional as F
import torchvision.transforms as transforms
import cv2
import numpy as np
import random
from time import sleep

#PixelNormalization module
class PixelNorm(nn.Module):
    def forward(self, x):
        eps = 1e-8
        return x / ((torch.mean(x**2, dim=1, keepdims=True) + eps) ** 0.5)

#equalized leanring rate
class WeightScale(nn.Module):
    def forward(slef, x, gain=2):
        c = ((x.shape[1] * x.shape[2] * x.shape[3]) / 2)**0.5
        return x / c
    