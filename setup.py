import py2exe
from distutils.core import setup

py2exe_options = {
    'compressed': 1,
    'optimize': 2,
    'bundle_files': 1
}

build_exe_options = {}

setup(
    options={
        'py2exe': py2exe_options,
        'build_exe': build_exe_options
    },
    data_files=[('certs', ['certs/cacert.pem'])],
    console=[
        {'script': 'src/tako_luka_img_scraper.py'}
    ],
    zipfile=None
)
