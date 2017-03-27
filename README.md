# burp-dev
Development with Burp Plugins

## Python Development Setup
- download Burp Suite from their [site](https://portswigger.net/burp/freedownload)
- if you have brew on your local machine, use `brew install jython`
- open Burp Suite > click on the `Extender` tab and then the subtab for `Options`
- under Python Environment click Select File and locate `jython.jar`
    - since you installed it through brew, it will most likely be under `/usr/local/Cellar/jython/<versionNumber>/libexec/jython.jar`
- once you have the environment setup, you can go to the subtab called `Extensions` > click on Add
- under Extension Details > Select Python for Extension type, then find the simple `hello_world.py` from this repo
- once you have loaded the extension, you should get an output of `Hello World`

