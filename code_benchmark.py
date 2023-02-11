import time 
import psutil
import threading
import os

def your_code():
    baslangic =  time.time()

    #Paste your code here
    #####################
    

    #####################

    saniye = time.time() - baslangic
    print("Geçen Toplam Süre: ",saniye)

    os.mkdir('deneme')

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
        time.sleep(0.5)
        if os.path.exists('deneme'):
            print("Ortalama Cpu Kullanimi: ",str(sum(cpu)/len(cpu))[:5])
            print("Ortalama Ram Kullanimi: ",abs(int(str(sum(ram)/len(ram))[:4]) - int((str(psutil.virtual_memory().used))[:4])))
            os.rmdir("deneme")
            break
                
if __name__ == '__main__':
    t1 = threading.Thread(target=your_code)
    t2 = threading.Thread(target=bench)
    t1.start()
    t2.start()