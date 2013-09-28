import re
from random import shuffle
import requests
from PIL import Image
from io import BytesIO

app_name = 'get_your_own'
app_key = 'get_your_own'
api_cache = 'pix.out'

def get_pix(urls):
    urls = set(urls)
    urls = [url for url in urls if url is not '\n']
    shuffle(urls)
    urls = urls[:250]

    for url in urls:
        image_name = re.sub('^.+/', '', url)
        r = requests.get(url)
        i = Image.open(BytesIO(r.content))
        i.save('pix_files/'+image_name)

try:
    with open(api_cache) as infile:
        pic_urls = infile.read().splitlines()
        get_pix(pic_urls)

except IOError:
    '''
    https://mozillians.org/api/v1/users/?app_name=get_your_own&format=json&app_key=get_your_own&is_vouched=true&groups=summit2013-santa-clara,summit2013-toronto,summit2013-brussels
    '''
    next_set = '/api/v1/users/?app_name=' +\
                    app_name +\
                    '&format=json&app_key=' +\
                    app_key +\
                    '&limit=500&offset=0&is_vouched=true&groups=' +\
                    'summit2013-santa-clara,summit2013-toronto,summit2013-brussels'

    pic_urls = []
    with open(api_cache, 'w') as outfile:
        while next_set is not None:
            r = requests.get('https://mozillians.org' + next_set)
            next_set = r.json()['meta'].get('next', None)
            for o in r.json()['objects']:
                if 'photo' in o:
                    pic_urls.append(o['photo'])
                    outfile.write("%s\n" % o['photo'])

    get_pix(pic_urls)


