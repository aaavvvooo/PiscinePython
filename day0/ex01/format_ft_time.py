import time
from datetime import date

sep_time = "{:,.4f}".format(time.time())
sc_time = "{:.2e}".format(time.time())
today = date.today().strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {sep_time} or {sc_time} in\
scientific notation")
print(today)
