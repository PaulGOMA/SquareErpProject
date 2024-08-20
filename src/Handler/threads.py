import sys
sys.path.append

import threading

# :::::::::::::::::::::::::::::::::::::::::::::::::::: Thread manager ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ThreadManager:
    def __init__(self):
        self.threads = []
        self.stop_events = []
        self.thread_labels = []

    def add_thread(self, target, label=None, daemon=True, use_stop_event=False, *args, **kwargs):
        if use_stop_event:
            stop_event = threading.Event()
            thread_args = args + (stop_event,)
            self.stop_events.append(stop_event)
        else:
            stop_event = None
            thread_args = args
            self.stop_events.append(None)  # Stocker None pour les threads sans stop event

        thread = threading.Thread(target=target, args=thread_args, kwargs=kwargs)
        thread.daemon = daemon  # Définit si le thread est un daemon
        self.threads.append(thread)
        self.thread_labels.append(label)

    def start_thread_by_index(self, index):
        if 0 <= index < len(self.threads) and not self.threads[index].is_alive():
            self.threads[index].start()

    def stop_thread_by_index(self, index):
        if 0 <= index < len(self.threads):
            event = self.stop_events[index]
            if event:
                event.set()
            self.threads[index].join()

    def start_thread_by_label(self, label):
        for index, thread_label in enumerate(self.thread_labels):
            if thread_label == label:
                self.start_thread_by_index(index)

    def stop_thread_by_label(self, label):
        for index, thread_label in enumerate(self.thread_labels):
            if thread_label == label:
                self.stop_thread_by_index(index)

    def clear_threads(self):
        self.threads = []
        self.stop_events = []
        self.thread_labels = []

    def wait_for_all(self):
        for thread in self.threads:
            thread.join()

    def start_all(self):
        for thread in self.threads:
            if not thread.is_alive():
                thread.start()

    def stop_all(self):
        for event in self.stop_events:
            event.set()
        self.wait_for_all()