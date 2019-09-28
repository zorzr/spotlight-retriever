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


if __name__ == "__main__":
	if not os.path.isdir(folder):
		print("Cannot find Spotlight folder")
		exit(1)
	
	if len(os.listdir(folder)) == 0:
		print("Spotlight folder is empty. Please make sure it is enabled")
		exit(2)

	import argparse
	parser = argparse.ArgumentParser(description="Fetch the current Spotlight wallpapers on Windows 10")
	parser.add_argument('-f', metavar='name', help='specifies the name of the output directory')
	parser.add_argument('-s', nargs=2, type=int, metavar=('width', 'height'), help='defines the size of the images to be saved')
	parser.add_argument('--fullhd', action='store_true', help='saves 1920x1080 and 1080x1920 images only')
	parser.add_argument('--widescreen', action='store_true', help='saves 1920x1080 images only')
	args = parser.parse_args()
	
	if args.f is not None:
		name = args.f

	if not os.path.exists(name):
		os.mkdir(name)

	image_list = retrieve_images()

	if args.fullhd:
		filter1 = filter_images(image_list, 1920, 1080)
		filter2 = filter_images(image_list, 1080, 1920)
		remove_unfiltered(image_list, filter1 + filter2)
	elif args.widescreen:
		image_filter = filter_images(image_list, 1920, 1080)
		remove_unfiltered(image_list, image_filter)
	elif args.s is not None:
		image_filter = filter_images(image_list, args.s[0], args.s[1])
		remove_unfiltered(image_list, image_filter)
