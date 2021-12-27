import json, fire, http.client, urllib.request, urllib.parse, urllib.error, base64
#cognitive document >> https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236.
#handouts >> https://github.com/jiangsir/TestFacePI
import classes.ClassConfig, classes.ClassFaceAPI, classes.ClassOpenCV

class FacePI:
  def __init__(self):
    self.Config = classes.ClassConfig.Config()
    self.Face = classes.ClassFaceAPI.Face()

  def show_opencv(self):
    classes.ClassOpenCV.show_opencv('hint')
  
  def SigninUrl(self, imageurl):
    '''
    線上刷臉簽到
    '''
    self.Face.detectFaceUrl(imageurl)
  
  def SigninLocal(self, imagepath):
    '''
    本地刷臉簽到
    '''
    self.Face.detectLocalImage(imagepath)

  def showConfig(self):
    self.Config.showConfig()

  def detectUrl(self, imageurl):
    self.Face.detectFaceUrl(imageurl)

  

if __name__ == '__main__':
    fire.Fire(FacePI)
