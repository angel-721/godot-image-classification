extends Control


var level = preload("res://BaseScene.tscn")



func _on_Play_pressed():
	get_tree().change_scene_to(level)




func _on_Quit_pressed():
	get_tree().quit()
