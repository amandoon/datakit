from datetime import datetime
from datetime import timedelta

# Get today's time
today = datetime.today()
print "------------------------ Today "
print today
print today.strftime("%Y-%m-%d")

print "------------------------ Yesterday "
print today - timedelta(days=24)
print (today - timedelta(days=24)).strftime('%Y-%m-%d')

print "------------------------ Tomorrow "
today = datetime.now()
print today + timedelta(days=1)
print (today + timedelta(days=1)).strftime("%Y-%m-%d")

print "---------------------- Convert string to time"
input_date = datetime.strptime('2015-02-25 13:41:21', "%Y-%m-%d %H:%M:%S")

print "---------------------- Extract hour from input date"
print input_date.strftime('%H')


print "----------------------- Extract date time from Unix epoch"
print datetime.fromtimestamp(1424900481)

print "---------------------------- Get time in UTC "
print  datetime.now() + (datetime.utcnow() - datetime.now())


