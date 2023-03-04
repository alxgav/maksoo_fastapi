import config
import requests
import pytz
import xml.etree.cElementTree as xml
import os

from models import SportData

from datetime import datetime
from m3u_parser import M3uParser

from config import warsaw_time
from pprint import pprint

time_utc = datetime.utcnow()
time_utc = pytz.utc.localize(time_utc, is_dst=None).astimezone(warsaw_time)
time_utc = datetime.strftime(time_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
time_utc = datetime.strptime(time_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
# time_utc = datetime.fromisoformat(time_utc[:-1])

print(time_utc)




''' get data from m3u this function return dictionary of m3u file'''
def get_m3u() -> dict:
    parser = M3uParser()
    parser.parse_m3u(config.m3u_url)
    return parser.get_list()


''' get response of links from main page'''
def get_url() -> list:
    urls = []
    response = requests.get(config.base_url,  headers=config.headers)
    data_json = response.json()["_embedded"]["viaplay:blocks"]
    for item in data_json:
        if config.carousels[2] == item["title"]:
            _links = item['_links']["self"]["href"]
            urls.append(_links)
            response = requests.get(_links,  headers=config.headers)
            href = response.json()["_links"]["next"]['href']
            urls.append(href)
    # urls.append(config.base_url)
    return urls


'''Create XML file'''
def createXML(data=None) -> None:
    filename = f'{config.path}/sport.xml'
    if os.path.exists(filename):
        os.remove(filename)
        print('file deleted')
    rerponse = xml.Element("events") 
    for item in data:
        data_items = xml.SubElement(rerponse,"event", dict(id=item['id'], start=item['start'], stop=item['end']))
        xml.SubElement(data_items,"title", dict(lang="pl")).text = str(item['title'])
        xml.SubElement(data_items,"description", dict(lang="pl")).text = str(item['description'])
        xml.SubElement(data_items,"url").text = str(item['url'])
        xml.SubElement(data_items,"icon", dict(src=item['img_url']))
        xml.SubElement(data_items,"stream", dict(src=item['stream']))
    xml_file = xml.ElementTree(rerponse)
    xml_file.write(filename, xml_declaration=True, method='xml', encoding='UTF-8')

    


def get_football_data(m3u) -> list:
    response = requests.get(config.base_url,  headers=config.headers)
    data_json = response.json()
    content = []
    data_title = []
    for item in data_json["_embedded"]["viaplay:blocks"]:
        data = ''
        if "_embedded" in item:
            for i_embedded in item["_embedded"]:
                if "viaplay:products" in i_embedded:
                    data = item["_embedded"]["viaplay:products"]
                    for content_item in data:
                        
                        if "title" in content_item["content"]:
                            title = content_item["content"]["title"]
                            id = content_item["system"]["guid"]
                            url = ''
                            image = content_item["content"]["images"]["landscape"]["url"]
                            try:
                                description = content_item["content"]["format"]["title"]
                            except:
                                description = ''
                            try:
                                description_ = content_item["content"]['originalTitle']
                            except:
                                description_ = ''
                            description = description +' | '+ description_
                            url = f'https://viaplay.pl/sport/{content_item["publicPath"]}'
                            try:
                                start = content_item["epg"]["start"]
                            except:
                                start = ''
                            try:
                                end = content_item["epg"]["end"]
                                print(end)
                            except:
                                end = ''
                            for m3u_item in m3u:
                                if title in m3u_item['name']:
                                    stream = m3u_item['url']
                                    if time_utc > datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ"):

                                        if id not in data_title :
                                            sport_data = SportData(id=id,
                                                                title=title,
                                                                description=description,
                                                                url=url,
                                                                img_url=image,
                                                                start=start,
                                                                end=end,
                                                                stream=stream).dict()
                                            content.append(sport_data)
                                            data_title.append(title)
    return content


def get_NHL_data(m3u) -> list:
    content = []
    data_title = []
    pprint(get_url())
    for link in get_url():
        data = ''
        response = requests.get(link,  headers=config.headers)
        data_json = response.json()
        if "viaplay:products" in data_json["_embedded"]:
            data = data_json["_embedded"]["viaplay:products"]
            for content_item in data:
                if "title" in content_item["content"]:
                    title = content_item["content"]["title"]
                    id = content_item["system"]["guid"]
                    url = ''
                    image = content_item["content"]["images"]["landscape"]["url"]
                    description = content_item["content"]["synopsis"]
                    start = content_item["system"]["availability"]["start"]
                    end = content_item["system"]["availability"]["end"]
                    for m3u_item in m3u:
                        if title in m3u_item['name']:
                            stream = m3u_item['url']
                            if time_utc < datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%fZ"):
                                if id not in data_title:
                                    sport_data = SportData(id=id,
                                                        title=title,
                                                        description=description,
                                                        url=url,
                                                        img_url=image,
                                                        start=start,
                                                        end=end,
                                                        stream=stream).dict()
                                    content.append(sport_data)
                                    data_title.append(title)
    return content


def get_all_data() -> list:
    m3u = get_m3u()
    pprint(m3u)
    return get_football_data(m3u) + get_NHL_data(m3u)