# Spotlight Retriever

Most of the Windows 10 users can notice that the Spotlight feature manages the lock screen by displaying a nice wallpaper and your notifications. The images change almost daily and a lot of time may pass before finding the same one.

*Spotlight Retriever* allows to save these wallpapers in order to keep and adopt them to make your desktop background shine!



## Usage

To use the application you need to run the `retriever.py` file from the command line:

```
cd retriever
python ./retriever.py
```

The images will be stored as JPEG files in a folder named with the current date and time. Alternatively, you can customize the output folder and the image size with the following program arguments:

```
  -f name          		specifies the name of the output directory
  -s width height  		defines the size of the images to be saved
  --fullhd         		saves 1920x1080 and 1080x1920 images only
  --widescreen     		saves 1920x1080 images only
```



## Requirements

- [Python 3](https://www.python.org)
- `get_image_size.py` from [scardine's image_size](https://github.com/scardine/image_size)

It must be stored in the *retriever* folder.