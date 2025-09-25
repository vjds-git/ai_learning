from datetime import datetime

# Current date and time
now = datetime.now()
print("Now:", now)

# Format it nicely
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Parse a string into datetime
dt = datetime.strptime("2025-09-20 14:30", "%Y-%m-%d %H:%M")
print("Parsed:", dt)

# Difference between two datetimes
future = datetime(2025, 12, 31, 23, 59)
delta = future - now
print("Days until new year:", delta.days)
