from guizero import App, PushButton
from gpiozero import LED
import sys

led = LED(21)

def exitApp():
    sys.exit()
    
def toggleLED():
    led.toggle()
    if led.is_lit :
        ledButton.text ="LED OFF"    
    else :
        ledButton.text ="LED ON"    
    
app = App('First Gui', height = 600, width = 800)

ledButton = PushButton(app, toggleLED, text="LED ON", align="top",width = 15, height = 3)
ledButton.text_size = 36

exitButton = PushButton(app, exitApp, text="Exit", align="bottom" , width = 15, height = 3)
exitButton.text_size = 36

app.display()