import urllib, http
import classes.ClassConfig

class Face:
    def __init__(self) -> None:
        self.config = classes.ClassConfig.Config().readConfig()

    
    def detectLocalImage(self, imagepath):
        headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',  # 用本地圖檔辨識
            'Ocp-Apim-Subscription-Key': self.config['api_key'],
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender',
            #'recognitionModel': 'recognition_04',
            'returnRecognitionModel': 'false',
            'detectionModel': 'detection_01',
            'faceIdTimeToLive': '86400',
        })
        #'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure'
        print('imagepath=', imagepath)
        requestbody = open(imagepath, "rb").read()
        try:
            conn = http.client.HTTPSConnection(self.config['host'])
            conn.request("POST", "/face/v1.0/detect?%s" % params, requestbody,
                         headers)
            response = conn.getresponse()
            data = response.read()
            json_face_detect = json.loads(str(data, 'UTF-8'))
            print("detectLocalImage.faces=", json_face_detect)
            #print(parsed[0]['faceId'])
            #faceids.append(parsed[0]['faceId'])
            conn.close()

            print("detectLocalImage:",
                f"{imagepath} 偵測到 {len(json_face_detect)} 個人")

            return json_face_detect
            
        except Exception as e:
            print("[Errno {0}]連線失敗！請檢查網路設定。 {1}".format(e.errno, e.strerror))
            #return []
        

    def detectFaceUrl(self, imagepath):
  
        headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key':  self.config.readConfig()['api_key'],
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
