from TextProcessor import TextProcesser
from models import *
from utils import *
from conf import start_day
import json


class smileTextProcessor(TextProcesser):
    def __init__(self):
        super(smileTextProcessor, self).__init__(r'这次活动大家玩的开心吗')

    def process(self, msg, match):
        _total_smile_num = 0
        records = Occure
        total_msg = '本次硅谷之行共拍了{}张照片'.format(PictureCollections.objects( date__gt=start_day).count())
        _top_smile_num = Ocurrences.objects(expression__gt=0).count()
        result_msg = '共有%d张笑脸'%(_top_smile_num)
        reply_msg = total_msg + result_msg
        msg.reply(reply_msg)
