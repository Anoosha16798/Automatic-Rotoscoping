## Automatic Rotoscoping in Python ##

**Rotoscoping for VFX is used to create a matte or mask for an element, so it can be extracted out to place on a different background, masked out so colors can be changed, or any other set of reasons. It is more widely used than many realize.**

######Here are few steps you need to follow:######

* **Step 1 - Installing the software**
         Download Anaconda(which will help you to create virtual environment).
         Download Wing/PyCharm/Sublime or any Python IDE
         
* **Step 2 - Creat a python environment and installing libraries**
         If you are using anaconda create vitual environment via anaconda prompt
         Install torchvision cmd--- pip install torchvision
         Install torchvision cmd--- pip install pytorch
         # Above two liberaries are machine learning liberaries used for applications such as computer vision and natural language processing.
         Install pillow cmd--- pip install pillow
         # Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.
         now check for tkinter and numpy liberaries in the editor
         import tkinter as tk
         import numpy 
         # if tkinter is not present install it via pip install tkinter
        
* **Step 3 - Now clone this repository to your local file.**
* **Step 4 - Findmatte.py is the trained model and Rotomaker_v001.py is the main file. Run Rotomaker_v001.py file in the terminal via python (pass the path of Rotomaker_v001.py file)**
* **Step 5 - You will get GUI asking to choose a folder(which consists of images), choose any folder, set the resolution (256 is prefered)**
* **Step 6 - you can find matte files in your folder.**

## Thank you. :relaxed: ##
        
         
         
