from time import sleep
from icrawler.builtin import GoogleImageCrawler
import json


def google_image_downloader(r_dir, k_word, num):
    filters = dict(
        type='photo',
        # license='noncommercial',
    )
    crawler = GoogleImageCrawler(storage={'root_dir': f'./img/{r_dir}'})
    crawler.crawl(
        keyword=k_word,
        max_num=num,
        overwrite=True,
        filters=filters,
    )
    pass


def read_json():
    with open('shop.json', encoding='utf-8') as file:
        src = json.load(file)
    return src


def make_readme(uid, item, url):
    with open(f'./img/{uid}/readme.txt', 'w', encoding='utf-8') as file:
        file.write(f'{uid}\n{item}\n{url}')
    pass


def main():
    src = read_json()

    tmp = 0
    for key, val in src.items():
        uid = key
        item = val[0]
        url = val[1]

        google_image_downloader(r_dir=uid, k_word=item, num=10)
        make_readme(uid=uid, item=item, url=url)

        #tmp += 1
        if tmp == 2:
            break


if __name__ == "__main__":
    main()
    pass
else:
    print("File one executed when imported")
