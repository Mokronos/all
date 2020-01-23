import matplotlib.pyplot as plt
import torchvision
import torch
import torch.nn as nn
import numpy as np
import torchvision.transforms as transforms
from torch.utils.data import Dataset

input_size = 20
output_size = 5
hidden_sizes = [100,100]
amount_samples = 2000
num_epochs = 2000
batch_size = int(1*amount_samples)
learning_rate = 0.00001


# data
#train_dataset = torchvision.datasets.MNIST(root="../../data",
#                                           train = True,
#                                           transform=transforms.ToTensor(),
#                                           download = True)
def tobit(x,dim):
    
    y = np.array([1 if digit=="1" else 0 for digit in bin(x)[2:]])
    return torch.from_numpy(np.pad(y,(dim-len(y),0),"constant")).float()

class NumbersDataset(Dataset):
    def __init__(self,input_size, output_size, amount_samples):
        np.random.seed(0)

        self.samples = torch.from_numpy(np.random.randint(2,size=(amount_samples,output_size))).float()


    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        inputs = tobit(idx,input_size)
        outputs = self.samples[idx]
        return inputs, outputs

train_test = NumbersDataset(input_size, output_size,amount_samples)

train_loader = torch.utils.data.DataLoader(dataset=train_test,
                                           batch_size=batch_size,
                                           shuffle=False)

test_loader = train_loader

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_sizes[0],'False') 
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_sizes[0], hidden_sizes[1],'False')  
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_sizes[1], output_size,'False')  

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu1(out)
        out = self.fc2(out)
        out = self.relu2(out)
        out = self.fc3(out)

        return out

model = NeuralNet(input_size, hidden_sizes, output_size)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

total_step = len(train_loader)


for epoch in range(num_epochs):
    if epoch%(0.01*num_epochs)==(0.01*num_epochs)-1:
        print("epoch [{}/{}]".format(epoch+1,num_epochs))
    for i, (images, labels) in enumerate(train_loader):  
        # Move tensors to the configured device
        
        # Forward pass
        outputs = model(images)
        
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
        if (i+1) % 100 == 0:
            print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                   .format(epoch+1, num_epochs, i+1, total_step, loss.item()))
            correct = 0
            total = 0
            for images, labels in test_loader:
                outputs = model(images)
                outputs = torch.round(outputs)
                total += labels.size(0)
                for i in range(outputs.size(0)):
                    correct += int(torch.all(torch.eq(outputs[i],labels[i])).item())
        
            print('Accuracy of the network on the test images: {} %'.format(100 * correct / total))


# Test the model
# In test phase, we don't need to compute gradients (for memory efficiency)
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        outputs = model(images)
        outputs = torch.round(outputs)
        print("final: ")
        print(outputs)
        print(labels)
        total += labels.size(0)
        for i in range(outputs.size(0)):
            correct += int(torch.all(torch.eq(outputs[i],labels[i])).item())
        
    print('Accuracy of the network on the 10000 test images: {} %'.format(100 * correct / total))
#
#np.random.seed(0)
#x = np.random.randint(2,  size=(amount_samples,output_size))




