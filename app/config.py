import os

import pytz

warsaw_time = pytz.timezone('Europe/Warsaw')

path = os.path.dirname(os.path.realpath(__file__))

headers = {
    'authority': 'content.viaplay.pl',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': 'OptanonAlertBoxClosed=2022-12-22T20:15:13.761Z; _gcl_au=1.1.471429287.1671740114; _ga=GA1.2.1278460483.1671740125; _scid=c391f2b8-392c-4ac6-9065-30b8722835c1; _tt_enable_cookie=1; _ttp=sfeLUtQuvM260zLOr-Oq0yFBzUU; Viaplay-ClientId=ca7bd3e5-f536-4f7d-97c8-a4a6112c5f3c; _hjSessionUser_2514801=eyJpZCI6IjJlNmJlYmYwLWY0MjktNTk5Ny1iYWNlLWQ2NGRkOGMwZDllNiIsImNyZWF0ZWQiOjE2NzE3NDAxMjU3ODAsImV4aXN0aW5nIjp0cnVlfQ==; RT="z=1&dm=viaplay.pl&si=02327516-fe85-4ff1-b938-4b30fb797074&ss=lcb3djld&sl=1&tt=3hm&bcn=%2F%2F02179913.akstat.io%2F&ld=47s&ul=10c7&hd=10dd"; huginSessionId=b1ce135b-d6df-4703-b9a4-f8dc732c8d77; _gid=GA1.2.115418501.1672686994; _hjSession_2514801=eyJpZCI6ImNiMzYwZmNjLTZkYWQtNDM4MC1hMGQ4LTI2Y2E4MGZmNTdjNyIsImNyZWF0ZWQiOjE2NzI2ODY5OTQ0MDUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jan+02+2023+20%3A51%3A31+GMT%2B0100+(Central+European+Standard+Time)&version=6.37.0&isIABGlobal=false&hosts=&consentId=a84ce81a-00a6-4558-a9c1-5a9928adb163&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0007%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false; _uetsid=f89565408ad111edbba30d3bd204a694; _uetvid=5ed6db30823511edab3f917d801c8514; _gat_UA-21114283-54=1; huginSequenceNumber=110',
    'dnt': '1',
    'if-none-match': 'W/"2437d-REae+moDkA7AH2PgYvtHp7subZ4"',
    'origin': 'https://viaplay.pl',
    'referer': 'https://viaplay.pl/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

m3u_url = 'http://31.42.176.205/play/list?username=eafbede8ae23d171&password=e57b21bfdfc0ef62&type=m3u&output=ts'

carousels = ('Główne transmisje', 'Premier League', 'Skróty meczów NHL', 'Bundesliga', 'Najlepsze skróty meczów')
base_url = 'https://content.viaplay.pl/pcdash-pl/sport'