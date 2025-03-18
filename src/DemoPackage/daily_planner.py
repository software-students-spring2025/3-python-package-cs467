"""
A personalized daily planner function that helps the users to list their tasks

param: name -> a string represents users name
return: none
"""
def daily_planner(name):
    print('\nWelcome to your daily planner!')
    tdlist = []

    # store the task and priority in 'tdlist'
    while True:
        task = input('Enter your task (type \'done\' to finish)\nTask: ').strip()
        if task.lower() == 'done':
            break

        priority = input('Priority (1-3, 3 being heighest): ').strip()
        if priority not in ['1', '2', '3']:
            print('⚠️ Invalid input. Please enter 1, 2, or 3.')
            priority = input('Priority (1-3, 3 being heighest): ').strip()

        tdlist.append({'task':task, 'priority':priority})

    # sort 'tdlist' according to the priority
    sorted_tdlist = sorted(tdlist, key=lambda x: x['priority'], reverse=True)

    # change the priority from number to text
    for i in sorted_tdlist:
        if i['priority'] == '1':
            i['priority'] = 'LOW'
        elif i['priority'] == '2':
            i['priority'] = 'MEDIUM'
        else:
            i['priority'] = 'HIGH'
    
    # print the result
    result = ''
    result += '\n~~~~~{0}\'s schedule for today~~~~~\n'.format(name)
    for i in range(len(sorted_tdlist)):
        task = sorted_tdlist[i]
        result += '{0}. [{1}] {2}\n'.format(i+1, task['priority'], task['task'])

    return result

print(daily_planner('benny'))