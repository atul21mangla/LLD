from abc import ABC, abstractmethod
from typing import Set
import threading
import time


class Observer(ABC):
    @abstractmethod
    def update(self, event_data: str) -> None:
        pass


class ThreadSafeSubject:
    def __init__(self) -> None:
        self._observers: Set[Observer] = set()
        # RLock allows re-entrant calls from the same thread without deadlocking
        self._lock = threading.RLock()

    def attach(self, observer: Observer) -> None:
        with self._lock:
            self._observers.add(observer)

    def detach(self, observer: Observer) -> None:
        with self._lock:
            self._observers.discard(observer)

    def notify(self, event_data: str) -> None:
        # Take a snapshot of observers under lock to avoid holding the lock
        # while executing external observer code.
        with self._lock:
            observers_snapshot = list(self._observers)

        # Notify outside the lock critical section to prevent deadlocks
        for observer in observers_snapshot:
            try:
                observer.update(event_data)
            except Exception as e:
                print(f"[Error] Observer failed: {e}")


# --- Concrete Example ---
class AuditLogger(Observer):
    def update(self, event_data: str) -> None:
        print(f"[{threading.current_thread().name}] Logging event: {event_data}")


class AlertService(Observer):
    def update(self, event_data: str) -> None:
        print(f"[{threading.current_thread().name}] Alerting on: {event_data}")


if __name__ == "__main__":
    subject = ThreadSafeSubject()
    subject.attach(AuditLogger())
    subject.attach(AlertService())

    # Simulate multi-threaded state updates
    def worker(worker_id: int):
        for i in range(2):
            subject.notify(f"Worker {worker_id} payload {i}")
            time.sleep(0.01)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()