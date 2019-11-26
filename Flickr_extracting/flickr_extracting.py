from flickrapi import FlickrAPI
import urllib
import os
import random
import time
import csv

# replace with your key
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# replace with your secret
API_SECRET = 'xxxxxxxxxx'
# replace with your folder to store the images
IMG_FOLDER = os.getcwd()
print(IMG_FOLDER)


def download_flickr_photos(keywords, size='original', max_nb_img=-1, lati=0, lont=0):
    """
    Downloads images based on keyword search on the Flickr website

    Parameters
    ----------
    keywords : string, list of strings
        Keyword to search for or a list of keywords should be given.
    size : one of the following strings 'thumbnail', 'square', 'medium', default: 'original'.
        Size of the image to download. In this function we only provide
        four options. More options are explained at
        http://librdf.org/flickcurl/api/flickcurl-searching-search-extras.html
    max_nb_img : int, default: -1
        Maximum number of images per keyword to download. If given a value of -1, all images
        will be downloaded

    Returns
    ------
    Images found based on the keyword are saved in a separate subfolder.

    Notes
    -----
    This function uses the Python package flickrapi and its walk method.
    FlickrAPI.walk has same parameters as FlickrAPI.search
    http://www.flickr.com/services/api/flickr.photos.search.html

    To use the Flickr API a set of API keys needs to be created on
    https://www.flickr.com/services/api/misc.api_keys.html
    """
    if not (isinstance(keywords, str) or isinstance(keywords, list)):
        raise AttributeError('keywords must be a string or a list of strings')

    if not (size in ['thumbnail', 'square', 'medium', 'original']):
        raise AttributeError('size must be "thumbnail", "square", "medium" or "original"')

    if not (max_nb_img == -1 or (max_nb_img > 0 and isinstance(max_nb_img, int))):
        raise AttributeError('max_nb_img must be an integer greater than zero or equal to -1')

    flickr = FlickrAPI(API_KEY, API_SECRET)

    if isinstance(keywords, str):
        keywords_list = []
        keywords_list.append(keywords)
    else:
        keywords_list = keywords

    if size == 'thumbnail':
        size_url = 'url_t'
    elif size == 'square':
        size_url = 'url_q'
    elif size == 'medium':
        size_url = 'url_c'
    elif size == 'original':
        size_url = 'url_o'

    geoloc = 'geo'
    for keyword in keywords_list:
        count = 0

        # print('Downloading images for', keyword)
        results_folder = IMG_FOLDER + '/' + keyword.replace(" ", "_") + "/"
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        photos = flickr.walk(
            tags=keyword,
            lat=lati,
            lon=lont,
            radius=32,
            extras=size_url,
            license='1,2,4,5',
            per_page=50)
        photos_geo = flickr.walk(
            tags=keyword,
            lat=lati,
            lon=lont,
            radius=32,
            extras=geoloc,
            license='1,2,4,5',
            per_page=50)
        ## This part is used to get the coordinates information and store them to csv
        os.makedirs('coordinates', exist_ok=True)
        coordinates = [['latitude', 'longitude']]
        for photo in photos_geo:
            t = random.randint(1, 3)
            time.sleep(t)
            count += 1
            if max_nb_img != -1:
                if count > max_nb_img:
                    print('Reached maximum number of images Geoinfo to get')
                    break
            try:
                print(photo.attrib['latitude'] + " " + photo.attrib['longitude'])
                store = []
                store.append(photo.attrib['latitude'])
                store.append(photo.attrib['longitude'])
                coordinates.append(store)
            except Exception as e:
                print(e, 'Get GeoInfo failure')
        corFile = open('coordinates/' + keywords + '.csv', 'w', newline='')
        corWriter = csv.writer(corFile)
        for row in coordinates:
            corWriter.writerow(row)
        corFile.close()
        # This part is used to download the images
        urls = []
        count = 0
        for photo in photos:
            t = random.randint(1, 3)
            time.sleep(t)
            count += 1
            if max_nb_img != -1:
                if count > max_nb_img:
                    print('Reached maximum number of images to download')
                    break
            try:
        
                url = photo.get(size_url)
                urls.append(url)
                urllib.request.urlretrieve(url, results_folder + str(count) + ".jpg")
                print('Downloading image #' + str(count) + ' from url ' + url)
            except Exception as e:
                print(e, 'Download failure')

    print("Total images downloaded:", str(count - 1))


info = input('please enter the keyword you want to search:')
picNumber = input('please enter the number of images you want to search:')
download_flickr_photos(info, 'original', int(picNumber), 40.6, -73.9)

