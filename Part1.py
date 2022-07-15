import csv

file = open('FileName.csv') #name of first data file to be read
csvreader = csv.reader(file)
datalist = []
for row in csvreader:
    datalist.append(row)
listlength = len(datalist)
tag_number_dictionary = {}
tag_number_list = []
for i in range(listlength):
    currentlist = datalist[i]
    if currentlist[1] not in tag_number_list:
        tag_number_lista.append(currentlist[1])

file = open('FileName2.csv') #name of second data file to be read
csvreader = csv.reader(file)
datalist2 = []
duration_dictionary = {}
for row in csvreader:
    datalist2.append(row)
current_tag = '0'
now_list = []
current_list = []
current_check = []
current_conversion = '0'
last_entry = {}
one_trip = {}

for i in range(len(tag_number_list)):
    now_list = []
    current_tag = tag_number_list[i]
    for i in range(len(datalist2)):
        current_check = datalist2[i]
        if current_check[1] == current_tag:
            now_list.append(current_check[2])
    x = len(now_list)
    if x == 1:
        one_trip[current_tag] = now_list[x-1]
    last_entry[current_tag] = now_list[x-1]
    
for i in range(len(tag_number_list)):
    current_list = []
    current_tag = tag_number_list[i]
    for i in range(len(datalist2)):
        current_check = datalist2[i]
        direction_list = []
        if current_check[1] == current_tag:
           current_conversion = current_check[0]
           if len(current_conversion) == 8:
               current_conversion = (int(current_conversion[0:2]))*60 + (int(current_conversion[3:5]))+(int((current_conversion[6:8]))/60)
               direction_list.append(current_conversion)
               direction_list.append(current_check[2])
               current_list.append(direction_list)
           else:
               current_conversion = (int(current_conversion[0:1]))*60 + (int(current_conversion[2:4]))+((int(current_conversion[5:7]))/60)
               direction_list.append(current_conversion)
               direction_list.append(current_check[2])
               current_list.append(direction_list)
        duration_dictionary[current_tag] = current_list
        

new_duration_dictionary = {}
for key in duration_dictionary:
    time_list = []
    while len(duration_dictionary[key]) > 1:
        for i in range(10):
            if len(duration_dictionary[key]) > 1:
                value = duration_dictionary[key]
                check_status = value[0]
                if check_status[1] == 'Arriving' or check_status[1] == 'Unknown':
                    del(((duration_dictionary[key])[0]))
                   
        if len(duration_dictionary[key]) >1:
            time_list.append((duration_dictionary[key])[0])
            time_list.append((duration_dictionary[key])[1])
            new_duration_dictionary[key] = time_list
            del(((duration_dictionary[key])[0]))
            del(((duration_dictionary[key])[0]))

timestamp_dictionary = {}
for key in new_duration_dictionary:
    x = new_duration_dictionary[key]
    time_length = len(x)
    list_of_timestamps = []
    for i in range(time_length):
        list_of_timestamps.append((x[i])[0])
    timestamp_dictionary[key] = list_of_timestamps        

