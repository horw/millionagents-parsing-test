from request.detmir_request import DetmirCategoryRequest
import csv
"""1. ID товара
2. Наименование 
3. Цена
4. Город
5. Промо цена (если имеется) - не нашел
6. Ссылка на страницу с товаром"""


def get_items_info(region: str):
    for items in DetmirCategoryRequest(region):
        for item in items:
            yield [
                item['id'],
                item['title'],
                f'{item["price"]["price"]} {item["price"]["currency"]}',
                region,
                item['link']['web_url']
            ]


if __name__ == "__main__":

    out_list = [['ID', 'Title', 'Price', 'Region', 'Link']]
    print('Prepare Moscow data')
    out_list.extend(list(get_items_info('MOW')))
    print('Prepare SPB data')
    out_list.extend(list(get_items_info('SPE')))
    #print(out_list)
    print('Write data in csv')
    with open('items.csv', 'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(out_list)