# Problem 21
def minimum_classrooms(timings):
    max_classrooms = 1
    for time in timings:
        for check_time in timings:
            temp_classrooms = 1
            if time is not check_time:
                if intersect(time, check_time):
                    temp_classrooms += 1
            max_classrooms = max(max_classrooms, temp_classrooms)
    return max_classrooms

def intersect(time1, time2):
    if time1[0] > time2[0]:
        min_time = time2
        max_time = time1
    else:
        min_time = time1
        max_time = time2
    if min_time[1] > max_time[0]:
        return True
    return False

print(minimum_classrooms([(30, 74), (0, 50), (60, 75)]))