import torch.nn.functional as F
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 86)
        self.fc2 = nn.Linear(86, 86)
        self.fc3 = nn.Linear(86, 86)
        self.fc4 = nn.Linear(86, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)

model = NeuralNetwork()