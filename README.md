GHCLNet 
===================


This README will guide you through running the code and getting classification results on test images. The paper which discuss its detailed implementation is 
"GHCLNet: A Generalized Hierarchically tuned Contact Lens detection Network" accepted at IEEE 4th International Conference on Identity, Security, and Behavior Analysis (ISBA) 2018

----------


Steps
-------------

> - Put all the test images in the folder 'images'
> - Run the python code GHCLNet.py
> - A text file 'result.txt' will be created with the classification results of the images

Required Dependencies
-------------

> - Python
> - Numpy(1.13.1)
> - Keras(2.0.7)
> - h5py(2.7.0)




----------------------------------------------------------------------------------------
We have tested our trained model on ND1-test dataset comprising of 400 images of each class i.e no-lens, soft-lens and textures-lens. 
The number of the images that are correctly classified are as follows:
1) no-lens = 382
2) soft-lens = 348
3) cosmetic-lens = 398
