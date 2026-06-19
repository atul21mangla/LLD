"""
INTERFACE SEGREGATION PRINCIPLE - COMPLIANT
Small, focused interfaces for specific behaviors
"""

from abc import ABC, abstractmethod
from typing import List

# ✅ SEGREGATED INTERFACES - Each has single responsibility
class Workable(ABC):
    """Interface for work behavior"""
    @abstractmethod
    def work(self) -> None:
        pass

class Eatable(ABC):
    """Interface for eating behavior"""
    @abstractmethod
    def eat(self) -> None:
        pass

class Sleepable(ABC):
    """Interface for sleeping behavior"""
    @abstractmethod
    def sleep(self) -> None:
        pass

class MeetingAttendable(ABC):
    """Interface for meeting attendance"""
    @abstractmethod
    def attend_meeting(self) -> None:
        pass

class ReportWritable(ABC):
    """Interface for report writing"""
    @abstractmethod
    def write_report(self) -> None:
        pass

class TeamManageable(ABC):
    """Interface for team management"""
    @abstractmethod
    def manage_team(self) -> None:
        pass

class CodeReviewable(ABC):
    """Interface for code review"""
    @abstractmethod
    def code_review(self) -> None:
        pass

class BreakTakable(ABC):
    """Interface for taking breaks"""
    @abstractmethod
    def take_break(self) -> None:
        pass


# ✅ HumanWorker implements only what humans do (all interfaces)
class HumanWorker(Workable, Eatable, Sleepable, MeetingAttendable, 
                  ReportWritable, TeamManageable, CodeReviewable, BreakTakable):
    def work(self):
        print("👨 Human is working")
    
    def eat(self):
        print("👨 Human is eating")
    
    def sleep(self):
        print("👨 Human is sleeping")
    
    def attend_meeting(self):
        print("👨 Human is attending meeting")
    
    def write_report(self):
        print("👨 Human is writing report")
    
    def manage_team(self):
        print("👨 Human is managing team")
    
    def code_review(self):
        print("👨 Human is doing code review")
    
    def take_break(self):
        print("👨 Human is taking break")


# ✅ RobotWorker implements ONLY what robots can do
class RobotWorker(Workable, ReportWritable, CodeReviewable):
    """Robot only implements work, reports, and code review"""
    
    def work(self):
        print("🤖 Robot is working")
    
    def write_report(self):
        print("🤖 Robot is writing report")
    
    def code_review(self):
        print("🤖 Robot is doing code review")
    
    # No eat(), sleep(), attend_meeting(), manage_team(), take_break()
    # This is fine because Robot doesn't need these!


# ✅ InternWorker implements only intern-appropriate interfaces
class InternWorker(Workable, Eatable, Sleepable, MeetingAttendable, 
                   ReportWritable, BreakTakable):
    """Intern doesn't manage team or do code reviews"""
    
    def work(self):
        print("👨‍🎓 Intern is working")
    
    def eat(self):
        print("👨‍🎓 Intern is eating")
    
    def sleep(self):
        print("👨‍🎓 Intern is sleeping")
    
    def attend_meeting(self):
        print("👨‍🎓 Intern is attending meeting")
    
    def write_report(self):
        print("👨‍🎓 Intern is writing report")
    
    def take_break(self):
        print("👨‍🎓 Intern is taking break")
    
    # No manage_team() or code_review() - Intern doesn't do these!


# ✅ Client code that depends on specific interfaces
class Company:
    """Company depends only on Workable interface"""
    
    def __init__(self, workers: List[Workable]):
        self.workers = workers
    
    def make_workers_work(self):
        """Only requires Workable interface"""
        print("\n--- Making all workers work ---")
        for worker in self.workers:
            worker.work()


class Cafeteria:
    """Cafeteria depends only on Eatable interface"""
    
    def __init__(self, eaters: List[Eatable]):
        self.eaters = eaters
    
    def serve_lunch(self):
        """Only requires Eatable interface"""
        print("\n--- Serving lunch ---")
        for eater in self.eaters:
            eater.eat()


class MeetingRoom:
    """MeetingRoom depends only on MeetingAttendable interface"""
    
    def __init__(self, attendees: List[MeetingAttendable]):
        self.attendees = attendees
    
    def conduct_meeting(self):
        """Only requires MeetingAttendable interface"""
        print("\n--- Conducting meeting ---")
        for attendee in self.attendees:
            attendee.attend_meeting()


class CodeReviewSession:
    """Code review depends only on CodeReviewable interface"""
    
    def __init__(self, reviewers: List[CodeReviewable]):
        self.reviewers = reviewers
    
    def conduct_review(self):
        """Only requires CodeReviewable interface"""
        print("\n--- Conducting code review ---")
        for reviewer in self.reviewers:
            reviewer.code_review()


# Demonstration
if __name__ == "__main__":
    print("=== ISP COMPLIANT EXAMPLE ===")
    
    # Create workers
    human = HumanWorker()
    robot = RobotWorker()
    intern = InternWorker()
    
    # Each service uses only the interfaces it needs
    company = Company([human, robot, intern])
    company.make_workers_work()
    
    cafeteria = Cafeteria([human, intern])  # Robot doesn't eat!
    cafeteria.serve_lunch()
    
    meeting_room = MeetingRoom([human, intern])  # Robot doesn't attend meetings!
    meeting_room.conduct_meeting()
    
    code_review = CodeReviewSession([human, robot])  # Intern doesn't review code!
    code_review.conduct_review()
    
    print("\n✅ BENEFITS:")
    print("1. Robot doesn't implement eat(), sleep(), attend_meeting()")
    print("2. Intern doesn't implement manage_team(), code_review()")
    print("3. Clients depend only on methods they actually use")
    print("4. Easy to add new worker types with specific capabilities")