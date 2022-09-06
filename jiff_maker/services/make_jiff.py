import ffmpeg,os
from django.conf import settings
from datetime import datetime

OUTPUT_URL = settings.BASE_DIR / 'jiff_maker/asset/jiffs/'

def make_jiff_from_video(video_file_path:str,startTime:int,endTime:int):
    if not os.path.exists(str(OUTPUT_URL)):
        os.mkdir(str(OUTPUT_URL))
    output_file = OUTPUT_URL / f'output_{(datetime.now().timestamp())}.gif'
    stream = ffmpeg.input(video_file_path)
    stream = ffmpeg.trim(stream,start=startTime,end=endTime)
    stream = ffmpeg.output(stream,str(output_file))
    ffmpeg.run(stream)
    return output_file


    
    
    