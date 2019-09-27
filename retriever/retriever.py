import os
import shutil
from datetime import datetime
try:
	from get_image_size import get_image_size, UnknownImageFormat
	image_size = True
except ImportError:
	image_size = False

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
	for image_path in image_list:
		try:
			width, height = get_image_size(image_path)
		except UnknownImageFormat:
			width, height = -1, -1
		
		if not (width == image_width and height == image_height):
			os.remove(image_path)


if __name__ == "__main__":
	if not os.path.isdir(folder):
		print("Cannot find Spotlight folder")
		exit(1)
	if not os.path.exists(name):
		os.mkdir(name)

	image_list = retrieve_images()
	if image_size:
		filter_images(image_list, 1920, 1080)
	else:
		print("Cannot find get_image_size.py")
		os.system("pause")
