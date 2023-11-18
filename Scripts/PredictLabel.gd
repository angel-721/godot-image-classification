xtends Node


var model = null
var label : Label
# Declare member variables here. Examples:
# var a = 2
# var b = "text"
func cat_or_dog(prediction):
	#Some kind of function here to tell the display label function whether a cat or dog should be printed
	#var prediction = "cat" #get the neural network output here????
	if prediction == "cat":
		return "CAT DETECTED"
	if prediction == "dog":
		return "DOG DETECTED"

func display_cat_text(prediction):
	#Label is how you get text displayed on the screen

	var text_to_display = null
	if prediction == "Cat":
		text_to_display = "CAT DETECTED"
	if prediction == "Dog":
		text_to_display = "DOG DETECTED"
	if prediction == null:
		text_to_display = "GOT NOTHING"
	#You have to set the .text of a label to a string, thats what is displayed
	label.text = str(text_to_display)
	#change the color of the text with modulate
	label.modulate = Color(255, 255, 0)
	#rect_size is supposedly supposed to change the size of the text, I could'nt get that to work
	#Another way is by using font files but i don't know how to do any of that
	label.rect_size = Vector2(1000, 1000)
	
	
	label.rect_scale.x = 2.0
	label.rect_scale.y = 2.0
	#get the text in the middle of the screen
	label.rect_position.x = (OS.get_screen_size().x / 2)# - (int(len(text_to_display) * 2))
	label.rect_position.y = (OS.get_screen_size().y / 2)
	
	#Add the label to the BaseScene

	
	#boilerplate for changing the text based on conditionals
	var cat = true
	if cat == false:
		label.text = "CAAAAT"
	pass
		
# Called when the node enters the scene tree for the first time.
func _ready():
	model = get_node("../Player/NetworkNode")
	label = Label.new()
	add_child(label)
	var prediction = model.prediction
	
	#display_cat_text(prediction)




# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
