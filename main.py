import json, fire, http.client, urllib.request, urllib.parse, urllib.error, base64



class FacePI:

  def readConfig(self):
    with open("Config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

  def writeConfig(self, config):
    with open("Config.json", "w", encoding="utf-8") as f:
      json.dump(config, f)

  def setConfig(self):
    config = self.readConfig()
    print("The '[]' after th value is the default value, press ENTER if you don't want to modify it.")
    api_key = input(f'Please enter the API_KEY, current -> [{config["api_key"]}]: ')
    if api_key: config["api_key"] = api_key
    title = input(f'Please enter the TITLE[{config["title"]}]: ')
    if title: config["title"] = title
    self.writeConfig(config)
    
  def showConfig(self):
    print(self.readConfig())

  def detectFaceUrl(self, imagepath):
  
    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key':  self.readConfig()['api_key'],
    }

    params = urllib.parse.urlencode({
      # Request parameters
      'returnFaceId': 'true',
      'returnFaceLandmarks': 'false',
      'returnFaceAttributes': 'age, gender',  #{string} -> age, gender
      'recognitionModel': 'recognition_04',
      'returnRecognitionModel': 'false',
      'detectionModel': 'detection_01',
      'faceIdTimeToLive': '86400',
    })

    print('imagepath =', imagepath)
    requestbody =  '{"url": "' + imagepath + '"}'
    #open(imagepath, "rb").read()

    try:
      conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
      conn.request("POST", "/face/v1.0/detect?%s" % params, requestbody, headers)  
      response = conn.getresponse()
      data = response.read()
      print(data)
      conn.close()
    except Exception as e:
      print("[Errno {0}] 連線失敗！請檢查網路連線 {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    fire.Fire(FacePI)
