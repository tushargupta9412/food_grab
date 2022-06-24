import json

import requests

from constants import REQUEST_PARAMS, WEB_URL, REQUEST_PROXY
import pandas as pd


class LocationFinder:
    def __init__(self):
        self.web_url = WEB_URL
        self.request_params = REQUEST_PARAMS

    def fetchData(self):
        try:
            request = requests.get(url=self.web_url, params=self.request_params, proxies=REQUEST_PROXY)
            return request.content
        except Exception as ex:
            print(ex)
            return None

    def dumpData(self):
        data = self.fetchData()
        final_list = []
        if data is not None:
            json_data = json.loads(data)
            for entry in json_data['places']:
                store_name = entry['name']
                longitude = entry["location"]['longitude']
                latitude = entry["location"]['latitude']
                restaurant_data = [store_name, longitude, latitude]
                final_list.append(restaurant_data)
            return final_list
        else:
            return None

    def createSheet(self):
        restaurants = self.dumpData()
        if restaurants is not None:
            df = pd.DataFrame(restaurants)
            writer = pd.ExcelWriter('restaurants_location.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name='data', index=False)
            writer.save()
        else:
            print("Error while fetching... data")


location_finder = LocationFinder()
print(location_finder.createSheet())
