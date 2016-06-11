# TakoLukaImgScraper

Webページ内の画像ファイル収集プログラム(スクレイパー)。

## Usage
```console
$ tako_luka_img_scraper -h
usage: tako_luka_img_scraper.py [-h] [-o OUTPATH] [-s SELECTOR] [-a ATTRIBUTE]
                                [-e EXTENSION [EXTENSION ...]]
                                url

positional arguments:
  url                   page url

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPATH, --outpath OUTPATH
                        output path (default: out)
  -s SELECTOR, --selector SELECTOR
                        CSS selector (default: img)
  -a ATTRIBUTE, --attribute ATTRIBUTE
                        target attribute (default: src)
  -e EXTENSION [EXTENSION ...], --extension EXTENSION [EXTENSION ...]
                        target file extensions (default: ['.gif', '.jpg',
                        '.jpeg', '.png'])
```
