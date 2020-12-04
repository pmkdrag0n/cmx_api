from flask import Flask, render_template, request
from requests.auth import HTTPBasicAuth
import requests
import json
#from tabulate import tabulate
requests.packages.urllib3.disable_warnings() #Tắt cảnh báo Warning
list_info = []
app = Flask(__name__,template_folder='Templates')
def get_count():
    server = "https://10.215.26.223"
    api_path = "/api/config/v1/maps/count"
    url = server+api_path
    auth= HTTPBasicAuth('admin','VnPro@123')
    resp = requests.get(url,auth=auth,verify= False)
    data = json.loads(resp.text)
    list_info = [data['totalCampuses'],data['totalBuildings'],data['totalFloors'],data['campusCounts']]
    return list_info
def get_floor():
    server = "https://10.215.26.223"
    api_path = "/api/config/v1/maps/floor/list"
    url = server+api_path
    auth= HTTPBasicAuth('admin','VnPro@123')
    resp = requests.get(url,auth=auth,verify= False)
    data = json.loads(resp.text)
    list_item = []
    for item in data:
         list_item.append(item.split('>'))
    return list_item
    
def get_client():
    server = "https://10.215.26.223"
    api_path = "/api/analytics/v1/now/clientCount"
    url = server+api_path
    auth= HTTPBasicAuth('admin','VnPro@123')
    list_client = []
    resp = requests.get(url,auth=auth,verify= False)
    data = json.loads(resp.text)
    for item in data['data']:
        list_client.append([item['floorName'],item['value']])
    return list_client
def get_info():
    server = "https://10.215.26.223"
    api_path = "/api/location/v1/history/clients"
    url = server+api_path
    auth= HTTPBasicAuth('admin','VnPro@123')
    resp = requests.get(url,auth=auth,verify= False)
    data = json.loads(resp.text)
    for item in data:
        if item['ipAddress'] == []:
            pass
        else:
            info = [
            item['macAddress'],
            item['mapInfo']['mapHierarchyDetails']["campus"],
            item['mapInfo']['mapHierarchyDetails']["building"],
            item['mapInfo']['mapHierarchyDetails']["floor"],
            item['statistics']['currentServerTime'],
            item['mapCoordinate']['x'],
            item['mapCoordinate']['y'],
            item['mapCoordinate']['z'],
            item['ipAddress'][0]] 
            list_info.append(info)
    return list_info

@app.route('/', methods=['GET'])
def index():
   data = get_info()
   return render_template('index.html',data = data)
@app.route('/client', methods=['GET'])
def floor():
   data = get_client()
   return render_template('client.html',data=data)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
    #get_floor()