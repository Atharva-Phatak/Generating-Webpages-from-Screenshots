#Function to split the raw data folder into training , val and test data
#importing libraries
import os
from shutil import copyfile
from tqdm import tqdm
import random


def SplitDataset(root_path , output_path):
    
    filenames = os.listdir(root_path)
    
    name_list = []
    for name in filenames:
        if name.endswith('.gui'):
            name_list.append((name[:-3] + 'gui' , name[:-3] + 'png'))
            
    #Setting random seed so as to ensure reproducability
    random.seed(42)
    name_list.sort()
    random.shuffle(name_list)
    
    split_1 = int(0.8*len(name_list))
    split_2 = int(0.9*len(name_list))
    
    f_name = {  'train' : name_list[:split_1],
                'val' : name_list[split_1 : split_2],
                'test' : name_list[split_2:]
            }
    
    #Let's check if output path exists or not , if not we'll create that folder
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    else:
        print("Output path Exists : {}".format(output_path))
    
    #Let's start splitting the dataset into folders and moving the data to the corresponding folders
    split_list = ['train' , 'val' , 'test']
    for split in split_list:
        
        output_dir_split = os.path.join(output_path ,'data_{}'.format(split))
        
        if not os.path.exists(output_dir_split):
            os.mkdir(output_dir_split)
            
        else:
            print("Path already exists : {}".format(output_dir_split))
            
        for (gui_file , png_file) in tqdm(f_name[split]):
            
            #For GUI(DSL) files
            gui_source_path = os.path.join(root_path , gui_file)
            gui_output_path = os.path.join(output_dir_split , gui_file)
            
            #For PNG images
            
            png_source_path = os.path.join(root_path , png_file)
            png_output_path = os.path.join(output_dir_split , png_file)
            
            copyfile(gui_source_path , gui_output_path)
            copyfile(png_source_path , png_output_path)
            
            
