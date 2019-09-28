#As the data is provided with custom screenshots and their respective DSL representation we will create a custom Torch Dataloader

#importing necessary libraries and functions
from torch.utils.data import Dataset
import torch
from BuildVocab import load_file
import os
from PIL import Image

class CreateDataset(Dataset):
    
    def __init__(self , data_dir , vocab , transform):
        
        self.data_dir = data_dir
        self.vocab = vocab
        self.transform = transform
        
        self.image_captions = []
        self.image_names = []
        
        self.filenames  = os.listdir(self.data_dir)
        self.filenames.sort()
        
        for filename in self.filenames:
            
            #if it's a .png file it's a screenshot
            if filename[-3:] == 'png':
                
                self.image_names.append(filename)
                
            #if it's a .gui file it contains DSL code 
            if filename[-3:] == 'gui':
                
                path = self.data_dir + filename
                data = load_file(path)
                self.image_captions.append(data)
        print("Created a dataset of "+ str(len(self)) + ' ' + 'items')
                
    def __len__(self):
        
        return len(self.image_names)
    
    def __getitem__(self , idx):
        
        img_path , raw_captions = self.image_names[idx] , self.image_captions[idx]
        
        image = Image.open(os.path.join(self.data_dir , img_path)).convert('RGB')
        
        #Applying the given transformations given
        image = self.transform(image)
        
        captions = []
        captions.append(self.vocab('<START>'))
        
        #Removing newlines and adding spaces between tokens
        
        tokens = ' '.join(raw_captions.split())
        
        #adding spaces after each comma
        tokens = tokens.replace(',' , ' ,')
        tokens = tokens.split(' ')
        captions.extend([self.vocab(token) for token in tokens])
        
        captions.append(self.vocab('<END>'))
        
        target = torch.Tensor(captions)
        
        return image , target
        