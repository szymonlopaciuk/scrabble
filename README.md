## Scrabble
Play scrabble with friends on your local network

* Still in dev.
* Please see the [DevFlow](DevFlow.md) file for issues I'm fixing.

**You'll need to checkout the `uat` branch to test. Please note that the gameplay itself is still in develpoment**

## Sneak-Peak
Here's a sneak-peak, nonetheless
![](sc.png)

## UAT Testing
- Checkout the `uat` branch: `git checkout uat`
- To test, You'll need Python3.6+ installed on your computer.
- Create a virtual environment, activate it, and install the requirements: `pip3 install -r requirements.txt`. 
- At the root folder, in the virtual environment, simply run `python3 wsgi.py`.
- By default, the application tries to get your local private IP address (not localhost) to run on. However, if you're using a VPN or are on a weird network, it may get it wrong. Feel free to modify the `host` variable in `wsgi.py` to your actual local private IP address. The only caveat is that you have to host the app on the private IP address and not `localhost`. This is in order to allow other players on your network to visit the application.
- Navigate to your local IP address (`192.168...:5005`) to view the app. 
- Host a game session and then connect other systems (players) to start the scrabble game
