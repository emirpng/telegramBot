from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import bot
import requests
from bs4 import BeautifulSoup

token = "1552303709:AAHHDq0fxqwgD89k8KB1_q2_sBRF7QL62s8"



def websites(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text("bot kullanılmaya hazır")
    url = requests.get("https://www.webtekno.com/rss.xml")
    if url.status_code == 200:
        soup = BeautifulSoup(url.content, "lxml")
        title = soup.select("channel > item > title")[0]
        url = soup.select("channel > item > guid")[0]
        id_ = soup.select("channel > item > pubDate")[0]
        response = "Webtekno yeni bir haber paylaştı!" + "\n\n" + " " + str(title.text) + "\n\n" + " " + str(url.text)
        temp = None
        veri = title.text

        while True:
            if veri != temp:
                temp = veri
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),data={'chat_id': chat_id, 'text':response}).json()
                print(temp)

def doviz():
    url = requests.get("https://kur.doviz.com/serbest-piyasa")
    if url.status_code == 200:
        response = BeautifulSoup(url.content, "lxml")
        dolar1 = response.select("body > header > div.header-secondary > div > div > div:nth-child(2) > a > span")[0]
        dolar2 = response.select("body > header > div.header-secondary > div > div > div:nth-child(2) > a > span")[1]

        response = BeautifulSoup(url.content, "lxml")
        grm1 = response.select("body > header > div.header-secondary > div > div > div:nth-child(1) > a > span")[0]
        grm2 = response.select("body > header > div.header-secondary > div > div > div:nth-child(1) > a > span")[1]

        response = BeautifulSoup(url.content, "lxml")
        eur1 = response.select("body > header > div.header-secondary > div > div > div:nth-child(3) > a > span")[0]
        eur2 = response.select("body > header > div.header-secondary > div > div > div:nth-child(3) > a > span")[1]

        response = BeautifulSoup(url.content, "lxml")
        strl1 = response.select("body > header > div.header-secondary > div > div > div:nth-child(4) > a > span")[0]
        strl2 = response.select("body > header > div.header-secondary > div > div > div:nth-child(4) > a > span")[1]

        dolarA = str(dolar1.text)
        dolarB = str(dolar2.text)

        EUR = str(eur1.text)
        EUR2 = str(eur2.text)
        GRML = str(grm1.text)
        GRML2 = str(grm2.text)
        STRL = str(strl1.text)
        STRL2 = str(strl2.text)


def idT(update, context):
    print(update.message.chat_id)
if __name__ == '__main__':


    updater = Updater(token=token)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("idN",idT))
    dp.add_handler(CommandHandler("start",websites))

    # <----------------------------------------------------------------------->

    updater.start_polling()
    updater.idle()