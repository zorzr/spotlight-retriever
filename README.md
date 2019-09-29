# Spotlight Retriever

Most of the Windows 10 users can notice that the Spotlight feature manages the lock screen by displaying a nice wallpaper and your notifications. The images change almost daily and a lot of time may pass before finding the same one.

*Spotlight Retriever* allows to save these wallpapers in order to keep and adopt them to make your desktop background shine!



## Usage

To run the application just double-click on the `Spotlight-Retriever.exe` file in the `retriever` folder. The graphical interface will be shown in a new window, where you can specify your preferences. When everything is settled, just press on the *Run* button.

In alternative, if you have some expertise, you can execute the same functionalities from command line with the following possible arguments:

```
  -f name          		specifies the name of the output directory
  -s width height  		defines the size of the images to be saved
  --fullhd         		saves 1920x1080 and 1080x1920 images only
  --widescreen     		saves 1920x1080 images only
  --run     			runs through command line (with default options)
```

The `--run` flag is necessary only if you want to launch the application with default settings: by omitting it, you will launch the graphical interface instead. However, if you insert any other type of argument the program will automatically run on the command line.

The images will be stored as JPEG files in a folder named with the current date and time (if it isn't specified differently).



To use the application from the source code you need to run the `main.py` file from the command line:

```
cd retriever
python ./main.py
```



## Requirements

There are no specific requirements for the released executable. Just make sure Spotlight is enabled in the lock screen Preferences.

For building the code, these libraries are required:

- [Python 3](https://www.python.org)
- [PyQt5](https://pypi.org/project/PyQt5/)
- `get_image_size.py` from [scardine's image_size](https://github.com/scardine/image_size)

It must be stored in the *retriever* folder.