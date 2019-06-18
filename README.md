# randomize_image_names

To understand the need for **random-rename**, imagine you're currently in this situation:

You and some other members of a crowdsourcing team are asked to download a bunch of hotel and non-hotel images from the internet. These images are needed by a hotel booking platform to train a Machine Learning (ML) model with, and this ML will automatically detect whether an image contains an hotel or not. 

Since you all are autonomously downloading images, the chances are high that two or more people will download images with the same name, which will cause conflicts when pushing to Git. You may choose to manually fix these conflicts or rather take an easier route which involves making each team member rename their files in such a way that no two files bear the same name.

The latter is not an 'easy' route if done manually. Hence, the need for random-rename. 

Random-rename is a Python package that offers a non-deterministic rename of files using the uuid module in Python's standard library.


**Requirements** 
- Python 3.*
