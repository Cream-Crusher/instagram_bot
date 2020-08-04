import requests
import os
import glob
import sys
import time
from io import open
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot  


def get_hubble_image(url, target_path):
    response = requests.get(url, verify=False)
    response.raise_for_status()  
    with open(target_path, 'wb') as the_path_to_the_file: 
        the_path_to_the_file.write(response.content) 
        image = Image.open(target_path)
        image.thumbnail((1080, 1080)) 
        image.save(target_path)          
        path_to_pictures.append(target_path)

if __name__ == '__main__':
    load_dotenv()   
    folder_name = 'images'
    path_to_pictures = []
    instagram_username = os.getenv('INSTAGRAM_USERNAME')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD') 
    for  reference_number in range(1, 4):
        url ='http://hubblesite.org/api/v3/image/{}'.format(reference_number)
        response = requests.get(url, verify=False).json()
        response = response['image_files'][-1]['file_url']
        url = response
        url='https:'+url
        target_path = os.path.join(folder_name , 'api_hubblev{}.jpg'.format(reference_number)) 
        get_hubble_image(url, target_path)  
    for  reference_number in range(1, 4):
        url ='https://api.spacexdata.com/v3/launches'
        response = requests.get(url, verify=False).json()
        response = response[12]['links']['flickr_images']
        for id,url in enumerate(response):
            target_path = os.path.join(folder_name , 'SpaceX_{}.jpg'.format(id)) 
            get_hubble_image(url, target_path)            
    bot = Bot(like_delay=60)
    bot.login(username=instagram_username, password=instagram_password)

    if True:
            folder_path = "./pics"
            pics = glob.glob(folder_path + "/*.jpg")
            pics = sorted(pics)
            try:
                for pic in pics:
                    if pic in posted_pic_list:
                        continue

                    pic_name = pic[:-4].split("-")
                    pic_name = "-".join(pic_name[1:])
                    file_path = os.path.join(folder_path, pic_name + ".txt")
                    if os.path.isfile(file_path):
                        with open(file_path, "r") as file:
                            caption = file.read()
                    else:
                        caption = pic_name.replace("-", " ")
                    bot.upload_photo(pic, caption=caption)
                    if bot.api.last_response.status_code != 200:
                       
                        break

                    if pic not in posted_pic_list:
                        posted_pic_list.append(pic)
                        with open("pics.txt", "a", encoding="utf8") as f:
                            f.write(pic + "\n")

                    time.sleep(timeout)

            except Exception as e:
                print(str(e))
            for id_pictures, upload_image in enumerate(path_to_pictures):        
                bot.upload_photo(upload_image, caption="Nice pic!")
                time.sleep(60)
'''