import time
import requests
from requests.exceptions import HTTPError


# incognito Chrome window used
class ShopApi:

    def get_products_ids(self):
        cookies = {
            '_gcl_au': '1.1.885258334.1661948120',
            'tmr_lvid': '5c47c77f02c11c6de25c61d74e956aa5',
            'tmr_lvidTS': '1661948120680',
            '_ga': 'GA1.2.2074629334.1661948121',
            '_gid': 'GA1.2.787654786.1661948121',
            'ab_experiments_entity_id': '1xPaxLwkTayA_YoKK_hM-A',
            'ab_experiments_list': 'acs-googlepay-ecosys-1075-3%3Atest%3Bdc-pro-v2%3Atest%3Bdcpro-137%3Acontrol%3Becosys-1493-web%3Atest%3Becosys-1497-web%3Acontrol%3Becosys-1851%3Atest%3Becosys-399%3Atest%3Becosysweb-1550%3Acontrol%3Bft-surge-rct-1257%3Atest%3Bopt-1760%3Aoff%3Boptbpm-879%3Alast%3Boptdcapi-777%3Aoff%3Boptpoints-1885%3Aoff%3Boptpromo-1734%3Aoff%3Boptun-1897%3Alast%3Bpot-39%3Aenabled%3Bpot-646%3Adisabled%3Bpot-717%3Aenabled%3Bsberid-auth-ecosys-1122%3Atest%3Bservice-fee-grocery-experiment-i-v13%3Atest39od%3Bta-coffee-filter-ta-1191%3Acontrol%3Bta-mcds-discount-text%3Anone%3Bta-ui-service-proxy%3Acontrol%3Bta-ui-service-proxy-v2%3Acontrol',
            'mr1lad': '630f50d8503e1569-0-0-',
            'mr1luid': '',
            'mr1lext': '',
            'visit_from_yandex_cpc': '0',
            'split_test_version': 'version_b',
            'PHPSESSID': '0e6ecf5e9b41c25c8a3f11dd1ec5ccf12ae038ec',
            'x_user_authorization': 'eyJ0b2tlbiI6IjBlNmVjZjVlOWI0MWMyNWM4YTNmMTFkZDFlYzVjY2YxMmFlMDM4ZWMiLCJzZWNyZXQiOiJiYWNlYTgyYTZkMGU5MjYzOTkyYTg4ZTdmNDVlMzcxN2FhMWI4MGJmIiwicGxhdGZvcm0iOiJtYXJrZXQiLCJ1c2VySUQiOjAsImRldmljZUlEIjoiMjY0N2JjMjktNzdkYi00ZmUwLWI0ODItZDZiNzQ1MzZkYWNiIiwiaW5zdGFsbElEIjoiMjI4YzliMGU1ZjVjYTM0ODcxOTFiNDgxNzU5NjA0NTdmNmFlYWJlZiIsImV4cCI6MTY2MTk0OTAyMn0.I4LqGKc1oLulyWU7Vpj_r5krmcIl8cTeE56T1jZYqcE',
            'client_address': '%7B%22cityId%22%3A1%2C%22host%22%3A%22moscow%22%2C%22latitude%22%3A55.7577374%2C%22longitude%22%3A37.6164793%2C%22timeOffset%22%3A0%7D',
            'selected_address': '%7B%22accuracy%22%3A%22preciseCoordinates%22%2C%22cityId%22%3A53%2C%22details%22%3A%5B%7B%22alias%22%3A%22Country%22%2C%22name%22%3A%22%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%22%2C%22type%22%3A%22country%22%7D%2C%7B%22alias%22%3A%22AdministrativeArea%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22type%22%3A%22administrativeArea%22%7D%2C%7B%22alias%22%3A%22SubAdministrativeArea%22%2C%22name%22%3A%22%D0%BC%D1%83%D0%BD%D0%B8%D1%86%D0%B8%D0%BF%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22subAdministrativeArea%22%7D%2C%7B%22alias%22%3A%22Locality%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22locality%22%7D%2C%7B%22alias%22%3A%22Thoroughfare%22%2C%22name%22%3A%22%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%22%2C%22type%22%3A%22street%22%7D%2C%7B%22alias%22%3A%22Premise%22%2C%22name%22%3A%2233%22%2C%22type%22%3A%22house%22%7D%5D%2C%22host%22%3A%22kirov%22%2C%22latitude%22%3A58.592735%2C%22longitude%22%3A49.650191%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%2C%2033%22%2C%22timeOffset%22%3A%220%22%7D',
            'tmr_reqNum': '3',
            '_gat_UA-9598444-6': '1',
            '_ga_H7GWMF5P1N': 'GS1.1.1661948120.1.1.1661948441.60.0.0',
            'amplitude_id_692a3723a9dfa13093b43c500d5c5074delivery-club.ru': 'eyJkZXZpY2VJZCI6IjYxODU2NjQ2LTZlYWQtNDg5ZS1hNzRhLTNkYjZkNTg1YjA5M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY2MTk0ODEyMDk2OCwibGFzdEV2ZW50VGltZSI6MTY2MTk0ODQ0ODMwMCwiZXZlbnRJZCI6NiwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjh9',
        }

        headers = {
            'authority': 'api.delivery-club.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_gcl_au=1.1.885258334.1661948120; tmr_lvid=5c47c77f02c11c6de25c61d74e956aa5; tmr_lvidTS=1661948120680; _ga=GA1.2.2074629334.1661948121; _gid=GA1.2.787654786.1661948121; ab_experiments_entity_id=1xPaxLwkTayA_YoKK_hM-A; ab_experiments_list=acs-googlepay-ecosys-1075-3%3Atest%3Bdc-pro-v2%3Atest%3Bdcpro-137%3Acontrol%3Becosys-1493-web%3Atest%3Becosys-1497-web%3Acontrol%3Becosys-1851%3Atest%3Becosys-399%3Atest%3Becosysweb-1550%3Acontrol%3Bft-surge-rct-1257%3Atest%3Bopt-1760%3Aoff%3Boptbpm-879%3Alast%3Boptdcapi-777%3Aoff%3Boptpoints-1885%3Aoff%3Boptpromo-1734%3Aoff%3Boptun-1897%3Alast%3Bpot-39%3Aenabled%3Bpot-646%3Adisabled%3Bpot-717%3Aenabled%3Bsberid-auth-ecosys-1122%3Atest%3Bservice-fee-grocery-experiment-i-v13%3Atest39od%3Bta-coffee-filter-ta-1191%3Acontrol%3Bta-mcds-discount-text%3Anone%3Bta-ui-service-proxy%3Acontrol%3Bta-ui-service-proxy-v2%3Acontrol; mr1lad=630f50d8503e1569-0-0-; mr1luid=; mr1lext=; visit_from_yandex_cpc=0; split_test_version=version_b; PHPSESSID=0e6ecf5e9b41c25c8a3f11dd1ec5ccf12ae038ec; x_user_authorization=eyJ0b2tlbiI6IjBlNmVjZjVlOWI0MWMyNWM4YTNmMTFkZDFlYzVjY2YxMmFlMDM4ZWMiLCJzZWNyZXQiOiJiYWNlYTgyYTZkMGU5MjYzOTkyYTg4ZTdmNDVlMzcxN2FhMWI4MGJmIiwicGxhdGZvcm0iOiJtYXJrZXQiLCJ1c2VySUQiOjAsImRldmljZUlEIjoiMjY0N2JjMjktNzdkYi00ZmUwLWI0ODItZDZiNzQ1MzZkYWNiIiwiaW5zdGFsbElEIjoiMjI4YzliMGU1ZjVjYTM0ODcxOTFiNDgxNzU5NjA0NTdmNmFlYWJlZiIsImV4cCI6MTY2MTk0OTAyMn0.I4LqGKc1oLulyWU7Vpj_r5krmcIl8cTeE56T1jZYqcE; client_address=%7B%22cityId%22%3A1%2C%22host%22%3A%22moscow%22%2C%22latitude%22%3A55.7577374%2C%22longitude%22%3A37.6164793%2C%22timeOffset%22%3A0%7D; selected_address=%7B%22accuracy%22%3A%22preciseCoordinates%22%2C%22cityId%22%3A53%2C%22details%22%3A%5B%7B%22alias%22%3A%22Country%22%2C%22name%22%3A%22%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%22%2C%22type%22%3A%22country%22%7D%2C%7B%22alias%22%3A%22AdministrativeArea%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22type%22%3A%22administrativeArea%22%7D%2C%7B%22alias%22%3A%22SubAdministrativeArea%22%2C%22name%22%3A%22%D0%BC%D1%83%D0%BD%D0%B8%D1%86%D0%B8%D0%BF%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22subAdministrativeArea%22%7D%2C%7B%22alias%22%3A%22Locality%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22locality%22%7D%2C%7B%22alias%22%3A%22Thoroughfare%22%2C%22name%22%3A%22%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%22%2C%22type%22%3A%22street%22%7D%2C%7B%22alias%22%3A%22Premise%22%2C%22name%22%3A%2233%22%2C%22type%22%3A%22house%22%7D%5D%2C%22host%22%3A%22kirov%22%2C%22latitude%22%3A58.592735%2C%22longitude%22%3A49.650191%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%2C%2033%22%2C%22timeOffset%22%3A%220%22%7D; tmr_reqNum=3; _gat_UA-9598444-6=1; _ga_H7GWMF5P1N=GS1.1.1661948120.1.1.1661948441.60.0.0; amplitude_id_692a3723a9dfa13093b43c500d5c5074delivery-club.ru=eyJkZXZpY2VJZCI6IjYxODU2NjQ2LTZlYWQtNDg5ZS1hNzRhLTNkYjZkNTg1YjA5M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY2MTk0ODEyMDk2OCwibGFzdEV2ZW50VGltZSI6MTY2MTk0ODQ0ODMwMCwiZXZlbnRJZCI6NiwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjh9',
            'origin': 'https://www.delivery-club.ru',
            'referer': 'https://www.delivery-club.ru/store/samokat_produkty_kirov_vd',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-entity-id': '1xPaxLwkTayA_YoKK_hM-A',
            'x-user-authorization': 'eyJ0b2tlbiI6IjBlNmVjZjVlOWI0MWMyNWM4YTNmMTFkZDFlYzVjY2YxMmFlMDM4ZWMiLCJzZWNyZXQiOiJiYWNlYTgyYTZkMGU5MjYzOTkyYTg4ZTdmNDVlMzcxN2FhMWI4MGJmIiwicGxhdGZvcm0iOiJtYXJrZXQiLCJ1c2VySUQiOjAsImRldmljZUlEIjoiMjY0N2JjMjktNzdkYi00ZmUwLWI0ODItZDZiNzQ1MzZkYWNiIiwiaW5zdGFsbElEIjoiMjI4YzliMGU1ZjVjYTM0ODcxOTFiNDgxNzU5NjA0NTdmNmFlYWJlZiIsImV4cCI6MTY2MTk0OTAyMn0.I4LqGKc1oLulyWU7Vpj_r5krmcIl8cTeE56T1jZYqcE',
        }

        json_data = {
            'categoriesId': [],
        }

        try:
            response = requests.post('https://api.delivery-club.ru/api1.2/grocery/stores/150811/catalog/discount',
                                     cookies=cookies, headers=headers, json=json_data, timeout=10)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return print('failed to get_products_ids')
        except Exception as err:
            print(f'Other error occurred: {err}')
            return print('failed to get_products_ids')
        else:
            return response.json()['products']



    def get_products_quantity(self, json_data):
        cookies = {
            '_gcl_au': '1.1.885258334.1661948120',
            'tmr_lvid': '5c47c77f02c11c6de25c61d74e956aa5',
            'tmr_lvidTS': '1661948120680',
            '_ga': 'GA1.2.2074629334.1661948121',
            '_gid': 'GA1.2.787654786.1661948121',
            'ab_experiments_entity_id': '1xPaxLwkTayA_YoKK_hM-A',
            'ab_experiments_list': 'acs-googlepay-ecosys-1075-3%3Atest%3Bdc-pro-v2%3Atest%3Bdcpro-137%3Acontrol%3Becosys-1493-web%3Atest%3Becosys-1497-web%3Acontrol%3Becosys-1851%3Atest%3Becosys-399%3Atest%3Becosysweb-1550%3Acontrol%3Bft-surge-rct-1257%3Atest%3Bopt-1760%3Aoff%3Boptbpm-879%3Alast%3Boptdcapi-777%3Aoff%3Boptpoints-1885%3Aoff%3Boptpromo-1734%3Aoff%3Boptun-1897%3Alast%3Bpot-39%3Aenabled%3Bpot-646%3Adisabled%3Bpot-717%3Aenabled%3Bsberid-auth-ecosys-1122%3Atest%3Bservice-fee-grocery-experiment-i-v13%3Atest39od%3Bta-coffee-filter-ta-1191%3Acontrol%3Bta-mcds-discount-text%3Anone%3Bta-ui-service-proxy%3Acontrol%3Bta-ui-service-proxy-v2%3Acontrol',
            'mr1lad': '630f50d8503e1569-0-0-',
            'mr1luid': '',
            'mr1lext': '',
            'visit_from_yandex_cpc': '0',
            'split_test_version': 'version_b',
            'PHPSESSID': '0e6ecf5e9b41c25c8a3f11dd1ec5ccf12ae038ec',
            'x_user_authorization': 'eyJ0b2tlbiI6IjBlNmVjZjVlOWI0MWMyNWM4YTNmMTFkZDFlYzVjY2YxMmFlMDM4ZWMiLCJzZWNyZXQiOiJiYWNlYTgyYTZkMGU5MjYzOTkyYTg4ZTdmNDVlMzcxN2FhMWI4MGJmIiwicGxhdGZvcm0iOiJtYXJrZXQiLCJ1c2VySUQiOjAsImRldmljZUlEIjoiMjY0N2JjMjktNzdkYi00ZmUwLWI0ODItZDZiNzQ1MzZkYWNiIiwiaW5zdGFsbElEIjoiMjI4YzliMGU1ZjVjYTM0ODcxOTFiNDgxNzU5NjA0NTdmNmFlYWJlZiIsImV4cCI6MTY2MTk0OTAyMn0.I4LqGKc1oLulyWU7Vpj_r5krmcIl8cTeE56T1jZYqcE',
            'client_address': '%7B%22cityId%22%3A1%2C%22host%22%3A%22moscow%22%2C%22latitude%22%3A55.7577374%2C%22longitude%22%3A37.6164793%2C%22timeOffset%22%3A0%7D',
            'selected_address': '%7B%22accuracy%22%3A%22preciseCoordinates%22%2C%22cityId%22%3A53%2C%22details%22%3A%5B%7B%22alias%22%3A%22Country%22%2C%22name%22%3A%22%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%22%2C%22type%22%3A%22country%22%7D%2C%7B%22alias%22%3A%22AdministrativeArea%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22type%22%3A%22administrativeArea%22%7D%2C%7B%22alias%22%3A%22SubAdministrativeArea%22%2C%22name%22%3A%22%D0%BC%D1%83%D0%BD%D0%B8%D1%86%D0%B8%D0%BF%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22subAdministrativeArea%22%7D%2C%7B%22alias%22%3A%22Locality%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22locality%22%7D%2C%7B%22alias%22%3A%22Thoroughfare%22%2C%22name%22%3A%22%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%22%2C%22type%22%3A%22street%22%7D%2C%7B%22alias%22%3A%22Premise%22%2C%22name%22%3A%2233%22%2C%22type%22%3A%22house%22%7D%5D%2C%22host%22%3A%22kirov%22%2C%22latitude%22%3A58.592735%2C%22longitude%22%3A49.650191%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%2C%2033%22%2C%22timeOffset%22%3A%220%22%7D',
            'tmr_reqNum': '3',
            '_gat_UA-9598444-6': '1',
            '_ga_H7GWMF5P1N': 'GS1.1.1661948120.1.1.1661948441.60.0.0',
            'amplitude_id_692a3723a9dfa13093b43c500d5c5074delivery-club.ru': 'eyJkZXZpY2VJZCI6IjYxODU2NjQ2LTZlYWQtNDg5ZS1hNzRhLTNkYjZkNTg1YjA5M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY2MTk0ODEyMDk2OCwibGFzdEV2ZW50VGltZSI6MTY2MTk0ODQ0ODMwMCwiZXZlbnRJZCI6NiwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjh9',
        }

        headers = {
            'authority': 'api.delivery-club.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_gcl_au=1.1.885258334.1661948120; tmr_lvid=5c47c77f02c11c6de25c61d74e956aa5; tmr_lvidTS=1661948120680; _ga=GA1.2.2074629334.1661948121; _gid=GA1.2.787654786.1661948121; ab_experiments_entity_id=1xPaxLwkTayA_YoKK_hM-A; ab_experiments_list=acs-googlepay-ecosys-1075-3%3Atest%3Bdc-pro-v2%3Atest%3Bdcpro-137%3Acontrol%3Becosys-1493-web%3Atest%3Becosys-1497-web%3Acontrol%3Becosys-1851%3Atest%3Becosys-399%3Atest%3Becosysweb-1550%3Acontrol%3Bft-surge-rct-1257%3Atest%3Bopt-1760%3Aoff%3Boptbpm-879%3Alast%3Boptdcapi-777%3Aoff%3Boptpoints-1885%3Aoff%3Boptpromo-1734%3Aoff%3Boptun-1897%3Alast%3Bpot-39%3Aenabled%3Bpot-646%3Adisabled%3Bpot-717%3Aenabled%3Bsberid-auth-ecosys-1122%3Atest%3Bservice-fee-grocery-experiment-i-v13%3Atest39od%3Bta-coffee-filter-ta-1191%3Acontrol%3Bta-mcds-discount-text%3Anone%3Bta-ui-service-proxy%3Acontrol%3Bta-ui-service-proxy-v2%3Acontrol; mr1lad=630f50d8503e1569-0-0-; mr1luid=; mr1lext=; visit_from_yandex_cpc=0; split_test_version=version_b; PHPSESSID=0e6ecf5e9b41c25c8a3f11dd1ec5ccf12ae038ec; x_user_authorization=eyJ0b2tlbiI6IjBlNmVjZjVlOWI0MWMyNWM4YTNmMTFkZDFlYzVjY2YxMmFlMDM4ZWMiLCJzZWNyZXQiOiJiYWNlYTgyYTZkMGU5MjYzOTkyYTg4ZTdmNDVlMzcxN2FhMWI4MGJmIiwicGxhdGZvcm0iOiJtYXJrZXQiLCJ1c2VySUQiOjAsImRldmljZUlEIjoiMjY0N2JjMjktNzdkYi00ZmUwLWI0ODItZDZiNzQ1MzZkYWNiIiwiaW5zdGFsbElEIjoiMjI4YzliMGU1ZjVjYTM0ODcxOTFiNDgxNzU5NjA0NTdmNmFlYWJlZiIsImV4cCI6MTY2MTk0OTAyMn0.I4LqGKc1oLulyWU7Vpj_r5krmcIl8cTeE56T1jZYqcE; client_address=%7B%22cityId%22%3A1%2C%22host%22%3A%22moscow%22%2C%22latitude%22%3A55.7577374%2C%22longitude%22%3A37.6164793%2C%22timeOffset%22%3A0%7D; selected_address=%7B%22accuracy%22%3A%22preciseCoordinates%22%2C%22cityId%22%3A53%2C%22details%22%3A%5B%7B%22alias%22%3A%22Country%22%2C%22name%22%3A%22%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%22%2C%22type%22%3A%22country%22%7D%2C%7B%22alias%22%3A%22AdministrativeArea%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22type%22%3A%22administrativeArea%22%7D%2C%7B%22alias%22%3A%22SubAdministrativeArea%22%2C%22name%22%3A%22%D0%BC%D1%83%D0%BD%D0%B8%D1%86%D0%B8%D0%BF%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22subAdministrativeArea%22%7D%2C%7B%22alias%22%3A%22Locality%22%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%22%2C%22type%22%3A%22locality%22%7D%2C%7B%22alias%22%3A%22Thoroughfare%22%2C%22name%22%3A%22%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%22%2C%22type%22%3A%22street%22%7D%2C%7B%22alias%22%3A%22Premise%22%2C%22name%22%3A%2233%22%2C%22type%22%3A%22house%22%7D%5D%2C%22host%22%3A%22kirov%22%2C%22latitude%22%3A58.592735%2C%22longitude%22%3A49.650191%2C%22name%22%3A%22%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%2C%2033%22%2C%22timeOffset%22%3A%220%22%7D; tmr_reqNum=3; _gat_UA-9598444-6=1; _ga_H7GWMF5P1N=GS1.1.1661948120.1.1.1661948441.60.0.0; amplitude_id_692a3723a9dfa13093b43c500d5c5074delivery-club.ru=eyJkZXZpY2VJZCI6IjYxODU2NjQ2LTZlYWQtNDg5ZS1hNzRhLTNkYjZkNTg1YjA5M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY2MTk0ODEyMDk2OCwibGFzdEV2ZW50VGltZSI6MTY2MTk0ODQ0ODMwMCwiZXZlbnRJZCI6NiwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjh9',
            'origin': 'https://www.delivery-club.ru',
            'referer': 'https://www.delivery-club.ru/store/samokat_produkty_kirov_vd',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-entity-id': '1xPaxLwkTayA_YoKK_hM-A',
            'x-user-authorization': 'eyJ0b2tlbiI6IjBlNmVjZjVlOWI0MWMyNWM4YTNmMTFkZDFlYzVjY2YxMmFlMDM4ZWMiLCJzZWNyZXQiOiJiYWNlYTgyYTZkMGU5MjYzOTkyYTg4ZTdmNDVlMzcxN2FhMWI4MGJmIiwicGxhdGZvcm0iOiJtYXJrZXQiLCJ1c2VySUQiOjAsImRldmljZUlEIjoiMjY0N2JjMjktNzdkYi00ZmUwLWI0ODItZDZiNzQ1MzZkYWNiIiwiaW5zdGFsbElEIjoiMjI4YzliMGU1ZjVjYTM0ODcxOTFiNDgxNzU5NjA0NTdmNmFlYWJlZiIsImV4cCI6MTY2MTk0OTAyMn0.I4LqGKc1oLulyWU7Vpj_r5krmcIl8cTeE56T1jZYqcE',
        }

        try:
            response = requests.post('https://api.delivery-club.ru/api1.2/grocery/stores/150811/products',
                                     cookies=cookies, headers=headers, json=json_data, timeout=10)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return print('failed to get_products_info')
        except Exception as err:
            print(f'Other error occurred: {err}')
            return print('failed to get_products_info')
        else:
            return response.json()['products']

