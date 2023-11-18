extends KinematicBody

onready var viewpt = $Viewport
var texture : ViewportTexture

func _ready():
	texture = viewpt.get_texture()

func _take_Picture():
	ScreenshotHandler._setScreenshot(texture.get_data())
	ScreenshotHandler.saveScreenshotOne("res://SavedPics/")
