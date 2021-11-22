import json, fire

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
    api_key = input(f'Please enter the API_KEY[{config["api_key"]}]: ')
    if api_key: config["api_key"] = api_key
    title = input(f'Please enter the TITLE[{config["title"]}]: ')
    if title: config["title"] = title
    self.writeConfig(config)
    
  def showConfig(self):
    print(self.readConfig())


if __name__ == '__main__':
    fire.Fire(FacePI)
