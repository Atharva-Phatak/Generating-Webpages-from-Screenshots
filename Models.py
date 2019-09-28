#Let's create encoder and decoder models for our task
#importing Torch requirements

import torch
import torch.nn as nn
import torchvision.models as models 

#We are going to use pre trained ResNet as our encoder but we will modift the final layer according to our requirements

class EncoderNet(nn.Module):
    
    def __init__(self , embedding_size):
        
        super(EncoderNet , self).__init__()
        
        resnet = models.resnet152(pretrained = True)
        
        #Removing the fully connected layers
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        
        #Let's create final layers according to our requirement
        self.linear = nn.Linear(in_features = resnet.fc.in_features , out_features = embedding_size)
        self.BatchNorm = nn.BatchNorm1d(num_features = embedding_size , momentum = 0.01)
        
    def forward(self , images):
        
        features = self.resnet(images)
        
        #Resisizng features according to size of our FC layer
        
        features = features.view(features.size(0) , -1)
        
        features  = self.BatchNorm(self.linear(features))
        
        return features
    
    
#We are going to create out decoder net using LSTM's (can use GRU for reduced computation)
        
class DecoderNet(nn.Module):
    
    def __init__(self , embed_size , hidden_size , vocab_size , num_layers):
        super(DecoderNet , self).__init__()
        
        self.embed_size = embed_size
        self.embed = nn.Embedding(num_embeddings = vocab_size , embedding_dim = embed_size)
        self.lstm = nn.LSTM(input_size = embed_size , hidden_size = hidden_size , num_layers = num_layers , batch_first = True)
        
        self.linear = nn.Linear(in_features = hidden_size , out_features = vocab_size)

    def forward(self ,features , captions , length):

        #Input : Captions size = [batch_size , len(longest_caption)]
        #output [batch_size , len(longest caption) , embed_size]
        embeddings = self.embed(captions)
        
        features  = features.unsqueeze(1)
        
        #concatenating features and embeddings
        
        embeddings = torch.cat((features , embeddings) , 1)
        packed = nn.utils.rnn.pack_padded_sequence(input = embeddings , lengths = length , batch_first = True)
        hidden , _ = self.lstm(packed)
        output = self.linear(hidden[0])
        
        return output
    
    #Method to test our model
    def sample(self , features , states = None):
        
        sampled_ids = []
        inputs = features.unsqueeze(1)
        
        for i in range(100):
            
            hidden , states = self.lstm(inputs ,states)
            
            output = self.linear(hidden.squeeze(1))
            predicted = output.max(dim = 1, keepdim = True)[1]
            sampled_ids.append(predicted)
            inputs = self.embed(predicted)
            inputs = inputs.view(-1, 1, self.embed_size)

        sampled_ids = torch.cat(sampled_ids, 1)

        return sampled_ids.squeeze()
        
        
                
        
        
