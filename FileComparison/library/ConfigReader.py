import configparser

def readConfigData(section,key):
    config = configparser.ConfigParser()
    config.read("./configurationFiles/Config.cfg")
    return config.get(section,key)

