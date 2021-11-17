import pygame
from time import sleep
pygame.init()
controller = pygame.joystick.Joystick(4)
controller.init()
buttons = {'0':0,'1':0,'2':0,'3':0,
           '4':0,'5':0,'6':0,'7':0,
           'axis1':0.,'axis2':0.,'axis3':0.,'axis4':0.}
axiss=[0.,0.,0.,0.,0.,0.]


def getJS(name=''):

    global buttons
    # retrieve any events ...
    for event in pygame.event.get():                                # Analog Sticks
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value,2)
            #print(event.dict, event.joy, event.axis, 'PRESSED')
        elif event.type == pygame.JOYBUTTONDOWN:                    # When button pressed
            #print(event.dict, event.joy, event.button, 'PRESSED')
            for x,(key,val) in enumerate(buttons.items()):
                if x<8:
                    print(x)
                    if controller.get_button(x):buttons[key]=1
        elif event.type == pygame.JOYBUTTONUP:                      # When button released
            #print(event.dict, event.joy, event.button, 'released')
            for x,(key,val) in enumerate(buttons.items()):
                if x<8:
                    if event.button ==x:buttons[key]=0

    # to remove element 2 since axis numbers are 0 1 3 4
    buttons['axis1'],buttons['axis2'] ,buttons['axis3'] ,buttons['axis4']  = [axiss[0],axiss[1],axiss[2],axiss[3]]
    if name == '':
        return buttons
    else:
        return buttons[name]
def main():
    print(getJS()) # To get all values
    sleep(0.1)
    #print(getJS('share')) # To get a single value
    #sleep(0.05)


if __name__ == '__main__':
  while True:
    main()