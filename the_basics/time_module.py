import time

print(time.ctime(0)) # convert a time expressed in seconds since the epoch to a string representing local time
                     # epoch = when your computer thinks time started (1/1/1970)
                     
print(time.time()) # return current seconds that have passed since epoch

print(time.ctime(time.time())) # convert current time to string

time_object = time.localtime() # return a time.struct_time object
time_object = time.gmtime() # return a time.struct_time object in UTC time
print(time_object) # time.struct_time(tm_year=2020, tm_mon=7, tm_mday=28, tm_hour=14, tm_min=34, tm_sec=10, tm_wday=1, tm_yday=210, tm_isdst=0)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) # https://docs.python.org/3/library/time.html#time.strftime
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y") # convert a string to a time.struct_time object
print(time_object)

time_tuple = (2020, 7, 28, 14, 34, 10, 1, 210, 0) # year, month, day, hour, minute, second, weekday, yearday, daylight savings
time_string = time.asctime(time_tuple) # convert a time.struct_time object to a string
print(time_string)