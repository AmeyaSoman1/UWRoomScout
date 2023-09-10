import requests
import datetime
import time
import json

url = "https://portalapi2.uwaterloo.ca/v2/map/OpenClassrooms"

response = requests.get(url)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

today = datetime.date.today()
weekday_name = today.strftime('%A')
print(weekday_name)

if response.status_code == 200:

    featureIndex = 0
    dataIndex = 0
    scheduleIndex = 0
    slotIndex = 0
    
    data = response.json()

    while (featureIndex < len(data['data']['features'])):
        
        slots = json.loads(data['data']['features'][featureIndex]['properties']['openClassroomSlots'])
    
        while (dataIndex < len(slots['data'])):
            print ("--------------------------")
            ###print(slots['data'][dataIndex]['buildingCode'])
            ###print(slots['data'][dataIndex]['roomNumber'])

            scheduleIndex = 0

            while (scheduleIndex < len(slots['data'][dataIndex]['Schedule'])):
                ###print(slots['data'][dataIndex]['Schedule'][scheduleIndex]['Weekday'])
                #print("scheduleIndex: ", scheduleIndex)
                #print("dataIndex: ", dataIndex)
                
                if (slots['data'][dataIndex]['Schedule'][scheduleIndex]['Slots'] == []):
                    print("Empty Array")
                    print("")
                else:
                    #print("Non Empty Array")
                    slotIndex = 0
                    while (slotIndex < len(slots['data'][dataIndex]['Schedule'][scheduleIndex]['Slots'])):
                        ###print(slots['data'][dataIndex]['Schedule'][scheduleIndex]['Slots'][slotIndex]['StartTime'])
                        ###print(slots['data'][dataIndex]['Schedule'][scheduleIndex]['Slots'][slotIndex]['EndTime'])
                        ###print("")

                        if (slots['data'][dataIndex]['Schedule'][scheduleIndex]['Slots'][slotIndex]['StartTime'] <= current_time <= slots['data'][dataIndex]['Schedule'][scheduleIndex]['Slots'][slotIndex]['StartTime']) and (weekday_name == (slots['data'][dataIndex]['Schedule'][scheduleIndex]['Weekday'])):
                            print(slots['data'][dataIndex]['buildingCode'])
                            print(slots['data'][dataIndex]['roomNumber'])

                        else:
                            print()

                        slotIndex += 1

                #print("Incrementing scheduleIndex")
                scheduleIndex += 1

            dataIndex += 1
        
        featureIndex += 1