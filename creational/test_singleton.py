import threading
import queue
from singleton import Singleton
from thread_safe_singleton import ThreadSafeSingleton


def test_singleton():
    instance_1 = Singleton()
    instance_2 = Singleton()

    assert instance_1 is instance_2


def test_tread_safe_singleton():
    number_of_threads = 10

    # Function to run in each threads and create an instance of our class and put them is a queue of all instances
    def create_instance(instances_queue: queue.Queue) -> None:
        instance = ThreadSafeSingleton()
        print(f"{threading.get_ident()} thread created a new instance")
        instances_queue.put(instance)

    # Create empty queue
    instances_queue = queue.Queue()

    # Create threads and put them inside a list
    threads = [
        threading.Thread(target=create_instance, args=(instances_queue,))
        for _ in range(number_of_threads)
    ]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Convert instances_queue to list to iterate over it
    instances_list = list(instances_queue.queue)
    print(instances_list)

    # Check all created instances are acctually the same
    main_instance = ThreadSafeSingleton()

    for instance in instances_list:
        assert instance is main_instance
