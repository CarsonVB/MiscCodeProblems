class Process:
    def __init__(self, burst_io, subscript):
        self.burst_io = burst_io
        self.subscript = subscript
        self.response_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.icount = 0
        self.curr_burst = self.burst_io[self.icount]

    def updateburst(self):
        self.curr_burst = self.burst_io[self.icount]


P1 = Process([6, 41, 5, 42, 7, 40, 8, 38, 6, 44, 5, 41, 9, 31, 7, 43, 8], 'P1')
P2 = Process([12, 24, 4, 21, 11, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4], 'P2')
P3 = Process([2, 21, 8, 25, 12, 29, 6, 26, 8, 33, 9, 22, 6, 24, 4, 29, 16], 'P3')
P4 = Process([5, 35, 7, 41, 14, 45, 4, 51, 9, 61, 10, 54, 11, 82, 5, 77, 3], 'P4')
P5 = Process([6, 33, 7, 44, 5, 42, 9, 37, 8, 46, 5, 41, 7, 31, 4, 43, 3], 'P5')
P6 = Process([14, 24, 12, 21, 11, 36, 12, 26, 9, 31, 19, 28, 10, 21, 6, 13, 3, 11, 4], 'P6')
P7 = Process([17, 46, 13, 41, 6, 42, 12, 21, 11, 32, 8, 19, 16, 33, 10], 'P7')
P8 = Process([6, 14, 7, 33, 8, 51, 9, 63, 10, 87, 11, 74, 8], 'P8')
P9 = Process([5, 32, 6, 40, 5, 29, 6, 21, 5, 44, 6, 24, 5, 31, 6, 33, 12], 'P9')

All_processes = [P1, P2, P3, P4, P5, P6, P7, P8, P9]

processes_queue = {
    0: [P1, P2, P3, P4, P5, P6, P7, P8, P9]
}

def simulate_fcfs(queue):
    total_time = 0
    idle_time = 0
    i = 0
    # i is current time
    while len(queue) > 0:
        # while queue has entries
        if not dict(filter(lambda x: x[0] <= total_time, queue.items())):
        #If no processes in ready queue
            idle_time += 1
            total_time += 1
        if i in queue:
            print('Current time:', total_time)
            temp_q = dict(filter(lambda x: x[0] <= total_time, queue.items()))
            if temp_q:
                ready_queue = 'Processes in ready queue: '
                for k, v in temp_q.items():
                    for process in v:
                        ready_queue += process.subscript + ', '
                print(ready_queue)
                print('Length of next CPU burst:', list(temp_q.items())[0][1][0].curr_burst)
            temp_q = dict(filter(lambda x: x[0] > total_time, queue.items()))
            if temp_q:
                io_queue = 'Processes in I/O: '
                for k, v in temp_q.items():
                    for process in v:
                        io_queue += process.subscript + ' has ' + str(k - total_time) + ' left in I/O, '
                print(io_queue)
            current_process = queue[i]
            if len(current_process) == 1:
                # if the amount of processes entered at the current time is only 1
                current_process = current_process[0]
                if current_process.icount == 0:
                    #time to calculate RT
                    current_process.response_time = total_time
                cpu_burst = current_process.burst_io[current_process.icount]
                if current_process.icount != len(current_process.burst_io) - 1:
                    # if not at the last CPU burst
                    io_time = current_process.burst_io[current_process.icount + 1]
                    current_process.icount += 2
                    queue_entry = total_time + io_time + cpu_burst
                    current_process.updateburst()
                    if queue_entry in queue:
                        # if another process enters the queue at the same time
                        queue[queue_entry].insert(len(queue[queue_entry]), current_process)
                        queue[queue_entry] = sorted(queue[queue_entry], key=lambda x: x.subscript)
                        # break ties by ordering by subscript/alphanumeric
                    else:
                        queue[queue_entry] = [current_process]
                else:
                    #time to calculate TT and WT
                    current_process.turnaround_time = total_time + cpu_burst - current_process.response_time
                    current_process.waiting_time = current_process.turnaround_time - sum(current_process.burst_io)
                total_time += cpu_burst
                # remove from queue
                queue.pop(i)
                # order queue by entry/re-entry time
                queue = dict(sorted(queue.items()))
                if len(queue) <= 0:
                    print('Current time:', total_time)
                    print('Processes in ready queue:', current_process.subscript)
                    print('Length of next CPU burst:', current_process.curr_burst)
                    print('Finished at ', total_time)
            else:
                # if multiple processes entered the queue at this time
                for process in current_process:
                    if process.icount == 0:
                        process.response_time = total_time
                    cpu_burst = process.burst_io[process.icount]
                    if process.icount < len(process.burst_io) - 1:
                        io_time = process.burst_io[process.icount + 1]
                        process.icount += 2
                        queue_entry = total_time + io_time + cpu_burst
                        process.updateburst()
                        if queue_entry in queue:
                            queue[queue_entry].insert(len(queue[queue_entry]), process)
                            queue[queue_entry] = sorted(queue[queue_entry], key=lambda x: x.subscript)
                        else:
                            queue[queue_entry] = [process]
                    else:
                        process.turnaround_time = total_time + cpu_burst - process.response_time
                        process.waiting_time = process.turnaround_time - sum(process.burst_io) + process.response_time
                    total_time += cpu_burst
                    queue = dict(sorted(queue.items()))
                queue.pop(i)
        i += 1
    print('All processes finished execution')
    print(str(round((total_time-idle_time)/total_time*100, 2)) + '% CPU utilization')


simulate_fcfs(processes_queue)

avg_wt = 0
avg_rt = 0
avg_tt = 0
for process in All_processes:
    avg_rt += process.response_time
    avg_wt += process.waiting_time
    avg_tt += process.turnaround_time
    print(process.subscript, 'response time:',process.response_time,', turnaround time:',process.turnaround_time,', waiting time:',process.waiting_time)
avg_tt = round(avg_tt/9, 2)
avg_wt = round(avg_wt/9, 2)
avg_rt = round(avg_rt/9, 2)
print('Averages\nresponse time:', avg_rt, ', turnaround time:', avg_tt, ', waiting time:', avg_wt)