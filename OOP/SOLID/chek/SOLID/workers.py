from abc import ABC, abstractmethod


class BasicWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(BasicWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BasicWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class UltimateWorker(BasicWorker):

    @staticmethod
    def work():
        print("working 24/7")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BasicWorker):
            raise AssertionError(f"`worker` must subclass of type {BasicWorker}")  # this is adopted to python 3

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = UltimateWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")