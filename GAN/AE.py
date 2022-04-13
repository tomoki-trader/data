import os
import matplotlib.pyplot as plt # 可視化
import numpy as np # 計算
import torch # 機械学習フレームワークとしてpytorchを使用
import torch.nn as nn # クラス内で利用するモジュールのため簡略化
import torch.nn.functional as F # クラス内で利用するモジュールのため簡略化
from torch import optim # 最適化アルゴリズム
from torch.utils.tensorboard import SummaryWriter # tensorboardの利用
from torchvision import datasets, transforms # データセットの準備

#tensorboad 保存先
if not os.pathexists("./logs"):
    os.mkdirs("./logs")

#transform = transforms.Compose([transforms.To])
train_datasets = datasets.MNIST("./", train=True, download=True, transform=transforms.ToTensor())
#train_loader = torch.utils.data.Dataloader(train_datasets, batch_size=16, shuffle=True)
