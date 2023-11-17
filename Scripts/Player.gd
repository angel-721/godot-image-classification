extends KinematicBody


export(float) var speed
export(float) var mouseSpeed
export(float) var grav

onready var cam = $Camera
onready var viewport = $Viewport

var actualVelocity := Vector3.ZERO

var texture := ViewportTexture.new()

var numScreenshots : int = 0
func _ready():
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
	texture = viewport.get_texture()

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
	var screenshotPath = "res://SavedPics/Screenshot"
	var testDir = Directory.new()
	numScreenshots += 1
	if(not testDir.dir_exists(screenshotPath)):
		testDir.make_dir(screenshotPath)
	texture.get_data().save_png(screenshotPath + String(numScreenshots) + ".png")
