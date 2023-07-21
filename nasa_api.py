from datetime import datetime, timedelta
import requests
import json
from googletrans import Translator

def main():
    translator = Translator()
    api_key = "API_KEY"
    start_date = datetime.today()
    end_date = datetime.date(start_date - timedelta(days=1))
    start_date = datetime.date(start_date)
    str_query = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    response = requests.get(str_query)
    if response.status_code == 200:
        stroke_s = json.loads(response.text)['near_earth_objects']#['2023-07-20']
        print(f"Астероиды, которые в период с {end_date} по {start_date} будут сближаться с планетой Земля, по данным NASA")
        for j in stroke_s:
            stroke_a = stroke_s[j]
            print(f'\nАстроиды на дату {j}:\n')
            for i in range(len(stroke_a)):
                name_a = stroke_a[i]['name']
                id_a  = stroke_a[i]['id']
                orbitig = stroke_a[i]['close_approach_data']
                dangers = stroke_a[i]['is_potentially_hazardous_asteroid']
                dataNasa = stroke_a[i]['nasa_jpl_url']
                if dangers:
                    dangers = "Да"
                else:
                    dangers = "Нет"

                if len(orbitig) == 1:
                    orbitig_a = orbitig[0]['orbiting_body']
                    orbitig_a = translator.translate(orbitig_a, src='en', dest='ru')
                else:
                    orbitig_a = 'None'
                print(f'\n*ID астероида: {id_a}:\n -Имя астероида: {name_a}\n -Орбитальное тело: {orbitig_a.text}\n -Потеницально опасный объект: {dangers}\n -Больше данных о данном космическом объекте на сайте NASA: {dataNasa}')
                i=i+1
    else:
        print("No connection...")

