#1 /usr/bin/env python
from dictionary import dictionary
import sys
import random
import datetime

def humanize_date_difference(now, otherdate=None, offset=None):
    if otherdate:
        dt = now - otherdate
        offset = dt.seconds + (dt.days * 60*60*24)
    if offset:
        delta_s = offset % 60
        offset /= 60
        delta_m = offset % 60
        offset /= 60
        delta_h = offset % 24
        offset /= 24
        delta_d = offset
    elif otherdate is not None:
        delta_s = 0
        delta_m = 0
        delta_h = 0
        delta_d = 0
    else:
        raise ValueError("Must supply otherdate or offset (from now)")

    if delta_d > 1:
        if delta_d > 6:
            date = now + datetime.timedelta(days=-delta_d, hours=-delta_h, minutes=-delta_m)
            return date.strftime('%A, %Y %B %m, %H:%I')
        else:
            wday = now + datetime.timedelta(days=-delta_d)
            return wday.strftime('%A')
    if delta_d == 1:
        return "Yesterday"
    if delta_h > 0:
        return "%dh%dm" % (delta_h, delta_m)
    if delta_m > 0:
        #return "%dm%ds ago" % (delta_m, delta_s)
        return "%dm%d" % (delta_m, delta_s)
    else:
        return "%ds" % delta_s

if __name__ == '__main__':

    dict_size = len(dictionary)
    quantity = raw_input("How many words? [20] ")
    words = list()
    count = 0
    while count < int(quantity):
        lookup = dictionary[random.randint(0, dict_size-1)]
        if not ("l" in lookup.lower() or "o" in lookup.lower()):
            count += 1
            words.append(lookup)

    sentence = ""
    for each in words:
        sentence += each + " "
    print sentence + "\n"
    before = datetime.datetime.now()
    tocheck = raw_input("Enter the sentence above\n")
    if tocheck == sentence[:len(sentence)-1]:
        finish_time = datetime.datetime.now()
        print humanize_date_difference(finish_time, before)
    else:
        print "FAILED, didn't match"
        print humanize_date_difference(finish_time, before)
