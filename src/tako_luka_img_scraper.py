import argparse
import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

TARGET_SUFFIX = ('.gif', '.jpg', '.jpeg', '.png')

os.environ['REQUESTS_CA_BUNDLE'] = os.path.abspath('../certs/cacert.pem')


def fetch_page(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise ValueError(
            'page response status code is {0}'.format(res.status_code))
    return res.text


def download_img(url, dst_dir):
    if not url.endswith(TARGET_SUFFIX):
        return
    res = requests.get(url)
    if res.status_code != 200:
        return
    print('downloading a file...')
    print(url)
    time.sleep(1)
    with open(os.path.join(dst_dir, os.path.basename(url)), 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('url', help='page url')
    parser.add_argument('-o', '--outpath', default='out', help='output path')
    parser.add_argument('-s', '--selector', default='img', help='CSS selector')
    parser.add_argument('-a', '--attr', default='src', help='target attribute')
    args = parser.parse_args()

    soup = BeautifulSoup(fetch_page(args.url), 'html.parser')
    img_urls = map(lambda img: img.get(args.attr), soup.select(args.selector))
    if not os.path.exists(args.outpath):
        os.makedirs(args.outpath)
    for img_url in img_urls:
        download_img(urljoin(args.url, img_url), args.outpath)
