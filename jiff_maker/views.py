from django.shortcuts import render
from jiff_maker.services.get_yt_video import get_yt_video
# Create your views here.
def test_view(request):
    get_yt_video('https://www.youtube.com/watch?v=FtdpDjV0dMY')
    return render(request,'jiff_maker/index.html')