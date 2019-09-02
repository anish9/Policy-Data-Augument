from autoaugment import ImageNetPolicy,SVHNPolicy,CIFAR10Policy
from PIL import Image, ImageEnhance
from tqdm import tqdm
import os
import re
import argparse
import numpy as np
import cv2


roots = argparse.ArgumentParser()
roots.add_argument("-f", "--files_directory", required=True, help="root image file directory containing classes and under classes containing images")
roots.add_argument("-r", "--replicas", required=True, type=int, help="number of times an image has to undergo policy augumentations")
roots.add_argument("-p", "--policy", required=True, help="available policies are svhn, imagenet, cifar, all")
args = vars(roots.parse_args())


class policy_maker(object):
    def __init__(self,image_carry,counter_val,save_dir="created_data/"):
        self.im_file = image_carry
        self.count = counter_val
        self.data_save_dir = save_dir


    def SVHN_policy(self):
        """generates auguments based on SVHN policy"""

        imag_tag = self.im_file
        policy = SVHNPolicy()
        image = Image.open(imag_tag)
        tag = re.findall('([-\w]+\.(?:jpg|gif|png|JPG|JPEG|jpeg))',imag_tag)
        for t in range(self.count):
            polic = policy(image)
            polic.save(self.data_save_dir+str(t)+tag[0],format="JPEG")
            
            
    def IMAGENET_policy(self):
        """generates IMAGENET Policy """
        
        imag_tag = self.im_file
        policy = ImageNetPolicy()
        image = Image.open(imag_tag)
        tag = re.findall('([-\w]+\.(?:jpg|gif|png|JPG|JPEG|jpeg))',imag_tag)
        for t in range(self.count):
            polic = policy(image)
            polic.save(self.data_save_dir+str(t)+tag[0],format="JPEG")
            

    def CIFAR10_policy(self):
        """generates CIFAR10 Policy"""
        imag_tag = self.im_file
        policy = CIFAR10Policy()
        image = Image.open(imag_tag)
        tag = re.findall('([-\w]+\.(?:jpg|gif|png|JPG|JPEG|jpeg))',imag_tag)
        for t in range(self.count):
            polic = policy(image)
            polic.save(self.data_save_dir+str(t)+tag[0],format="JPEG")
            
            
            
def main_caller(folder_id,replicas,policy="all"):
    DATA_DIR = folder_id
    for folders in os.listdir(DATA_DIR):
        for images_ in tqdm(os.listdir(os.path.join(DATA_DIR,folders))):
            init_policy = policy_maker(os.path.join(DATA_DIR,folders,images_),replicas,save_dir=os.path.join(DATA_DIR,folders)+"/")
            if policy == "all":
                try:
                    init_policy.SVHN_policy()
                    init_policy.IMAGENET_policy()
                    init_policy.CIFAR10_policy()
                except:
                    print(str(os.path.join(DATA_DIR,folders,images_)))
                    continue
            if policy == "svhn":
                try:
                    init_policy.SVHN_policy()
                except:
                    continue
            if policy == "imagenet":
                try:
                    init_policy.IMAGENET_policy()
                except:
                    continue
            if policy == "cifar":
                try:
                    init_policy.CIFAR10_policy()
                except:
                    continue
                    
                    
                    
main_caller(args["files_directory"],args["replicas"],args["policy"])