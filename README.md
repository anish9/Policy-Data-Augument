### Data Augumentation as claimed in the paper [Policies](https://arxiv.org/abs/1805.09501)
The project has been build on top of [AutoAugment](https://github.com/DeepVoltaire/AutoAugment)

### USAGE
#### we need to have folder structure in similiar way

    ├── image_classifier_data
    ├── Apple                    
    │   ├── apple1.jpg          
    │   ├── apple2.jpg         
    │   └── apple3.jpg              
    ├── Orange                    
    │   ├── orange1.jpg          
    │   ├── orange2.jpg         
    │   └── ornage3.jpg          # Image directory structure (something similiar to classifier friendly structure) 
    └── ...
    
 
#### check the helps before execution
```
python3 build_dataset.py -h
usage: build_dataset.py [-h] -f FILES_DIRECTORY -r REPLICAS -p POLICY

optional arguments:
  -h, --help            show this help message and exit
  -f FILES_DIRECTORY, --files_directory FILES_DIRECTORY
                        root image file directory containing classes and under
                        classes containing images
  -r REPLICAS, --replicas REPLICAS
                        number of times an image has to undergo policy
                        augumentations
  -p POLICY, --policy POLICY
                        available policies are svhn, imagenet, cifar, all


```
#### running the code when all set (NOTE : augumented image files are saved on the same folder itself )
```
python3 build_dataset.py -f train_data/ -r 5 -p imagenet


```
