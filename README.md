# godot-image-classification

### This is a simple Godot project to show that image classification can be used within the [godot](https://godotengine.org/) game engine!
Find the full project [Here!](https://gitlab.com/angel-721/godot-code-camp) This link has Git-LFS support to get the full project.

### Classification Model
Built off a [Pytorch](https://pytorch.org/) implementation of a convolutional neural network found [HERE](https://github.com/angel-721/image-classifier-cnn).
Trained on the Kaggle [Cats-vs-Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset) dataset.

<a href="https://github.com/angel-721/image-classifier-cnn"><img height="30%" src="https://github.com/angel-721/godot-image-classification/assets/75283919/15de0932-1638-43a6-951c-90c224263061"></a>

### Loading the model into Godot
- Prertrain using the linked CNN and place it within Godot project
- Use the Godot 3.5 extension called [PythonScript](https://godotengine.org/asset-library/asset/179)
  - Github for the extension is [godot-python](https://github.com/touilleMan/godot-python?tab=readme-ov-file)
- Use [```Scripts/pyfiles/NetworkNode.py```](https://github.com/angel-721/godot-image-classification/blob/main/Scripts/pyfiles/NetworkNode.py) to load the pretrained model file within the engine
- WARNING - the project won't work without this extension and a little extra [set up](https://github.com/angel-721/godot-image-classification/blob/main/Docs/setup.md)

### Godot Game Environment
The game environment is a simple maze environment where the player can walk around in a first person view and right click to take a screenshot.
The screenshot is then set to the model and the model will classify if the contents within the image are a cat or dog.
The model wasn't trained to handle extra pixels due to backgrounds such as the red brick wall which may cause faulty results.
This is more of a demonstration of using image classification within a game instead of a game.

<a href=""><img height="250px" src="https://github.com/angel-721/godot-image-classification/assets/75283919/fb6a9e6d-54fe-4bd3-a1fd-e95d86cb0717"></a>
<a href=""><img height="250px" src="https://github.com/angel-721/godot-image-classification/assets/75283919/ff536ae7-b133-4960-beee-e24391d5e1f6"></a> 
