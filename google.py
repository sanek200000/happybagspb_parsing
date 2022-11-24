#from time import sleep
from icrawler.builtin import GoogleImageCrawler
import json


def google_image_downloader(r_dir, k_word, num):
    filters = dict(
        type = 'photo',
        # license='noncommercial',
    )
    crawler = GoogleImageCrawler(storage={'root_dir': f'./img/{r_dir}'})
    crawler.crawl(
        keyword = k_word,
        max_num = num,
        overwrite = True,
        filters = filters,
    )
    pass


def read_shopjson():
    with open('shop.json', encoding='utf-8') as file:
        src = json.load(file)
    return src


def make_readme(uid, item, url):
    with open(f'./img/{uid}/readme.txt', 'w', encoding='utf-8') as file:
        file.write(f'{uid}\n{item}\n{url}')
    pass


def google_main():
    src = read_shopjson()

    tmp = 0
    for key in src:
        uid = key
        item = src[key][0]
        url = src[key][1]

        print('\n', uid, item, url, sep='\n')
        google_image_downloader(uid, item, 10)
        make_readme(uid, item, url)

        #tmp += 1
        if tmp == 2:
            break


if __name__ == "__main__":
    #google_main()
    print("Hello world!")
else:
    print("File one executed when imported")
