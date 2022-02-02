# Google Image Downloader
This program uses Selenium to navigate through google images and downloads them on its own.
The program requires selenium==4.1.0

# Usage
1. Clone the repository
1. Navigate to the repository in command prompt and type `python downloader.py`
2. Enter query for image search
3. Provide the desired resolution of the images (by default medium)
   Press -> "l" for large, "i" for small
   or press enter to proceed with default value
3. Enter the number of images to download

# NOTE -
1. Images downloaded might be less than the provided number. So, it's recommeded to download more than required, to compensate
2. Images will be downloaded in .JPG format as -> 0.jpg, 1.jpg, 2.jpg....so on
3. A download directory will be created as `<query>_<number of images>` if it doesn't exist
4. If downloaded resolution is lower than actual one, of an image, try increasing `WAIT_TIME_PER_IMAGE` and `INITIAL_WAIT_TIME`
6. By default webdriver window remains hidden. To unhide it, set `HEADLESS` to FALSE
7. It only works for `chrome driver` 

# VIDEO LINK 
https://drive.google.com/file/d/1sX3pBcOcgo-Ap8feDPDYVxxhz6d9Zc9e/view?usp=sharing
