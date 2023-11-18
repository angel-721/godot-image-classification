extends Node


var currScreenshot : Image
var imgName = "Screenshot"

func _ready():
	pass

func _setScreenshot(newScreenShot : Image):
	currScreenshot = newScreenShot

func getScreenshot():
	return currScreenshot
#get image as a list of vector3s

func getScreenImgRGBArray() -> PoolVector3Array:
	var returnArr := PoolVector3Array([])
	for i in currScreenshot.get_size().x:
		for j in currScreenshot.get_size().y:
			var col := currScreenshot.get_pixel(i,j)
			var vec := Vector3(col.r,col.g,col.b)
			returnArr.append(vec)
	return returnArr

#Save image to file
func saveScreenshot(path : String) -> int:
	var dir = Directory.new()
	var imgCount : int
	if(not dir.dir_exists(path)):
		var err = dir.make_dir(path)
		if(err != 0):
			return err
		imgCount = 0
	elif(dir.open(path) == OK):
		dir.list_dir_begin(true)
		var currFile = dir.get_next()
		while(currFile):
			print(currFile)
			if(currFile.ends_with(".png")):
				imgCount += 1
			currFile = dir.get_next()
		print(currFile)
	var val = currScreenshot.save_png(path + imgName + str(imgCount + 1) + ".png")
	return val

func saveScreenshotOne(path : String) -> int:
	var dir = Directory.new()
	var imgCount : int = 0
	if(not dir.dir_exists(path)):
		var err = dir.make_dir(path)
		if(err != 0):
			return err
		imgCount = 0
	elif(dir.open(path) == OK):
		dir.list_dir_begin(true)
		var currFile = dir.get_next()
		while(currFile):
			if(currFile.ends_with(".png")):
				imgCount += 1
			currFile = dir.get_next()
	var val = currScreenshot.save_png(path + "read" + ".png")
	return val
