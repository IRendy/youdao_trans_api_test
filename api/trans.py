
# -*- coding: utf-8 -*

import sys
import uuid
import requests
import hashlib
import time
from importlib import reload
import json

import time

reload(sys)

class chosen_lan(object): 
    """
    支持的语言类型
    """
    中文 = 'zh-CHS'
    中文繁体 = 'zh-CHT'
    英文 = 'en'
    日文 = 'ja'
    韩文 = 'ko'
    法文 = 'fr'
    西班牙文 = 'es'
    葡萄牙文 = 'pt'
    意大利文 = 'it'
    俄文 = 'ru'
    越南文 = 'vi'
    德文 = 'de'
    阿拉伯文 = 'ar'
    印尼文 = 'id'
    南非荷兰语 = 'af'
    波斯尼亚语 = 'bs'
    保加利亚语 = 'bg'
    粤语 = 'yue'
    加泰隆语 = 'ca'
    克罗地亚语 = 'hr'
    捷克语 = 'cs'
    丹麦语 = 'da'
    荷兰语 = 'nl'
    爱沙尼亚语 = 'et'
    斐济语 = 'fj'
    芬兰语 = 'fi'
    希腊语 = 'el'
    海地克里奥尔语 = 'ht'
    希伯来语 = 'he'
    印地语 = 'hi'
    白苗语 = 'mww'
    匈牙利语 = 'hu'
    斯瓦希里语 = 'sw'
    克林贡语 = 'tlh'
    拉脱维亚语 = 'lv'
    立陶宛语 = 'lt'
    马来语 = 'ms'
    马耳他语 = 'mt'
    挪威语 = 'no'
    波斯语 = 'fa'
    波兰语 = 'pl'
    克雷塔罗奥托米语 = 'otq'
    罗马尼亚语 = 'ro'
    塞尔维亚语西里尔文  = 'sr-Cyrl'
    塞尔维亚语拉丁文  = 'sr-Latn'
    斯洛伐克语 = 'sk'
    斯洛文尼亚语 = 'sl'
    瑞典语 = 'sv'
    塔希提语 = 'ty'
    泰语 = 'th'
    汤加语 = 'to'
    土耳其语 = 'tr'
    乌克兰语 = 'uk'
    乌尔都语 = 'ur'
    威尔士语 = 'cy'
    尤卡坦玛雅语 = 'yua'
    阿尔巴尼亚语 = 'sq'
    阿姆哈拉语 = 'am'
    亚美尼亚语 = 'hy'
    阿塞拜疆语 = 'az'
    孟加拉语 = 'bn'
    巴斯克语 = 'eu'
    白俄罗斯语 = 'be'
    宿务语 = 'ceb'
    科西嘉语 = 'co'
    世界语 = 'eo'
    菲律宾语 = 'tl'
    弗里西语 = 'fy'
    加利西亚语 = 'gl'
    格鲁吉亚语 = 'ka'
    古吉拉特语 = 'gu'
    豪萨语 = 'ha'
    夏威夷语 = 'haw'
    冰岛语 = 'is'
    伊博语 = 'ig'
    爱尔兰语 = 'ga'
    爪哇语 = 'jw'
    卡纳达语 = 'kn'
    哈萨克语 = 'kk'
    高棉语 = 'km'
    库尔德语 = 'ku'
    柯尔克孜语 = 'ky'
    老挝语 = 'lo'
    拉丁语 = 'la'
    卢森堡语 = 'lb'
    马其顿语 = 'mk'
    马尔加什语 = 'mg'
    马拉雅拉姆语 = 'ml'
    毛利语 = 'mi'
    马拉地语 = 'mr'
    蒙古语 = 'mn'
    缅甸语 = 'my'
    尼泊尔语 = 'ne'
    齐切瓦语 = 'ny'
    普什图语 = 'ps'
    旁遮普语 = 'pa'
    萨摩亚语 = 'sm'
    苏格兰盖尔语 = 'gd'
    塞索托语 = 'st'
    修纳语 = 'sn'
    信德语 = 'sd'
    僧伽罗语 = 'si'
    索马里语 = 'so'
    巽他语 = 'su'
    塔吉克语 = 'tg'
    泰米尔语 = 'ta'
    泰卢固语 = 'te'
    乌兹别克语 = 'uz'
    南非科萨语 = 'xh'
    意第绪语 = 'yi:'
    约鲁巴语 = 'yo'
    南非祖鲁语 = 'zu'
    自动识别 = 'auto'

class ApiTrans(object):
    """
    ApiTrans 文本翻译
    """

    YOUDAO_URL = 'https://openapi.youdao.com/api'

    def __init__(self, APP_KEY: str, APP_SECRET: str, trans_from:chosen_lan = chosen_lan.自动识别, trans_to:chosen_lan = chosen_lan.英文):
        self.__APP_KEY = APP_KEY #
        self.__APP_SECRET = APP_SECRET
        self.trans_from = trans_from
        self.trans_to = trans_to

    def _encrypt(self, signStr):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode('utf-8'))
        return hash_algorithm.hexdigest()

    def _truncate(self, q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

    def _do_request(self, data):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return requests.post(self.YOUDAO_URL, data=data, headers=headers)

    def lan_opt(self, trans_from: str, trans_to: str):

        """
        选择语言转换类型
        """
        self.trans_from = trans_from
        self.trans_to = trans_to

    def trans(self, q: str):

        """
        翻译
        """

        q = q
        data = {}
        data['from'] = self.trans_from
        data['to'] = self.trans_to
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = self.__APP_KEY + self._truncate(q) + salt + curtime + self.__APP_SECRET
        sign = self._encrypt(signStr)
        data['appKey'] = self.__APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign
        # data['vocabId'] = "您的用户词表ID"

        response = self._do_request(data)
        contentType = response.headers['Content-Type']
        if contentType == "audio/mp3":
            millis = int(round(time.time() * 1000))
            filePath = "./" + str(millis) + ".mp3"
            fo = open(filePath, 'wb')
            fo.write(response.content)
            fo.close()
        else:
            txt = json.loads(response.text)['translation'][0]
            # print(txt)
            return txt
    
    def 连珠炮(self):
        while True:
            q = input(f"> {self.trans_from}: ")
            if not q:
                break
            elif q == '0':
                trans_from = input('from:')
                trans_to = input("to:")
                if trans_from in dir(chosen_lan) and trans_to in dir(chosen_lan):
                    self.trans_from = eval(f"chosen_lan.{trans_from}")
                    self.trans_to = eval(f"chosen_lan.{trans_to}")
                    continue
                else:
                    print("Invalid Languages Options")
                    continue
            a = self.trans(q)
            print(f"{self.trans_to}: {a}")

    def 虚空之境(self, filename: str):
        with open(filename,'r', encoding='utf-8') as f:
            return self.trans(f.read())

if __name__ == '__main__':
    # cli = client(APP_KEY, APP_SECRET, chosen_lan.中文, chosen_lan.英文)
    # cli.trans("老子天下第一可爱")
    print(chosen_lan("中文"))