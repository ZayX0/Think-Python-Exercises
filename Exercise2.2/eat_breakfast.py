startingTimeSec = (6*60+52)*60
easyPaceSec = (8*60+15)*2
hardPaceSec = (7*60+12)*3

finish_hour_conversion = (startingTimeSec + easyPaceSec + hardPaceSec) / (60*60)
finish_floored = (startingTimeSec + easyPaceSec + hardPaceSec) // (60*60)
finish_min = (finish_hour_conversion - finish_floored)*60
print(finish_floored)
print(finish_min)
print('Finish time is %d:%d') % (finish_hour_conversion, finish_min)
