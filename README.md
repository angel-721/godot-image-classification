# godot-image-classification

### This is a simple Godot project to show that image classification can be used within the [godot](https://godotengine.org/) game engine!
Find the full project [Here!](https://gitlab.com/angel-721/godot-code-camp) This link has Git-LFS support to get the full project.

### Classification Model
Built off a [Pytorch](https://pytorch.org/) implementation of a convolutional neural network found [HERE](https://github.com/angel-721/image-classifier-cnn).
Trainned on the Kaggle [Cats-vs-Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset) dataset.

<a href="https://github.com/angel-721/image-classifier-cnn"><img height="30%" src="https://github.com/angel-721/godot-image-classifcation/assets/75283919/d521c9e8-8bbe-4109-a8e6-0352bf35b20b"></a>

### Loading the model into Godot
- Prertrain using the linked CNN and place it within Godot project
- Use the Godot 3.5 extension called [PythonScript](https://godotengine.org/asset-library/asset/179)
  - Github for the extension is [godot-python](https://github.com/touilleMan/godot-python?tab=readme-ov-file)
- Use [```Scripts/pyfiles/NetworkNode.py```](https://github.com/angel-721/godot-image-classifcation/blob/main/Scripts/pyfiles/NetworkNode.py) to load the pretrained model file within the engine
- WARNING - the project won't work without this extension and a little extra set up

### Godot Game Environment
The game enviroment is a simple maze enviroment where the player can walk around in a first person view and right click to take a screenhot.
The screenshot is then set to the model and the model will classify if the contents within in the image are a cat or dog. 
The model wasn't trainned to handle extra pixels due to background such as the red brick wall which may cause faulty results.
This is more of demostration of using image classifcation within in a game instead of a game. 

<a href=""><img height="300px" src="https://github.com/angel-721/godot-image-classifcation/assets/75283919/a7525839-2d42-42d7-976c-9e8605d84756"></a>
<a href=""><img height="300px" src="https://github.com/angel-721/godot-image-classifcation/assets/75283919/84287cf3-e9de-4698-b5a0-6b6a0e28a757"></a> 
