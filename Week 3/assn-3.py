#assn 3.2
hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter Rate:")
r = float(rph)
if h<=40:
    sal=h*r
else:
    h=h-40
    h=h*15.75
    sal=(40*r)+h
print sal    


#assn- 3.3

score = raw_input("Enter your score:")
try: score = float(score)
except: score = -1
if score == -1: print "Are you kidding me?"
elif score >= 0.9: print "A"
elif score >= 0.8: print "B"
elif score >= 0.7: print "C"
elif score >= 0.6: print "D"
elif score < 0.6: print "F"