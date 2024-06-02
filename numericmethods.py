import time
from colorama import Fore
import tracemalloc

def fx(x,y):
    return  y - x**2 + 1


def heun(start,start_val,end,iter,fx):
    diff = (end-start)/iter

    while start<end:
        k1 = fx(start,start_val)
        k2 = fx(start+diff,start_val+k1*diff)
        start_val = start_val + diff*(k1/2 + k2/2)    
        start+=diff
    return start_val


def midpoint(start,start_val,end,iter,fx):
    diff = (end-start)/iter
    while start<end:
        k1 = fx(start,start_val)
        k2 = fx(start+diff/2,start_val+(k1/2)*diff)
        start_val = start_val + k2*diff
        start+=diff
    return start_val

def ralston(start,start_val,end,iter,fx):
    diff = (end-start)/iter

    while start<end:
        k1 = fx(start,start_val)
        k2 = fx(start+(3/4)*diff,start_val+(3/4)*k1*diff)
        start_val = start_val + diff*((1/3)*k1+(2/3)*k2)
        start+=diff
    return start_val

iterations = [5,10,20,50,100]

heun_times = []
midpoint_times = []
ralston_times = []

heun_results = []
midpoint_results = []
ralston_results = []

heun_memories = []
midpoint_memories = []
ralston_memories = []

for iteration in iterations:
    tracemalloc.start()
    clock = time.perf_counter()
    heun_result = heun(start=0,start_val=0.5,end=0.4,iter=iteration,fx=fx)
    clock = time.perf_counter() - clock
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    heun_times.append(clock)
    heun_memories.append(peak / 10**6 - current / 10**6)
    heun_results.append(heun_result)
    print(f"{Fore.LIGHTRED_EX}Heun Metodu{Fore.WHITE} {Fore.GREEN}{clock:.20f}{Fore.WHITE} saniye içinde {Fore.CYAN}{iteration}{Fore.WHITE} iterasyonda {Fore.LIGHTRED_EX}{peak / 10**6 - current / 10**6:.10f} MB bellek kullanımı ile {Fore.WHITE} {Fore.YELLOW}{heun_result}{Fore.WHITE} değerini elde etti.")
    
    tracemalloc.start()
    clock = time.perf_counter()
    midpoint_result = midpoint(start=0,start_val=0.5,end=0.4,iter=iteration,fx=fx)
    clock = time.perf_counter()-clock
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    midpoint_times.append(clock)
    midpoint_memories.append(peak / 10**6 - current / 10**6)
    midpoint_results.append(midpoint_result)
    print(f"{Fore.LIGHTBLUE_EX}Midpoint Metodu{Fore.WHITE} {Fore.GREEN}{clock:.20f}{Fore.WHITE} saniye içinde {Fore.CYAN}{iteration}{Fore.WHITE} iterasyonda {Fore.LIGHTRED_EX}{peak / 10**6 - current / 10**6:.10f} MB bellek kullanımı ile {Fore.WHITE}{Fore.YELLOW}{midpoint_result}{Fore.WHITE} değerini elde etti.")
    
    tracemalloc.start()
    clock = time.perf_counter()
    ralston_result = ralston(start=0,start_val=0.5,end=0.4,iter=iteration,fx=fx)
    clock = time.perf_counter()-clock
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    ralston_times.append(clock)
    ralston_memories.append(peak / 10**6 - current / 10**6)
    ralston_results.append(ralston_result)
    print(f"{Fore.LIGHTYELLOW_EX}Ralston Metodu{Fore.WHITE} {Fore.GREEN}{clock:.20f}{Fore.WHITE} saniye içinde {Fore.CYAN}{iteration}{Fore.WHITE} iterasyonda {Fore.LIGHTRED_EX}{peak / 10**6 - current / 10**6:.10f} MB bellek kullanımı ile {Fore.WHITE}{Fore.YELLOW}{ralston_result}{Fore.WHITE} değerini elde etti.")    



from prettytable import PrettyTable 
 
myTable = PrettyTable(["İterayon", "Heun Sonucu", "Orta Nokta Sonucu", "Ralston Sonucu"]) 
 

for index,iteration in enumerate(iterations):
    myTable.add_row([f"{iteration}", heun_results[index], midpoint_results[index], ralston_results[index]])
 
print(myTable,"\n")

myTable = PrettyTable(["İterayon", "Heun Süresi (s)", "Orta Nokta Süresi (s)", "Ralston Süresi (s)"]) 
 

for index,iteration in enumerate(iterations):
    myTable.add_row([f"{iteration}", f"{heun_times[index]:.10f}", f"{midpoint_times[index]:.10f}", f"{ralston_times[index]:.10f}"])
print(myTable)
myTable = PrettyTable(["İterayon", "Heun Bellek (MB)", "Orta Nokta Bellek (MB)", "Ralston Bellek (MB)"]) 
for index,iteration in enumerate(iterations):
    myTable.add_row([f"{iteration}", f"{heun_memories[index]:.10f}", f"{midpoint_memories[index]:.10f}", f"{ralston_memories[index]:.10f}"])
print(myTable)
from matplotlib import pyplot as plt
plt.subplot(2,1,1)
plt.xlabel("Iterasyon Sayısı")
plt.ylabel("Süre (saniye)")
plt.plot(iterations, heun_times, label="Heun")
plt.plot(iterations, midpoint_times, label="Midpoint")
plt.plot(iterations, ralston_times, label="Ralston")
plt.legend()

plt.subplot(2,1,2)
plt.xlabel("Iterasyon Sayısı")
plt.ylabel("Bellek Kullanımı (MB)")
plt.plot(iterations, heun_memories, label="Heun")
plt.plot(iterations, midpoint_memories, label="Midpoint")
plt.plot(iterations, ralston_memories, label="Ralston")
plt.legend()
plt.show()