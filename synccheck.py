import os
import requests
import re
import time

TG_API = 'апитокен бота тг'
TGchat_id = 'твой чат айди куда хочешь получать уведомления'

while True:
    try:
        f = os.popen('ironfish status')
        rd = f.read()
        pat_name = re.compile('(?<=Block\ Graffiti\ \ \ \ \ \ \ ).*(?=\\n)')
        name = pat_name.search(rd)
        name = name.group(0)
        pat_syncer = re.compile('(?<=Syncer\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ).*(?=-)')
        syncer = pat_syncer.search(rd)
        syncer = syncer.group(0)
        pat_status = re.compile('(?<=Node\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ).*(?=\\n)')
        status = pat_status.search(rd)
        status = status.group(0)
        pat_height = re.compile('(?<=\ \().*(?=\),\ Since\ HEAD)')
        height = pat_height.search(rd)
        height = height.group(0)
        pat_version = re.compile('(?<=Version\ \ \ \ \ \ \ \ \ \ \ \ \ \ ).*(?=\ @)')
        version = pat_version.search(rd)
        version = version.group(0)
    except:
        time.sleep(1)
    head_req = requests.get('https://explorer.ironfish.network/api/blocks/head')
    head_req = head_req.json()
    head_req = head_req['sequence']
    height = int(height)
    diff = head_req - height
    print(diff)
    print(head_req)
    print(height)

    if diff >= 4:
        print('ALARM')
        ans = requests.get(f'https://api.telegram.org/bot{TG_API}/sendMessage?chat_id={TGchat_id}&text=Граффити {name}\nHEAD блок ноды: {height} HEAD в эксплоррере: {head_req}\nВерсия ноды: {version}\n ❌❌❌❌❌❌❌❌❌')
        print(ans)
        time.sleep(10)
    time.sleep(900)
