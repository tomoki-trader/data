import torch
import torch.nn as nn
from .ResBlock import block 
        
class ResNet(nn.Module):
    def __init__(self, block, num_classes):
        super().__init__()

        #conv1
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)
        #paddingが１マス余ってもよい。
        #224*224*3 - 112*112*64
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2,padding=1)
        #112*112*64 - 56*56*64

        #conv2
        self.conv2_x = self._make_layer(block, 3, res_block_in_channels=64, first_conv_out_channels=64, stride=1)
        self.conv3_x = self._make_layer(block, 4, res_block_in_channels=256, first_conv_out_channels=128, stride=2)
        self.conv4_x = self._make_layer(block, 6, res_block_in_channels=512, first_conv_out_channels=256, stride=2)
        self.conv5_x = self._make_layer(block, 3, res_block_in_channels=1024, first_conv_out_channels=512, stride=2)
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))
        self.fc = nn.Linear(512*4, num_classes)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.conv2_x(x)
        x = self.conv3_x(x)
        x = self.conv4_x(x)
        x = self.conv5_x(x)
        x = self.avgpool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc(x)
        return x

    #慣例的に先頭アンダースコアはクラス内参照を意味する
    #class外の時はワイルドカードでimportできない。
    def _make_layer(self, block, num_res_blocks, res_block_in_channels, first_conv_out_channels, stride):
        layers = []

        identity_conv = nn.Conv2d(res_block_in_channels, first_conv_out_channels*4, kernel_size=1, stride=stride)
        layers.append(block(res_block_in_channels, first_conv_out_channels, identity_conv, stride))

        in_channels = first_conv_out_channels*4

        for i in range(num_res_blocks -1):
            layers.append(block(in_channels, first_conv_out_channels, identity_conv=None, stride=1))
        
        return nn.Sequential(*layers)
    
if __name__ == "__main__":
   print('ok resnet')

   