#-*- coding:utf-8 -*-
import requests
import json

APPID = ''
SECRET = ''


#API URL BEGIN
ACCESSTOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token'
CUSTOM_URL = 'https://api.weixin.qq.com/cgi-bin/message/custom/send'
USERINFO_URL = 'https://api.weixin.qq.com/cgi-bin/user/info'
QRCODE_URL = 'https://api.weixin.qq.com/cgi-bin/qrcode/create'
CREATE_MENU_URL = 'https://api.weixin.qq.com/cgi-bin/menu/create'
GET_MUNU_URL = 'https://api.weixin.qq.com/cgi-bin/menu/get'
DELETE_MUNU_URL = 'https://api.weixin.qq.com/cgi-bin/menu/delete'
GET_FOLLOWER_URL = 'https://api.weixin.qq.com/cgi-bin/user/get'
UPLOAD_MEDIA_URL = 'http://file.api.weixin.qq.com/cgi-bin/media/upload?type=image&'
#API URL END 

def subscribe_qrcode(parameters, kind = 'QR_SCENE'):
    payload = {
            'expire_seconds': 1800,
            'action_name': kind,
            'action_info': {
                'scene': {
                    'scene_id': parameters 
                    }
                }
            }
    r = requests.post(QRCODE_URL + '?' + 'access_token=' + get_access_token(), data=json.dumps(payload))
    print r.text
    return

def getfollower():
    data = {
            'access_token': get_access_token()
            }
    r = requests.get(GET_FOLLOWER_URL, params=data)
    print r.content
    return

def getinfo(fakeId):
    data = {
            'access_token': get_access_token(),
            'openid': fakeId 
            }
    r = requests.get(USERINFO_URL, params=data)
    print r.content
    return

def get_access_token(): 
    data = {
            'grant_type': 'client_credential',
            'appid': APPID,  
            'secret': SECRET    
            }
    r = requests.get(ACCESSTOKEN_URL, params=data)
    #print r.content
    return json.loads(r.content)['access_token']

def lookup_menu():
    data = {
            'access_token': get_access_token(),
            }
    r = requests.get(GET_MUNU_URL, params=data)
    print r.content
    return

def delete_menu():
    data = {
            'access_token': get_access_token(),
            }
    r = requests.get(DELETE_MUNU_URL, params=data)
    print r.content
    return

def create_menu():
    payload = {
            'button': [
                {
                    'name': '找信息',
                    'sub_button': [
                        {
                            'type': 'view',
                            'name': '二手车',
                            'url': 'http://www.baixing.com/m/ershouqiche?src=weixinmenu'
                            },
                        {
                            'type': 'view',
                            'name': '找全职工作',
                            'url': 'http://www.baixing.com/m/gongzuo/?select=category&src=weixinmenu'
                            },
                        {
                            'type': 'view',
                            'name': '找兼职工作',
                            'url': 'http://www.baixing.com/m/jianzhi/?select=category&src=weixinmenu'
                            },
                        {
                            'type': 'view',
                            'name': '租房',
                            'url': 'http://www.baixing.com/m/zhengzu?src=weixinmenu'
                            },
                        {
                            'type': 'view',
                            'name': '更多',
                            'url': 'http://www.baixing.com/m/?src=weixinmenu'
                            }
                        ]
                    }, 
                {
                    'type': 'view',
                    'name': '发布',
                    'url': 'http://www.baixing.com/m/fabu?src=weixinmenu'
                    },
                {
                    'type': 'click',
                    'name': '继续订阅',
                    'key': 'continuepush'
                    }
                ]
            }
    r = requests.post(CREATE_MENU_URL + '?' + 'access_token=' + get_access_token(), data=json.dumps(payload, ensure_ascii = False))
    print r.text
    return


def custom_reply(fakeId, content):
    payload = {
            'touser': fakeId,
            'msgtype': 'text',
            'text': {
                'content': content 
                }
            }
            #'msgtype': 'image',
            #'image': {
            #    'media_id': upload_media()
            #    }
            #}
    #payload = {
    #        'touser': fakeId,
    #        'msgtype': 'news',
    #        'news': {
    #            'articles': [
    #                {
    #                    'title': '',
    #                    'description': 'one',
    #                    'url': 'http://www.baixing.com',
    #                    'picurl': 'http://ww4.sinaimg.cn/large/92540662jw1dugq4j86bpj.jpg'
    #                    }
    #                #{
    #                #    'title': 'happy day two',
    #                #    'description': 'two',
    #                #    'url': 'http://www.58.com',
    #                #    'picurl': 'http://ww4.sinaimg.cn/large/92540662jw1dugq35jk5qj.jpg'
    #                #    }
    #                ]
    #            }
    #        }
    r = requests.post(CUSTOM_URL + '?' + 'access_token=' + get_access_token(), data=json.dumps(payload, ensure_ascii = False))
    print r.text
    return

def upload_media():
    files = {'file': open('QQ.jpg', 'rb')}
    r = requests.post(UPLOAD_MEDIA_URL + 'access_token=' + get_access_token(), files = files)
    print r.text
    return json.loads(r.text)['media_id']


#login()
#get_access_token()
#custom_reply()
#getinfo()
#subscribe_qrcode()
#create_menu()
#delete_menu()
#lookup_menu()
#getfollower()
#upload_media()
