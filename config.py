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

def write_config():
    """
    Returns: nothing
    """
    with open("config.cfg","w") as archivo:
        archivo.write("# Game config file\n\n# Lines starting with \"#\" are comments\n# and will not be read by the game.\n\n# Whether to show FPS on screen or not\n# 1=yes; 0=no\nShowFPS=1\n\n# Resolution of the screen, in pixels\nWindowHEIGHT=480\nWindowWIDTH=640".encode("utf-8"))
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
                linea = linea.rstrip("\n")
                print "[Parser] Reading cfg line '" + linea.encode("utf-8") + "'"
                if linea == "": continue
                if linea[0] == "#": continue
                linearr = linea.split("=")
                if linearr[0] == "ShowFPS" and linearr[1] == "1": config.setShowFPS(True)
                elif linearr[0] == "ShowFPS" and linearr[1] == "0": config.setShowFPS(False)
                elif linearr[0] == "WindowHEIGHT": config.setWindowALTO(int(linearr[1]))
                elif linearr[0] == "WindowWIDTH": config.setWindowANCHO(int(linearr[1]))
                else: 
                    print "[WARNING] Invalid .cfg file, using default config."
                    return config
        return config
    except IOError as exc:
        print "An error has occurred: " , exc
        print "Writing cfg file again..."
        write_config()
        return config
