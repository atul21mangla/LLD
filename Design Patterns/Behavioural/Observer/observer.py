from abc import ABC, abstractmethod
from typing import List


# -------------------------------------------------------------------
# 1. Observer Interface
# -------------------------------------------------------------------
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float) -> None:
        """Called by the Subject when its state changes."""
        pass


# -------------------------------------------------------------------
# 2. Subject Interface
# -------------------------------------------------------------------
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Register an observer."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Unregister an observer."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all registered observers."""
        pass


# -------------------------------------------------------------------
# 3. Concrete Subject
# -------------------------------------------------------------------
class WeatherStation(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def set_measurements(self, temperature: float, humidity: float) -> None:
        """Simulates new weather readings and triggers notifications."""
        self._temperature = temperature
        self._humidity = humidity
        self.notify()


# -------------------------------------------------------------------
# 4. Concrete Observers
# -------------------------------------------------------------------
class PhoneDisplay(Observer):
    def update(self, temperature: float, humidity: float) -> None:
        print(f"[Phone Display] Temp: {temperature}°C | Humidity: {humidity}%")


class WebDashboard(Observer):
    def update(self, temperature: float, humidity: float) -> None:
        print(f"[Web Dashboard] Updated — Temp: {temperature}°C")


# -------------------------------------------------------------------
# Client Code Demonstration
# -------------------------------------------------------------------
if __name__ == "__main__":
    weather_station = WeatherStation()

    phone = PhoneDisplay()
    dashboard = WebDashboard()

    # Register observers
    weather_station.attach(phone)
    weather_station.attach(dashboard)

    print("--- First Weather Update ---")
    weather_station.set_measurements(25.5, 60.0)

    # Detach phone display
    weather_station.detach(phone)

    print("\n--- Second Weather Update (Phone detached) ---")
    weather_station.set_measurements(28.0, 55.0)