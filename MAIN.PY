import matplotlib .pyplot as plt
import psutil as p
app_name_list = []
app_name_percentage_list = []
count=0
for process in p.process_iter():
    count = count +1
    if count <= 10:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name, '-- cpu_usage : ', cpu_usage)
        app_name_list.append(name)
        app_name_percentage_list.append(cpu_usage)
plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(app_name_list, app_name_percentage_list, width=0.10
,color=("purple","green","red","blue","orange","pink"))
plt.show()