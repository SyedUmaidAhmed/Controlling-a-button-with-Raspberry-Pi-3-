
from gpiozero import Button



btn = Button(4)

while True:

    btn.wait_for_press()
    print('You pressed me')
    btn.wait_for_release()
    print('You released me')
    
    
