from queue import Queue
import random

queue = Queue()


def generate_request(req_id):
    queue.put(req_id)
    return f"Request № {req_id} added to queue"


def process_request():
    if not queue.empty():
        request_processing = queue.get()
        return f"Request # {request_processing} accepted for processing"
    else:
        return "Queue is empty"


request_id = 0
while request_id < 100:
# while True:
    rand = random.randint(0, 1)
    if rand == 1:
        print(generate_request(request_id))
        request_id += 1
    else:
        print(process_request())
