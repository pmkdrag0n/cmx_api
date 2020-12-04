from requests.auth import HTTPBasicAuth
import requests
import json
#from tabulate import tabulate
requests.packages.urllib3.disable_warnings() #Tắt cảnh báo Warning
list_info = []
def get_info():
    server = "https://10.215.26.223"
    api_path = "/api/location/v1/history/clients"
    url = server+api_path
    auth= HTTPBasicAuth('admin','VnPro@123')
    resp = requests.get(url,auth=auth,verify= False)
    data = json.loads(resp.text)
    for item in data:
        #if item['ipAddress'] == []:
            #pass
        #else:
            info = [
            item['macAddress'],
            item['mapInfo']['mapHierarchyDetails']["campus"],
            item['mapInfo']['mapHierarchyDetails']["building"],
            item['mapInfo']['mapHierarchyDetails']["floor"],
            item['statistics']['currentServerTime'],
            item['mapCoordinate']['x'],
            item['mapCoordinate']['y'],
            item['mapCoordinate']['z'],
            item['ipAddress']] 
            list_info.append(info)
            '''
            info = {
            'macAddr' : item['macAddress'],
            'campus': item['mapInfo']['mapHierarchyDetails']["campus"],
            'building' : item['mapInfo']['mapHierarchyDetails']["building"],
            'floor' : item['mapInfo']['mapHierarchyDetails']["floor"],
            'time' : item['statistics']['currentServerTime'],
            'x' : item['mapCoordinate']['x'],
            'y' : item['mapCoordinate']['y'],
            'z' :item['mapCoordinate']['z'],
            'ip' : item['ipAddress']
            }
            '''
    #print(list_info)
    return list_info
if __name__ == "__main__":
    get_info()