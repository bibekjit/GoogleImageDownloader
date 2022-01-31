# Google Image Downloader
This program uses Selenium to navigate through google images and downloads them on its own.
The program requires selenium==4.1.0

# Usage
1. Navigate to the repository in command prompt and type `python downloader.py`
2. Enter query for image search
3. Provide the desired resolution of the images (by default medium)
   Press -> "l" for large, "i" for small
   or press enter to proceed with default value
3. Number of images to download

# NOTE -
1. Images downloaded might be less than the provided number. This is because some images don't have a source link
   So, it's recommeded to download more than required, to compensate
2. Images will be downloaded in .JPG format as -> 0.jpg, 1.jpg, 2.jpg....so on
3. A download directory will be created as `<query>_<number of images>` if it doesn't exist

