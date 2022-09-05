import logging
import os

import pytube
from django.conf import settings

logger = logging.getLogger(__name__)

DOWNLOAD_BASE_PATH = settings.BASE_DIR / 'jiff_maker/asset/download_videos/'


def get_yt_video(url:str):
    yt = pytube.YouTube(url)
    output_path = DOWNLOAD_BASE_PATH / yt.video_id
    file_path = str(output_path)+'/'+yt.title+'.mp4'

    output = {
        "video_id":yt.video_id,
        'file_path':file_path,
    }

    if  os.path.exists(output_path) and os.path.isfile(file_path):
        return output
    
    yt.streams\
        .filter(res='360p',file_extension='mp4')\
        .first()\
        .download(
            output_path=output_path,
            timeout=1000
        )

    return output
