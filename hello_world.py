from burp import IBurpExtender
from java.io import PrintWriter

class BurpExtender(IBurpExtender):
    
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("My Extension Name")
        stdout = PrintWriter(callbacks.getStdout(), True)
        stdout.println("Hello World")
        return