# return-starter
# Henry Roeser 
# 11/19/24

# Project 1: Destination Europe
def describe_vacation(destination, activity, season = 'summer'):
    # description_1 = describe_vacation(f'Im going on vacation to {destination} to {activity} in the {season}.')
    # description_2 = describe_vacation(f'Im going on vacation to {destination} to {activity} in the {season}.')
    # print(description_1)
    # print(description_2)
    return f"I'm going on vacation to {destination} to {activity} in the {season}."



description_1 = describe_vacation('Hawaii', 'surf')
description_2 = describe_vacation('Iceland', 'ski', 'winter')
print(description_1)
print(description_2)

# Project 2: Student Major
def show_major(first_name, university, major = 'Sports Medicine'):
    print(f'{first_name} attends the {university} and is majoring in {major}. ')
show_major('Henry', 'University of Michigan', 'Computer Science')
show_major('Jaxsen', 'University of Florida')