import os
import shutil
from datetime import datetime
from get_image_size import get_image_size, UnknownImageFormat

name = datetime.now().strftime("%Y-%m-%d %H%M%S")
folder = os.path.expanduser('~\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')


def retrieve_images():
	for file in os.listdir(folder):
		full_path = os.path.join(folder, file)
		shutil.copy(full_path, name)

	image_list = []
	for file in os.listdir(name):
		full_path = os.path.join(name, file)
		new_path = full_path + ".jpg"

		image_list.append(new_path)

		if os.path.exists(new_path):
			os.remove(full_path)
			continue

		os.rename(full_path, new_path)
	
	return image_list


def filter_images(image_list, image_width, image_height):
	filtered_list = []
	for image_path in image_list:
		try:
			width, height = get_image_size(image_path)
		except UnknownImageFormat:
			width, height = -1, -1

		if width == image_width and height == image_height:
			filtered_list.append(image_path)
	
	return filtered_list


def remove_unfiltered(image_list, filtered_list):
	for image_path in image_list:
		if image_path not in filtered_list:
			os.remove(image_path)
