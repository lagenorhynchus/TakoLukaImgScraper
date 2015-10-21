import argparse
import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

os.environ['REQUESTS_CA_BUNDLE'] = os.path.abspath('../certs/cacert.pem')
file_names = set()


def fetch_page(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise ValueError(
            'page response status code is {0}'.format(res.status_code))
    return res.text


def download_img(url, dst_dir, extensions):
    if not url.endswith(extensions):
        return
    file_name = os.path.basename(url)
    if file_name in file_names:
        return
    file_names.add(file_name)
    print('downloading a file...')
    print(url)
    time.sleep(1)
    res = requests.get(url)
    if res.status_code != 200:
        return
    with open(os.path.join(dst_dir, file_name), 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('url', help='page url')
    parser.add_argument('-o', '--outpath', default='out',
                        help='output path')
    parser.add_argument('-s', '--selector', default='img',
                        help='CSS selector')
    parser.add_argument('-a', '--attribute', default='src',
                        help='target attribute')
    parser.add_argument('-e', '--extension', nargs='+',
                        default=['.gif', '.jpg', '.jpeg', '.png'],
                        help='target file extensions')
    args = parser.parse_args()

    soup = BeautifulSoup(fetch_page(args.url), 'html.parser')
    img_urls = map(lambda img: img.get(args.attribute),
                   soup.select(args.selector))
    if not os.path.exists(args.outpath):
        os.makedirs(args.outpath)
    extensions = tuple(args.extension)
    for img_url in img_urls:
        download_img(urljoin(args.url, img_url), args.outpath, extensions)
