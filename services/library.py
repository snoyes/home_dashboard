import requests
import json
from datetime import datetime, date
from lxml import html

def update():
    today = date.today()
    with open('.library_cards.json') as f:
        cards = json.load(f)
    data = []
    for card in cards:
        if (result := requests.get(card['url'], headers=card['headers'], cookies=card['cookies'])):
            tree = html.fromstring(result.content)
            items_out = [{"title": div[1].text_content(), "due_date": div[2].text_content()} for div in tree.xpath('//ul[@id="body"]/li')]
            data.append({
                    "card_name": card['card_name'],
                    "checked_out_count": len(items_out),
                    "overdue_count": sum(datetime.strptime(item['due_date'], '%m/%d/%Y').date() < today for item in items_out),
                    "items_out": items_out
                    })

    with open('cache/.library', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update()