time_dictionary = {}
for key in timestamp_dictionary:
    current_list = []
    timestamp_list = []
    short = 0
    medium = 0
    long = 0
    med_total_time = 0
    long_total_time = 0
    total_time = 0
    avg_long = 0
    avg_med = 0
    length = len(timestamp_dictionary[key])
    if length % 2 == 0:
        current = 0
        lengthNew = 0
        x = timestamp_dictionary[key]
        for i in range(length // 2):
            current_check = (float(x[current+1])) - (float(x[current]))
            timestamp_list.append(round(current_check,4))
            if current_check <= 3:
                short +=1
            elif current_check <= 6:
                medium += 1
                lengthNew += 1
                total_time += current_check
                med_total_time += current_check
            else:
                long += 1
                total_time += current_check
                long_total_time += current_check
                lengthNew += 1
            current += 2
        if lengthNew != 0:
            avg_time = round(((total_time) / (lengthNew)), 4)
            if medium != 0:
                avg_med = round(((med_total_time) / (medium)), 4)
            if long != 0:
                avg_long = round(((long_total_time) / (long)), 4)
            current_list.append(avg_time)
            current_list.append(avg_med)
            current_list.append(avg_long)
            
        else:
            current_list.append(0)
            current_list.append(avg_med)
            current_list.append(avg_long)
        current_list.append(short)
        current_list.append(medium)
        current_list.append(long)
        current_list.append(timestamp_list)
        time_dictionary[key] = current_list
    else:
        current = 0
        lengthNew = 0
        x = timestamp_dictionary[key]
        for i in range((length-1) // 2):
            current_check = (float(x[current+1])) - (float(x[current]))
            timestamp_list.append(round(current_check,4))
            if current_check <= 3:
                short +=1
            elif current_check <= 6:
                medium += 1
                total_time += current_check
                med_total_time += current_check
                lengthNew += 1
            else:
                long += 1
                total_time += current_check
                lengthNew += 1
                long_total_time += current_check
            current += 2
        if ((lengthNew-1)) != 0:
            avg_time = round((total_time // ((lengthNew-1))), 4)
            if medium != 0:
                avg_med = round(((med_total_time) / (medium)), 4)
            if long != 0:
                avg_long = round(((long_total_time) / (long)), 4)
            current_list.append(avg_time)
            current_list.append(avg_med)
            current_list.append(avg_long)
        else:
            current_list.append(0)
        current_list.append(short)
        current_list.append(medium)
        current_list.append(long)
        current_list.append(timestamp_list)
        time_dictionary[key] = current_list

for key in time_dictionary:
        tag_number_dictionary[key] = len((time_dictionary[key])[6])

for key in duration_dictionary:
    if key not in tag_number_dictionary:
        tag_number_dictionary[key] = 0

file = open('FileName3.csv') #name of file with tag numbers to be read
csvreader = csv.reader(file)
for row in csvreader:
    if row[1] in tag_number_dictionary:
        iList = []
        iList.append(row[0])
        iList.append(tag_number_dictionary[row[1]])
        tag_number_dictionary[row[1]] = iList
final_dictionary = {}
final_list = []
for key in tag_number_dictionary:
    if key in time_dictionary:
        final_list = []
        if type(tag_number_dictionary[key]) is list:
            final_list.append(key)
            final_list.append((tag_number_dictionary[key])[0]) 
            final_list.append(str(tag_number_dictionary[key][1])) 
            final_list.append(str((time_dictionary[key])[3])) 
            final_list.append(str((time_dictionary[key])[4])) 
            final_list.append(str((time_dictionary[key])[5])) 
            final_list.append(str((time_dictionary[key])[1])) 
            final_list.append(str((time_dictionary[key])[2])) 
            final_list.append(str((time_dictionary[key])[0])) 
            final_list.append(str((time_dictionary[key])[6])) 
            final_dictionary[key] = final_list
        else:
            final_list.append(key)
            final_list.append("no group") 
            final_list.append(str(tag_number_dictionary[key])) 
            final_list.append(str((time_dictionary[key])[3])) 
            final_list.append(str((time_dictionary[key])[4])) 
            final_list.append(str((time_dictionary[key])[5])) 
            final_list.append(str((time_dictionary[key])[1])) 
            final_list.append(str((time_dictionary[key])[2])) 
            final_list.append(str((time_dictionary[key])[0])) 
            final_list.append(str((time_dictionary[key])[6])) 
            final_dictionary[key] = final_list
    else:
        if type(tag_number_dictionary[key]) is list:
            final_list.append(key)
            final_list.append((tag_number_dictionary[key])[0]) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_dictionary[key] = final_list
        else:
            final_list.append(key)
            final_list.append("no group")
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_list.append(0) 
            final_dictionary[key] = final_list
        
header = ['ID', 'Tag Group', 'Total # of Trips', '# of Short Trips', '# of Med Trips', '# of Long Trips',
          'Avg of Med Trip Durations', 'Avg of Long Trip Durations', 'Avg of Med and Long Durations', 'All Trip Durations']

list_compilation = []
for key in final_dictionary:
    list_compilation.append(final_dictionary[key])
data = list_compilation


with open('FileName4.csv', 'w') as f:#name of file for data to be written into
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

         
