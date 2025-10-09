def least_interval(tasks, n):
    task_counts = {}
    for task in tasks:
        if task in task_counts:
            task_counts[task] += 1
        else:
            task_counts[task] = 1
    # print("Task counts: ", task_counts)

    
    next_available = {}
    for task in task_counts:
        next_available[task] = 0 

    print("next_available", next_available)
    time = 0
    tasks_left = len(tasks)
    print("task_left ", tasks_left)

    while tasks_left > 0:
        chosen_task = None
    

        for task in task_counts:
            if task_counts[task] > 0 and next_available[task] <= time:
                chosen_task = task
                break

        if chosen_task is not None:
            print(f"Time {time}: Run {chosen_task}")
            task_counts[chosen_task] -= 1
            next_available[chosen_task] = time + n + 1 
            tasks_left -= 1
        else:
            print(f"Time {time}: Idle")

        time += 1

    return time

# tasks = ['A', 'B', 'A', 'B','A']
# n = 2
# total_time = least_interval(tasks, n)
# print("\nTotal time needed:", total_time)
