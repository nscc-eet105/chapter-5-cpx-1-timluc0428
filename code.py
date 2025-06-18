from adafruit_circuitplayground import cp
import time

#function receives the value of the light sensor and scales it to output
#an integer corresponding to a pixel. (0-9)
def scale(value):
    #the maxIndex is the highest number I want to return. 
    maxIndex = 9
    index = int(round(value/315 * maxIndex))
#    print(index)
    return index

#function simplifies turning all the pixels off
def pixel_black():
    for i in range(0, 10):
        cp.pixels[i] = (0, 0, 0)
    
def main():
    while True:
        pixel_black()
        #assigns the light sensor to a variable 
        light = cp.light
        #calls the function to scale the light sensor value to within the range
        #of the number of our pixels, and assigns it to a variable
        index = scale(light,)
        #identifies the pixel to turn on based on the scaled value from the 
        #light sensor.
        cp.pixels[index] = (0, 0, 255)
        time.sleep(.01)
    
main()
    
