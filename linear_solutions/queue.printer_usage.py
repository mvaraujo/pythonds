import random
from linear import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time, max_pages):
        self.time_stamp = time
        self.pages = random.randrange(1, max_pages + 1)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def simulation(num_seconds, pages_per_minute, max_pages, seconds_till_new_task):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task(seconds_till_new_task):
            task = Task(current_second, max_pages)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = 0 if len(waiting_times) == 0 else sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def new_print_task(seconds_till_new_task):
    return random.randrange(1, seconds_till_new_task + 1) == seconds_till_new_task


run_window = 3600  # one hour
ppm = 5
max_pages = 20
seconds_till_new_task = 180

for i in range(10):
    simulation(run_window, ppm, max_pages, seconds_till_new_task)
