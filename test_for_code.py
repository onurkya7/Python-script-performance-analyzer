import time 
import psutil
import threading
import os

# Ram Default
top = 0
for i in range(5):
    z = int((str(psutil.virtual_memory().used))[:4])
    time.sleep(0.1)
    top += z
bas_ram = str(top/5)[:4]
    
# Test Code
def your_code():
    baslangic =  time.time()
    # Paste your code here
    ######################



    
    #######################
    # Code Time 
    saniye = time.time() - baslangic
    print("TIME:",str(saniye)[:5] + " Second")
    os.mkdir('deneme')

# Benchmark for Code
def bench():
    cpu = []
    ram = []
    def display_usage(cpu_usage,mem_usage):
        cpu_percent = (cpu_usage)
        mem_percent = (mem_usage / 100.0)
        cpu.append(cpu_percent)
        ram.append(mem_percent)
    while True:
        display_usage(psutil.cpu_percent(), psutil.virtual_memory().used)
        time.sleep(0.1)
        if os.path.exists('deneme'):
            print("CPU: " + " % " + str(sum(cpu)/len(cpu))[:4])
            print("RAM: ", abs(int(str(sum(ram)/len(ram))[:4]) - int(bas_ram)),"MB")
            os.rmdir("deneme")
            break
                
if __name__ == '__main__':
    t1 = threading.Thread(target=your_code)
    t2 = threading.Thread(target=bench)
    t1.start()
    t2.start()