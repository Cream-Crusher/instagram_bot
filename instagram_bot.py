import requests
import os
import glob
import sys
import time
from io import open
from PIL import Image
from dotenv import load_dotenv


def get_hubble_image(url, target_path):
    print(url)
    response = requests.get(url)
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
    url_full=[]
    reference_number = ['1','2','3']  
    instagram_username = os.getenv('INSTAGRAM_USERNAME')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD')
    for  reference_number in range(1, 4):
        url ='http://hubblesite.org/api/v3/image/{}'.format(reference_number)
        response = requests.get(url).json() 
        response = response['image_files'][-1]['file_url']
        url = response
        url='https:'+url
        target_path = os.path.join(folder_name , 'api_hubblev{}.jpg'.format(reference_number)) 
        get_hubble_image(url, target_path)




#get_hubble_image(url, target_path)
'''            
    sys.path.append(os.path.join(sys.path[0], "../../"))
    from instabot import Bot  

    posted_pic_list = []
    try:
        with open("pics.txt", "r", encoding="utf8") as f:
            posted_pic_list = f.read().splitlines()
    except Exception:
        posted_pic_list = []

    timeout = 24 * 60 * 60 

    bot = Bot(like_delay=60)
    bot.login(username=instagram_username, password=instagram_password)

    while True:
        folder_path = "./pics"
        pics = glob.glob(folder_path + "/*.jpg")
        pics = sorted(pics)
        try:
            for pic in pics:
                if pic in posted_pic_list:
                    continue

                pic_name = pic[:-4].split("-")
                pic_name = "-".join(pic_name[1:])

                print("upload: " + pic_name)

                description_file = folder_path + "/" + pic_name + ".txt"

                if os.path.isfile(description_file):
                    with open(description_file, "r") as file:
                        caption = file.read()
                else:
                    caption = pic_name.replace("-", " ")

                bot.upload_photo(pic, caption=caption)
                if bot.api.last_response.status_code != 200:
                    print(bot.api.last_response)
                   
                    break

                if pic not in posted_pic_list:
                    posted_pic_list.append(pic)
                    with open("pics.txt", "a", encoding="utf8") as f:
                        f.write(pic + "\n")

                time.sleep(timeout)

        except Exception as e:
            print(str(e))
        for id, upload_image in enumerate(path_to_pictures):        
            bot.upload_photo(upload_image, caption="Nice pic!")
            time.sleep(60)
'''







'''
def get_hubble_image(url, folder_name, target_path):
    

    
    response = requests.get(url)
    if response.url.startswith('full',73 ,77) or response.url.startswith('full',72 ,76):
        response.raise_for_status() 
        with open(folder_name, 'wb') as the_path_to_the_file: 
            the_path_to_the_file.write(response.content) 
            image = Image.open(target_path)
            image.thumbnail((1080, 1080)) 
            image.save(target_path)          
            path_to_pictures.append(target_path)
      
if __name__ == '__main__':
    load_dotenv()
    folder_name = 'images'
    path_to_pictures = []
    reference_number = ['1','2','3']  
    instagram_username = os.getenv('INSTAGRAM_USERNAME')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD')
    for  id,reference_number in enumerate(reference_number, 1):
        url ='http://hubblesite.org/api/v3/image/{}'.format(id)
        response = requests.get(url).json() 
        response = response['image_files']             
        for id, url in enumerate(response, 1):
            target_path = os.path.join(folder_name , 'api_hubblev{}_{}.JPG'.format(reference_number,id)) 
            url='https:'+url['file_url']
            get_hubble_image(url, target_path)
            
    sys.path.append(os.path.join(sys.path[0], "../../"))
    from instabot import Bot  

    posted_pic_list = []
    try:
        with open("pics.txt", "r", encoding="utf8") as f:
            posted_pic_list = f.read().splitlines()
    except Exception:
        posted_pic_list = []

    timeout = 24 * 60 * 60 

    bot = Bot(like_delay=60)
    bot.login(username=instagram_username, password=instagram_password)

    while True:
        folder_path = "./pics"
        pics = glob.glob(folder_path + "/*.jpg")
        pics = sorted(pics)
        try:
            for pic in pics:
                if pic in posted_pic_list:
                    continue

                pic_name = pic[:-4].split("-")
                pic_name = "-".join(pic_name[1:])

                print("upload: " + pic_name)

                description_file = folder_path + "/" + pic_name + ".txt"

                if os.path.isfile(description_file):
                    with open(description_file, "r") as file:
                        caption = file.read()
                else:
                    caption = pic_name.replace("-", " ")

                bot.upload_photo(pic, caption=caption)
                if bot.api.last_response.status_code != 200:
                    print(bot.api.last_response)
                   
                    break

                if pic not in posted_pic_list:
                    posted_pic_list.append(pic)
                    with open("pics.txt", "a", encoding="utf8") as f:
                        f.write(pic + "\n")

                time.sleep(timeout)

        except Exception as e:
            print(str(e))
        for id, upload_image in enumerate(path_to_pictures):        
            bot.upload_photo(upload_image, caption="Nice pic!")
            time.sleep(60)
'''
            
