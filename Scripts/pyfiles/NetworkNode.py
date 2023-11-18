from godot import exposed, export
from godot import *
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from PIL import Image
from torch.nn.functional import softmax
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms


DATA_DIR = './Scripts/pyfiles/data/'
data_dir = DATA_DIR
BATCH_SIZE = 16
PATH = './Scripts/pyfiles/best.pth'


DATA_DIR = './Scripts/pyfiles/data'
BATCH_SIZE = 16
PATH = '../models/model1.pth'

# MAKE SURE CLASSES ARE IN THE SAME ORDER THEY ARE IN ../data/
# Put the classes that are in the ../data folder
CLASSES = ('Cat', 'Dog')

DEVICE = 'cpu'


def im_show(img, label, i, right):
	"""
	Show a Image batch with matplotlib
	"""
	img = img / 2 + 0.5
	npimg = img.cpu().numpy()
	plt.imshow(np.transpose(npimg, (1, 2, 0)))

	plt.title(CLASSES[label])
	plt.axis('off')
	if right is True:
		plt.savefig(f'./results/test-correct{i}.png')
	else:
		plt.savefig(f'./results/test-failed{i}.png')


def try_gpu(input_n, device):
	"""
	Try to use the GPU to train, test, and score on if called
	"""
	if input_n != 0:
		device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
	#print(device)


def load_data(data=DATA_DIR):
	"""
	Load images into classes from the described folder
	"""
	data_transform = transforms.Compose(
		[
			transforms.Resize((53, 53)),
			transforms.ToTensor(),
			transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
		]
	)

	dataset = datasets.ImageFolder(root=data, transform=data_transform)
	num_train = int(0.8 * len(dataset))
	num_test = len(dataset) - num_train
	train_dataset, test_dataset = random_split(dataset, [num_train, num_test])
	
	train_loader = DataLoader(
		train_dataset, batch_size=BATCH_SIZE, shuffle=True
	)
	test_loader = DataLoader(
		test_dataset, batch_size=BATCH_SIZE, shuffle=False
	)
	return train_loader, test_loader

class CNN(nn.Module):

	"""
	Class for convolutional neural network
	"""

	def __init__(self, data_dir):
		super().__init__()

		self.data_dir = data_dir
		self.train_loader, self.test_loader = load_data(data_dir)

		self.conv_layers = nn.ModuleList(
			[
				nn.Conv2d(3, 8, kernel_size=(3, 3), padding='same'),
				nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2)),
				nn.Conv2d(8, 16, kernel_size=(3, 3), padding='same'),
				nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2)),
				nn.Conv2d(16, 32, kernel_size=(3, 3), padding='same'),
				nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2)),
			]
		)

		self.fc_layers = nn.ModuleList(
			[
				nn.Linear(32 * 6 * 6, 128),
				nn.Dropout(0.5),
				nn.Linear(128, 64),
				nn.Dropout(0.5),
				nn.Linear(64, 6),
			]
		)

		# Train on GPU
		self.to(DEVICE)

		self.criterion = nn.CrossEntropyLoss().to(DEVICE)
		self.optimizer = optim.SGD(self.parameters(), lr=0.001, momentum=0.9)
		self.classes = CLASSES

	def forward(self, data_x):
		"""
		Organize and order the CNN by layer. I'm follwing a
		c-p -> c-p -> c-p -> flat -> h -> drop -> h -> drop -> h
		layout
		c = convolutional, p = pool, flat = flatten, h = hidden, drop = dropout
		"""
		new_x = data_x

		for layer in self.conv_layers:
			new_x = F.relu(layer(new_x))

		new_x = torch.flatten(new_x, 1)
		# new_x = new_x.view(new_x.size(0),-1)

		for layer in self.fc_layers:
			new_x = F.relu(layer(new_x))

		return new_x
			
	def predict_image_path_net(self, input_image_path, network_path=PATH):
		"""
		Predicts a single image
		"""
		model = torch.load(network_path)
		self.load_state_dict(model)
		self.eval()
		self.to(DEVICE)

		image = Image.open(input_image_path).convert('RGB')
		data_transform = transforms.Compose(
			[
				transforms.Resize((53, 53)),
				transforms.ToTensor(),
				transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
			]
		)
		transformed_image = data_transform(image).unsqueeze(0)

		#print('transformed_image shape', transformed_image.shape)
		#sprint('weight shape', self.fc_layers[0].weight.shape)

		with torch.no_grad():
			output = self(transformed_image)
			_, predicted = torch.max(output.data, 1)
			predicted_class = CLASSES[predicted.item()]

		#print(predicted_class)
		return predicted_class
	
	def predict_image_object_net(self, image_object, network_path=PATH):
		"""
		Predicts a single image
		"""
		model = torch.load(network_path)
		self.load_state_dict(model)
		self.eval()
		self.to(DEVICE)

		image = image_object.convert('RGB')
		data_transform = transforms.Compose(
			[
				transforms.Resize((53, 53)),
				transforms.ToTensor(),
				transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
			]
		)
		transformed_image = data_transform(image).unsqueeze(0)

		#print('transformed_image shape', transformed_image.shape)
		#sprint('weight shape', self.fc_layers[0].weight.shape)

		with torch.no_grad():
			output = self(transformed_image)
			_, predicted = torch.max(output.data, 1)
			predicted_class = CLASSES[predicted.item()]

		print(predicted_class)
		return
	
	def predict_image_array_net(self, image_array, network_path=Path,):
		"""
		Predicts a single image array
		"""
		model = torch.load(network_path)
		self.load_state_dict(model)
		self.eval()
		self.to(DEVICE)

		#image = Image.open(input_image_path).convert('RGB')
		image = image_array
		data_transform = transforms.Compose(
			[
				transforms.Resize((53, 53)),
				transforms.ToTensor(),
				transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
			]
		)
		transformed_image = data_transform(image).unsqueeze(0)

		#print('transformed_image shape', transformed_image.shape)
		#sprint('weight shape', self.fc_layers[0].weight.shape)

		with torch.no_grad():
			output = self(transformed_image)
			_, predicted = torch.max(output.data, 1)
			predicted_class = CLASSES[predicted.item()]

		print(predicted_class)
		return
	
	def hi_net(self):
		print("hi from network class")
	

@exposed
class NetworkNode(Node):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
	prediction = export(str, default="")

	def _ready(self):
		self.model = CNN("./Scripts/pyfiles/data/")

	
	def predict_image_array(self, image):
		self.model.predict_image_array_net(image, "./Scripts/pyfiles/best.pth")
	
	def predict_image_object(self, image):
		self.model.predict_image_object_net(image, ".Scripts/pyfiles/best.pth")
	
	def predict_image_read(self):
		self.prediction = str(self.model.predict_image_path_net("./SavedPics/read.png", "./Scripts/pyfiles/best.pth"))
