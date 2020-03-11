import requests
from bs4 import BeautifulSoup
import time
import re
from django.http import JsonResponse


def get_account(request):
    #获取搜索词
    info_list=[]
    search = request.POST.get('search_word')
    #for循环切换页数
    for page in range(1,2):
        #爬取页面文字信息
        url = 'https://weixin.sogou.com/weixin?query=%s&_sug_type_=&s_from=input&_sug_=y&type=1&page=%d&ie=utf8'%(search,page)
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
        res = requests.get(url,headers=header)
        html=res.text
        #bs4初步信息
        soup=BeautifulSoup(html,"html.parser")
        titles = soup.find_all('div',{'class':'txt-box'})
        imgs = soup.find_all('div',{'class':'img-box'})
        for count in range(len(titles)):
            info={}
            #提取公众号名称、微信ID,存到字典info中
            title=titles[count]
            ##名称(account)
            j=title.find(attrs='tit').text
            # print(j[1:-1])
            info['account']=str(j[1:-1])
            ##微信ID(weChatID)
            k=title.find(attrs='info').text
            # print(k[:-1])
            info['weChatID']=str(k[4:-1])
            # print('名称、ID存入成功')
            #提取网页链接、头像链接，存入字典info中
            i =imgs[count]
            #网页链接
            url_link = str(i.find('a'))
            pat = re.compile('href=\"'+'(.*?)'+'" target',re.S)
            result=pat.findall(url_link)
            result = 'https://weixin.sogou.com'+result[0].replace('amp;','')
            info['url_link']=result
            #头像链接
            img_link=str(i.find('a').find('img'))
            pat1 = re.compile('src=\"'+'(.*?)'+'"/',re.S)
            pat1=pat1.findall(img_link)[0]
            result1 = 'https:'+pat1
            info['photo_link']=result1
            info_list.append(info)
        print('第%d轮'%page)
        time.sleep(1)

    #函数返回值：info_list列表，内嵌套字典
    return JsonResponse({'data': info_list})

if __name__ == '__main__':
    aa = get_account()
    for a in aa:
        print(a['account'])
