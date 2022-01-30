import json, os

class Config:
    def __init__(self):
        basepath = os.path.dirname(os.path.realpath(__file__))
        self.Configpath = os.path.join(basepath, '../Config.json')

    def readConfig(self):
        with open(self.Configpath, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config

    def writeConfig(self, config):
        with open(self.Configpath, "w", encoding="utf-8") as f:
            json.dump(config, f)

    def setConfig(self):
        config = self.readConfig()
        print("The '[]' after th value is the default value, press ENTER if you don't want to modify it.")
        api_key = input(f'Please enter the API_KEY, current -> [{config["api_key"]}]: ')
        if api_key: config["api_key"] = api_key
        title = input(f'Please enter the TITLE, current -> [{config["title"]}]: ')
        if title: config["title"] = title
        self.writeConfig(config)
    
    '''
    (已使用readConfig取代)
    
    def showConfig(self):
        config = self.readConfig()
        return config
    '''