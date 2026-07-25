import asyncio
from abc import ABC, abstractmethod
from typing import Set


class AsyncObserver(ABC):
    @abstractmethod
    async def update(self, event_data: str) -> None:
        pass


class AsyncSubject:
    def __init__(self) -> None:
        self._observers: Set[AsyncObserver] = set()

    def attach(self, observer: AsyncObserver) -> None:
        self._observers.add(observer)

    def detach(self, observer: AsyncObserver) -> None:
        self._observers.discard(observer)

    async def notify(self, event_data: str) -> None:
        if not self._observers:
            return

        # Fire all observer updates concurrently
        tasks = [
            asyncio.create_task(self._safe_update(observer, event_data))
            for observer in self._observers
        ]
        await asyncio.gather(*tasks)

    async def _safe_update(self, observer: AsyncObserver, event_data: str) -> None:
        """Wrapper to prevent one failing observer from breaking others."""
        try:
            await observer.update(event_data)
        except Exception as e:
            print(f"[Async Error] Observer failed: {e}")


# --- Concrete Observers performing I/O ---
class DatabaseWriter(AsyncObserver):
    async def update(self, event_data: str) -> None:
        await asyncio.sleep(0.5)  # Simulate DB write overhead
        print(f"[DB Writer] Saved '{event_data}' to database.")


class EmailNotifier(AsyncObserver):
    async def update(self, event_data: str) -> None:
        await asyncio.sleep(0.2)  # Simulate network latency
        print(f"[Email Notifier] Email sent for '{event_data}'.")


async def main():
    subject = AsyncSubject()
    db_writer = DatabaseWriter()
    email_notifier = EmailNotifier()

    subject.attach(db_writer)
    subject.attach(email_notifier)

    print("--- Triggering Notification 1 ---")
    # Both database write and email send happen concurrently
    await subject.notify("User Account Created")

    print("\n--- Detaching Email Notifier ---")
    subject.detach(email_notifier)

    print("--- Triggering Notification 2 ---")
    await subject.notify("User Password Changed")


if __name__ == "__main__":
    asyncio.run(main())