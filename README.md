# Google Image Downloader
This program uses Selenium to navigate through google images and downloads them on its own.
The program requires selenium==4.1.0

# Usage
1. Enter query for image search
2. Provide the desired resolution of the images (by default medium)
   Press -> "l" for large, "i" for small
   or press enter to proceed with default value
3. Number of images to download
4. Images will be downloaded in .JPG format as -> 0.jpg, 1.jpg, 2.jpg....so on
5. A download directory will be created as `<query>_<number of images>` if it doesn't exist

# NOTE -
Images downloaded might be less than the provided number. This is because some images don't have a source link


