from datetime import datetime

week_day_birthday = {'Monday:': [],
                     'Tuesday:': [],
                     'Wednesday:': [],
                     'Thursday:': [],
                     'Friday:': []
                     }


def sort_user_birthday(user, date):
    week_day = date.weekday()
    if week_day == 1:
        week_day_birthday['Tuesday:'].append(user)
    elif week_day == 2:
        week_day_birthday['Wednesday:'].append(user)
    elif week_day == 3:
        week_day_birthday['Thursday:'].append(user)
    elif week_day == 4:
        week_day_birthday['Friday:'].append(user)
    else:
        week_day_birthday['Monday:'].append(user)


def congratulations_day(user_list):
    for elem in user_list:
        for key, value in elem.items():
            new_value = value.split('.')
            birthday_day = datetime(year=int(new_value[2]), month=int(new_value[1]), day=int(new_value[0]))
            sort_user_birthday(key, birthday_day)


def print_info(user_dict):
    for key, value in user_dict.items():
        day = key
        user = ', '.join(value)
        print(f'{day} {user}')


test = [{'Nic': '21.08.2002', 'Karl': '24.08.2002'}]


if __name__ == '__main__':
    congratulations_day(test)
    print_info(week_day_birthday)
