# Setup

To use external Python packages within [PythonScript](https://godotengine.org/asset-library/asset/179) you have to install the packages into the virtual environment created by the extension.

1. Clone the full project from Gitlab [HERE](https://gitlab.com/angel-721/godot-code-camp/-/tree/main)
2. Install the PythonScript library into the Godot project via the [AssetLib](https://docs.godotengine.org/en/stable/community/asset_library/using_assetlib.html) tab. Godot 3.5 ONLY
3. Go into the ```addons``` folder within your Godot project and then into the ```addons/pythonscript``` folder
4. Go to the folder for your system e.g ```windows-64```
5. Install pip by running the command ```./python.exe -m ensurepip```
6. Install libraries used by the image classifier with this command ```./python.exe -m pillow numpy pandas```
7. Install Pytorch. ```./python.exe -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118```

After these steps you should be ready to demo this project or have a working framework for Machine Learning within Godot 3.5.
