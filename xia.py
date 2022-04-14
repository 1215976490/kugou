
# -*- coding：utf-8 -*-
import sys
import you_get
import kugou

url = "https://www.kugou.com/yy/special/single/5339195.html"

output_dir = 'songs/'

songs = kugou.get_info(url)

kugou.download(songs['info'],output_dir)
