import requests
import csv

def get_warehouses(domen):
    """Получение данных о складах и сохранение их в CSV файл."""
    url = f'https://{domen}/vol0/data/stores-data.json'
    headers = {
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'Referer': 'https://www.wildberries.ru/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем наличие ошибок
        data = response.json()

        # Открываем файл для записи данных
        with open('warehouses.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Название'])

            # Проверяем структуру данных
            if isinstance(data, list):  # Убедитесь, что это список
                for warehouse in data:
                    warehouse_id = warehouse.get('id')
                    warehouse_name = warehouse.get('name')

                    # Проверка, начинается или заканчивается ли название на "WB"
                    if warehouse_name and (warehouse_name.startswith('WB') or warehouse_name.endswith('WB')):
                        print(f'ID: {warehouse_id}, Название: {warehouse_name}')
                        
                        # Записываем данные в файл
                        writer.writerow([warehouse_id, warehouse_name])
            else:
                print("[ERROR] Неверный формат данных")

    except requests.exceptions.HTTPError as http_err:
        print(f'[ERROR] Ошибка HTTP: {http_err}')
    except Exception as err:
        print(f'[ERROR] Ошибка: {err}')

def main(domen):
    get_warehouses(domen)

if __name__ == '__main__':
    main('static-basket-01.wbbasket.ru')
