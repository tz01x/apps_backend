from django.shortcuts import render
from jiff_maker.services.get_yt_video import get_yt_video
from jiff_maker.services.make_jiff import make_jiff_from_video
import pathlib
from django.conf import settings


def test_view(request):
    info = get_yt_video('https://www.youtube.com/watch?v=FtdpDjV0dMY')
    output_file_path = make_jiff_from_video(info['file_path'],2,4)
    
    path = pathlib.Path(settings.BASE_DIR / 'jiff_maker/asset/jiffs/')
    gif_files=[]
    for p in path.glob('*.gif'):
        gif_files.append(p.name)

    return render(request,'jiff_maker/index.html',{
        'gif_files':gif_files
    })