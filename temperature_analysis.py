# Name: [Your Name]
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
def find_min_max(temperature):
    max=0
    min=temperature[0]
    for temp in temperature:
        if temp>=max:
            max=temp
        if temp<=min:
            min=temp
        
    print("Highest temperature: "+ str(max)+"°C")
    print("Lowest Temperature: "+ str(min)+"°C")
find_min_max(temperatures)





print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
def count_hot_days(temperature):
    count=0
    for temp in temperature:
        if temp<=30:
            continue
        else:
            count+=1
    print("Hot Days (>30°C): ",count)
count_hot_days(temperatures)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
def alert_system(temperature):
    count=0
    for temp  in temperature:
        if temp>=40:
            extreme_temp_day=temperature.index(temp)+1
            break
        if temp>30:
            count+=1
        
    print("Hot Days before alert: ",count)
    print("Alert! Extreme temperature 40°C detected on Day ",extreme_temp_day)

alert_system(temperatures)
