"""
INTERFACE SEGREGATION PRINCIPLE - VIOLATED
Fat interface forces all classes to implement methods they don't need
"""

from abc import ABC, abstractmethod
from typing import List

# ❌ FAT INTERFACE - Too many responsibilities
class Worker(ABC):
    """Fat interface with too many methods"""
    
    @abstractmethod
    def work(self) -> None:
        pass
    
    @abstractmethod
    def eat(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass
    
    @abstractmethod
    def attend_meeting(self) -> None:
        pass
    
    @abstractmethod
    def write_report(self) -> None:
        pass
    
    @abstractmethod
    def manage_team(self) -> None:
        pass
    
    @abstractmethod
    def code_review(self) -> None:
        pass
    
    @abstractmethod
    def take_break(self) -> None:
        pass


# ❌ HumanWorker forced to implement all methods (ok - humans do all these)
class HumanWorker(Worker):
    def work(self):
        print("Human is working")
    
    def eat(self):
        print("Human is eating")
    
    def sleep(self):
        print("Human is sleeping")
    
    def attend_meeting(self):
        print("Human is attending meeting")
    
    def write_report(self):
        print("Human is writing report")
    
    def manage_team(self):
        print("Human is managing team")
    
    def code_review(self):
        print("Human is doing code review")
    
    def take_break(self):
        print("Human is taking break")


# ❌ RobotWorker forced to implement methods it doesn't need!
class RobotWorker(Worker):
    def work(self):
        print("Robot is working")
    
    def eat(self):
        # ❌ Robot doesn't eat! But forced to implement
        raise NotImplementedError("Robot doesn't eat!")
    
    def sleep(self):
        # ❌ Robot doesn't sleep! But forced to implement
        raise NotImplementedError("Robot doesn't sleep!")
    
    def attend_meeting(self):
        # ❌ Robot doesn't attend meetings!
        raise NotImplementedError("Robot doesn't attend meetings!")
    
    def write_report(self):
        print("Robot can write reports")
    
    def manage_team(self):
        # ❌ Robot doesn't manage teams!
        raise NotImplementedError("Robot doesn't manage teams!")
    
    def code_review(self):
        print("Robot can do code review")
    
    def take_break(self):
        # ❌ Robot doesn't take breaks!
        raise NotImplementedError("Robot doesn't take breaks!")


# ❌ InternWorker also forced to implement management methods
class InternWorker(Worker):
    def work(self):
        print("Intern is working")
    
    def eat(self):
        print("Intern is eating")
    
    def sleep(self):
        print("Intern is sleeping")
    
    def attend_meeting(self):
        print("Intern is attending meeting")
    
    def write_report(self):
        print("Intern is writing report")
    
    def manage_team(self):
        # ❌ Intern can't manage team!
        raise NotImplementedError("Intern can't manage team!")
    
    def code_review(self):
        # ❌ Intern can't do code review!
        raise NotImplementedError("Intern can't do code review!")
    
    def take_break(self):
        print("Intern is taking break")


# Client code that forces usage
class Company:
    def __init__(self, workers: List[Worker]):
        self.workers = workers
    
    def run_operations(self):
        for worker in self.workers:
            try:
                worker.work()
                worker.eat()  # ❌ This will fail for RobotWorker!
                worker.attend_meeting()  # ❌ This will fail for RobotWorker!
            except NotImplementedError as e:
                print(f"Error: {e}")


# Demonstration of ISP violation
if __name__ == "__main__":
    print("=== ISP VIOLATION EXAMPLE ===")
    print("\n❌ RobotWorker forced to implement human methods:")
    
    workers = [HumanWorker(), RobotWorker(), InternWorker()]
    company = Company(workers)
    company.run_operations()
    
    print("\n❌ PROBLEMS:")
    print("1. RobotWorker forced to implement eat(), sleep(), attend_meeting()")
    print("2. InternWorker forced to implement manage_team(), code_review()")
    print("3. Changes to Worker interface affect all subclasses")