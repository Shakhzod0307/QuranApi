import requests

from pprint import pprint as print

sura = 96
oyat = 1
tafsir = 'uzb-muhammadsodikmu'

url_sura = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json'
url_oyat = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json'


# Quran dagai surani json shaklda consoleda chiqaradi
r = requests.get(url_sura)
res = r.json()


# bu qismda Quran oyatini text qilib consolega chiqaradi
# r = requests.get(url_oyat)
# res = r.json()['text']


print(r.status_code)
print(res)


