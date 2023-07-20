import allure
from allure_commons.types import AttachmentType


def attach_video(video_url):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" + video_url + "'></video></body></html>'"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')