from datetime import datetime, date, timedelta

# print(datetime.now())
# print(datetime.now() - timedelta(days=5))
# print(datetime.now() + timedelta(hours=8))
# print(datetime.now().strftime("%Y %m %d, %H:%M:%S"))


date_input = input("Enter date: ")
date = datetime.strptime(date_input, "%Y-%m-%d")
difference = datetime.now() - date
print("Years:", round(difference.days / 365))
print("Months:", round(difference.days / 31))
print("Days:", difference.days)
print("Hours:", round(difference.total_seconds() / 3600))
print("Minutes:", round(difference.total_seconds() / 60))
print("Seconds:", round(difference.total_seconds()))
