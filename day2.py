# get data/reports
reports = []
with open("day2_input_eg.txt", "r") as reports_file:
    reports = reports_file.readlines()

# challenge 1: check number of reports that indicate safe levels
#TODO challenge 2: report is safe if removing one bad level makes it safe
def is_report_safe(report):
    levels = [int(i) for i in report.split()]
    max_index = len(levels)-1
    bad_levels = 0
    for index, level in enumerate(levels):
        if index == max_index: # have already checked the last figure
            return True
        elif is_level_safe(level, index, levels):
            continue
        else: return False
"""
            if bad_levels >= 1:
                return False
            else:
                for i in range(index, max_index+1):
                    bad_levels += 1  
                    dampened_report = levels[:index]+levels[index+1:]             
                    if is_level_safe(levels[index+1], index, dampened_report) and is_level_safe(levels[index-1], index, dampened_report):
                        continue
                    else:
                        return False
"""


def is_level_safe(level, index, levels):
    if level == levels[index+1]: # no change
        print(levels, level, "Report displays no change")
        return False
    elif level+4 <= levels[index+1]:# and level-3 >= levels[index+1]: # change must be gradual
        print(levels, level, "Report's increase is not gradual")
        return False
    elif level-4 >= levels[index+1]:
        print(levels, level, "Report's decrease is not gradual")
        return False
    elif index != 0: # change must be consistent
        if levels[index-1] < level and levels[index+1] < level:
            print(levels, level, "Report's change is not consistent")
            return False
        elif levels[index-1] > level and levels[index+1] > level:
            print(levels, level, "Report's change is not consistent")
            return False
    else:
        print(levels, level, "Level safe")
        return True



safe_counter = 0
for report in reports:
    report_safe = is_report_safe(report)
    print(f"Is `{report}` safe? {report_safe}")
    if report_safe:
        safe_counter += 1

print(f"Total safe reports: {safe_counter}")
    