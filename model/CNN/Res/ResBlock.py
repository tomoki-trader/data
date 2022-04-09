import torch
import torch.nn as nn

class block(nn.Module):
    def __init__(self, first_conv_in_channels, first_conv_out_channels, identity_conv=None, stride=1):
        """Args: 
            first_conv_in_channels: input_channels
            first_conv_out_channels: output_channels
            identity_conv : tuning the number of channels

            """
        
        super().__init__()
        #[model_name].moduleの関数名で呼び出せるのがメリット。
        #instance varietyもselfをつけて呼び出せる。
        
        #first layer
        self.conv1 = nn.Conv2d(
            first_conv_in_channels, first_conv_out_channels, kernel_size=1, stride=1, padding=0)
        self.bn1 =nn.BatchNorm2d(first_conv_out_channels)

        #second layer
        self.conv2 = nn.Conv2d(first_conv_out_channels, first_conv_out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn2 = nn.BatchNorm2d(first_conv_out_channels)

        #third layer
        self.conv3 = nn.Conv2d(first_conv_out_channels, first_conv_out_channels*4, kernel_size=1, stride=1, padding=0)
        self.bn3 = nn.BatchNorm2d(first_conv_out_channels*4)
        self.relu = nn.ReLU()

        self.identity_conv = identity_conv

    def forward(self, x):
        identity = x.clone()

        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.bn3(x)
        #activation func uses concatenated data.
        if self.identity_conv is not None:
            identity = self.identity_conv(identity)
        
        x += identity
        x = self.relu(x)

        return x
        
if __name__ == "__main__":
    print('ok')
    