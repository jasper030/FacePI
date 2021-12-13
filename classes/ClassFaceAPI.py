import urllib, http
import classes.ClassConfig

class Face:
    def __init__(self) -> None:
        self.config = classes.ClassConfig.Config
        

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
