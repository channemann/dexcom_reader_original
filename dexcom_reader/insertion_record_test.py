import readdata

dd = readdata.Dexcom.FindDevice()
dr = readdata.Dexcom(dd)
meter_records = dr.ReadRecords('METER_DATA')
print meter_records[0]
print meter_records[-1]
insertion_records = dr.ReadRecords('INSERTION_TIME')
# print insertion_records[0]
# print insertion_records[-1]
print insertion_records