import sys
sys.path.append("..")

import threading

# :::::::::::::::::::::::::::::::::::::::::::::::::::: Thread manager ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ThreadManager:
    def __init__(self):
        self.threads = []
        self.stopEvents = []
        self.threadLabels = []

    def addThread(self, target, label=None, daemon=True, useStopevent=False, *args, **kwargs):
        if useStopevent:
            stopEvent = threading.Event()
            threadArgs = args + (stopEvent,)
            self.stopEvents.append(stopEvent)
        else:
            stopEvent = None
            threadArgs = args
            self.stopEvents.append(None)  # Stocker None pour les threads sans stop event

        thread = threading.Thread(target=target, args=threadArgs, kwargs=kwargs)
        thread.daemon = daemon  # Définit si le thread est un daemon
        self.threads.append(thread)
        self.threadLabels.append(label)

    def startThreadByIndex(self, index):
        if 0 <= index < len(self.threads) and not self.threads[index].is_alive():
            self.threads[index].start()

    def stopThreadByIndex(self, index):
        if 0 <= index < len(self.threads):
            event = self.stopEvents[index]
            if event:
                event.set()
            self.threads[index].join()

    def startThreadByLabel(self, label):
        for index, thread_label in enumerate(self.threadLabels):
            if thread_label == label:
                self.startThreadByIndex(index)

    def stopThreadByLabel(self, label):
        for index, thread_label in enumerate(self.threadLabels):
            if thread_label == label:
                self.stopThreadByIndex(index)

    def clearThreads(self):
        self.threads = []
        self.stopEvents = []
        self.threadLabels = []

    def waitForAll(self):
        for thread in self.threads:
            thread.join()

    def startAll(self):
        for thread in self.threads:
            if not thread.is_alive():
                thread.start()

    def stopAll(self):
        for event in self.stopEvents:
            event.set()
        self.waitForAll()