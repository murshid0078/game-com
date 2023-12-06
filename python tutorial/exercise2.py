import time
timestamp=time.strftime("%H:%M:%S:")
print(timestamp)
timestamp =int(time.strftime("%H"))
print(timestamp)
timestamp = int(time.strftime("%M"))
print(timestamp)
timestamp = int(time.strftime("%S"))
print(timestamp)

if(5<=timestamp<12):
    print("good morning,sir")
elif(12<=timestamp<18):
    print("good afternoon,sir")
else:
    print("good evening,sir")
# import time

# # Get the current time
# current_time = time.localtime()

# # Extract the hour, minute, and second
# current_hour = current_time.tm_hour
# current_minute = current_time.tm_min
# current_second = current_time.tm_sec

# # Define the greeting based on the current hour
# if 5 <= current_hour < 12:
#     greeting = "Good morning"
# elif 12 <= current_hour < 17:
#     greeting = "Good afternoon"
# else:
#     greeting = "Good evening"

# # Print the greeting along with the current time
# print(f"{greeting}, it's {current_hour}:{current_minute}:{current_second}. How can I assist you?")
