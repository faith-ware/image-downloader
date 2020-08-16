import requests,os,bs4,webbrowser
from pathlib import Path
site = "https://stocksnap.io/search/"
the_search = input("Enter image to search for and download from stocksnap.io\n")

website = site + the_search
os.makedirs("img_downloader", exist_ok=True) 

res = requests.get(website)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
imgElem = soup.select("#main a")

imageslink = []
for a in range(len(imgElem)):
    theImage = imgElem[a].get("href")
    if theImage.startswith(r"/"):
        imageslink.append("https://stocksnap.io" + theImage)
count = 0
print("Downloading images...")
for i in range(2):
    image_link_res = requests.get(imageslink[i])
    image_link_res.raise_for_status()  
    image_link_soup = bs4.BeautifulSoup(image_link_res.text,"html.parser")
    img_link_elem = image_link_soup.select("figure img")
    img_src = img_link_elem[0].get("src")
    img_src_res = requests.get(img_src)
    count = count + 1
    img_format = Path(img_src).parts[-1].split(".")[-1]
    img_name = Path(img_src).parts[-1].split(".")[0]
    the_extension = "." + img_format
    img_file = open(os.path.join("img_downloader",f"image {img_name} {count}" + the_extension),"wb")
    for the_bytes in img_src_res.iter_content(100000):
        img_file.write(the_bytes)
    img_file.close()
    print(f'Image {img_name} {count} has been downloaded to ' + r"C:\Users\USER\Desktop\Python_practice\Web_scraping\img_downloader")    
