import json, fire, time, os
import http.client, urllib.request, urllib.parse, urllib.error, base64
#cognitive document >> https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236.
#handouts >> https://github.com/jiangsir/TestFacePI
import classes.ClassConfig, classes.ClassFaceAPI, classes.ClassOpenCV, classes.ClassPerson, classes.ClassPersonGroup

class FacePI:

  def show_opencv(self):
    classes.ClassOpenCV.show_opencv('hint')
  
  def Identify(self, pictureurl): 
      """14: 進行「辨識」，使用 image URL or 檔案路徑"""
      start = int(round(time.time() * 1000))
      print("開始計時 identify")
      faceApi = classes.ClassFaceAPI.Face()
      personApi = classes.ClassPerson.Person()
      print("載入 class", int(round(time.time() * 1000) - start), "ms")
      # imageurl = input('請輸入準備要辨識的 image URL or 檔案路徑:')
      if pictureurl.startswith("http"):
        detectfaces = faceApi.detectURLImages(pictureurl)
      else:
        pictureurl = pictureurl.strip()
        detectfaces = faceApi.detectLocalImage(pictureurl)

      faceids = []
      for detectface in detectfaces:
        print("所偵測到的 faceId=", detectface["faceId"])
        faceids.append(detectface["faceId"])

      print("Identify.detectfaces=", detectfaces)

      identifiedfaces = faceApi.identify(faceids[:10], config["personGroupId"])

      print("在所提供的相片中偵測到 identifyfaces 共 ", len(identifiedfaces), "個")

      # successes = []
      for identifiedface in identifiedfaces:
        for candidate in identifiedface["candidates"]:
            personId = candidate["personId"]
            person = personApi.get_a_person(personId, config["personGroupId"])
            identifiedface["person"] = person
            identifiedface["confidence"] = candidate["confidence"]
            identifiedface["personId"] = candidate["personId"]

      ### cv_Identifyfaces() 精簡版
      for identifyface in identifiedfaces:
        if "person" not in identifyface:
            print("identifyface=", identifyface)
            print("無法辨識此人，請先訓練!!")
        else:
            name = identifyface["person"]["name"]
            confidence = float(identifyface["confidence"])
            if confidence >= 0.9:
                print(name + " 簽到成功!!!")
            elif confidence >= 0.8:
                print(name + " 簽到成功!!")
            elif confidence >= 0.7:
                print(name + " 簽到成功!")
            else:
                print(name + " 簽到成功")

  def SingIn(self):
    '''刷臉簽到'''
    imagepath = classes.ClassOpenCV.show_opencv
    self.Identify(imagepath)

  def Train(self, userData = None, personname = None):  #存檔有問題
    '''用三連拍訓練一個新人'''
    jpgimagepaths = []
    for i in range(3):
      jpgimagepath = classes.ClassOpenCV.show_opencv(
        hint = " (訓練第 " + str(i + 1) + " 張)"
      )
      jpgimagepaths.append(jpgimagepath)

    if personname == None:
      personname = input("請輸入你的名字：")
    
    if userData == None:
      userData = input("請輸入你的說明文字(ex. 高師大附中高三信)：")
    
    basepath = os.path.dirname(os.path.realpath(__file__)) #C:\Users\崇崇超人\Desktop\FacePI\classes
    jpgtrainpaths = []
    for jpgimagepath in jpgimagepaths:
      filename = os.path.basename(jpgimagepath)
      jpgtrainpath = os.path.join(
        basepath, "traindatas", userData, personname, filename
      )
      if not os.path.exists(os.path.dirname(jpgtrainpath)):
        os.makedirs(os.path.dirname(jpgtrainpath))
        print("not exist check")
      os.rename(jpgimagepath, jpgtrainpath)
      jpgtrainpaths.append(jpgtrainpath)

    myconfig = classes.ClassConfig.Config().readConfig()

    personAPI = classes.ClassPerson.Person()
    personAPI.add_personimages(
      myconfig["personGroupId"], personname, userData, jpgtrainpaths
    )
    personGroupapi = classes.ClassPersonGroup.PersonGroup()
    personGroupapi.train_personGroup()

  def showConfig(self, item_name):
    '''please enter the item you want to check. (ex. python main.py showConfig api_key)
       If you want to check all items, please type '0' '''
    config = classes.ClassConfig.Config().readConfig()
    if item_name == 0:
      for i in config:
        print(i + ': ' , config[i])
    else:
      print(config[item_name])

  def detectUrl(self, imageurl):
    classes.ClassFaceAPI.Face().detectImageUrl(imageurl)

  

if __name__ == '__main__':
    fire.Fire(FacePI)
