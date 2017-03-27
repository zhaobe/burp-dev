# IBurpExtender is used for hooking into Burp
# java.io PrinterWriter class is used to print to Burp
from burp import IBurpExtender
from java.io import PrintWriter

class BurpExtender(IBurpExtender):
    
    def registerExtenderCallbacks(self, callbacks):
        # this is the extension name
        callbacks.setExtensionName("My Extension Name")
        # create stdout object
        stdout = PrintWriter(callbacks.getStdout(), True)
        stdout.println("Hello World")
        return