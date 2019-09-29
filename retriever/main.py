import os
import sys
import argparse
import retriever
import gui


def check_spotlight():
	if not os.path.isdir(retriever.folder):
		print("Cannot find Spotlight folder")
		exit(1)
	
	if len(os.listdir(retriever.folder)) == 0:
		print("Spotlight folder is empty. Please make sure it is enabled")
		exit(2)


def start():
	check_spotlight()

	if args.f is not None:
		retriever.name = args.f
	if not os.path.exists(retriever.name):
		os.mkdir(retriever.name)

	image_list = retriever.retrieve_images()

	if args.fullhd:
		filter1 = retriever.filter_images(image_list, 1920, 1080)
		filter2 = retriever.filter_images(image_list, 1080, 1920)
		retriever.remove_unfiltered(image_list, filter1 + filter2)
	elif args.widescreen:
		image_filter = retriever.filter_images(image_list, 1920, 1080)
		retriever.remove_unfiltered(image_list, image_filter)
	elif args.s is not None:
		image_filter = retriever.filter_images(image_list, args.s[0], args.s[1])
		retriever.remove_unfiltered(image_list, image_filter)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Fetch the current Spotlight wallpapers on Windows 10")
	parser.add_argument('-f', metavar='name', help='specifies the name of the output directory')
	parser.add_argument('-s', nargs=2, type=int, metavar=('width', 'height'), help='defines the size of the images to be saved')
	parser.add_argument('--fullhd', action='store_true', help='saves 1920x1080 and 1080x1920 images only')
	parser.add_argument('--widescreen', action='store_true', help='saves 1920x1080 images only')
	parser.add_argument('--run', action='store_true', help='runs through command line')
	args = parser.parse_args()

	if args.run or len(sys.argv) > 1:
		start()
	else:
		gui.start()
