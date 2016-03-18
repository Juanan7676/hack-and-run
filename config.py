from pip._vendor.distlib.util import ARCHIVE_EXTENSIONS

class Config:
    def __init__(self):
        self.showFPS = True
        self.WindowANCHO = 640
        self.WindowALTO = 480
    def setShowFPS(self, show):
        self.showFPS = show
    def getShowFPS(self):
        return self.showFPS
    def setWindowANCHO(self, ancho):
        self.WindowANCHO = ancho
    def getWindowANCHO(self):
        return self.WindowANCHO
    def setWindowALTO(self, alto):
        self.WindowALTO = alto
    def getWindowALTO(self):
        return self.WindowALTO

def load_config(path):
    """
    Arguments:
         path: path to config.cfg
    
    Returns:Config instance
    """
    config = Config()
    try:
        with open(path, "r") as archivo:
            for linea in archivo.readlines():
                linea = linea.decode("utf-8")
                if linea[0] == "#": continue
                linearr = linea.split("=")
                if linearr[0] == "ShowFPS" and linearr[1] == "1": config.setShowFPS(True)
                elif linearr[0] == "ShowFPS" and linearr[1] == "0": config.setShowFPS(False)
                elif linearr[0] == "WindowHEIGHT": config.setWINDOWALTO(int(linearr[1]))
                elif linearr[0] == "WindowWIDTH": config.setWINDOWANCHO(int(linearr[1]))
                else: 
                    print "[WARNING] Invalid .cfg file, using default config."
                    return config
        return config
    except IOError as exc:
        print "An error has occurred: " , exc
        print "Using default config..."
        return config
