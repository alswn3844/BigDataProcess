import sys
import calendar
weekdayCode = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
uberList = {}
activeVehicleList = {}
tripList = {}
input = str(sys.argv[1])
output = str(sys.argv[2])

f = open(output, "wt")
with open(input, "rt") as fp:
	data = fp.read()
	lines = data.split("\n")
	for line in lines:
		uber = line.split(",")
		date = uber[1].split("/")
		day = weekdayCode[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))]
		if (uber[0], day) in uberList:
			activeVehicleList[(uber[0], day)] = uber[2]
			tripList[(uber[0], day)] += uber[3]
		else:
			activeVehicleList[(uber[0], day)] = uber[2]
			tripList[(uber[0], day)] = uber[3]
		
	keyList = tripList.keys()
for i in keyList:
	f.write("%s %s,%s\n" % (i, activeVehicleList[i], tripList[i]))
f.close()

