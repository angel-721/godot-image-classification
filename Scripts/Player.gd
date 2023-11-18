extends KinematicBody


export(float) var speed
export(float) var mouseSpeed
export(float) var grav

onready var cam = $Camera
onready var viewport = $Viewport
onready var audioAnim = $AudioHoldder/AnimationPlayer

var actualVelocity := Vector3.ZERO

var texture := ViewportTexture.new()
var modelLastPrediction = ''
var model = null
var screenshot = null

var numScreenshots : int = 0
func _ready():
	audioAnim.play("ToCat")
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
	texture = viewport.get_texture()
	model = get_node("NetworkNode")
	print(model)
	

func _physics_process(_delta):
	var dir = Input.get_vector("Walk_Left","Walk_Right","Walk_Forward","Walk_Back")
	
	var vel = Vector3(dir.x * speed, 0,dir.y * speed)
	
	
	vel = vel.rotated(Vector3(0,1,0),rotation.y)
	
	vel.y = actualVelocity.y - grav
	
	actualVelocity = move_and_slide(vel,Vector3.UP)
	

func _unhandled_input(event):
	if event is InputEventMouseMotion:
		rotate_y(-event.relative.x * mouseSpeed)
		cam.rotate_x(-event.relative.y * mouseSpeed)
		
		cam.rotation.x = clamp(cam.rotation.x,deg2rad(-70),deg2rad(70))
	if event.is_action_pressed("Quit"):
		get_tree().quit()
	if event.is_action_pressed("TakePic"):
		_take_picture()
		
func _take_picture():
	ScreenshotHandler._setScreenshot(texture.get_data())
	ScreenshotHandler.saveScreenshotOne("res://SavedPics/")
	model.predict_image_read()
	print(model.prediction)
	
	if(model.prediction != modelLastPrediction):
		if(model.prediction == 'Cat'):
			audioAnim.play("ToCat")
		else:
			audioAnim.play("ToDog")
	
