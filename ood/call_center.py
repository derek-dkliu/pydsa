from enum import Enum
from collections import deque
import random
import time

class Rank(Enum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2

class CallCenter:
    def __init__(self, r, m, d):
        self.callqueue = deque()
        self.employees = []
        self.employees.append([Respondent(self) for _ in range(r)])
        self.employees.append([Manager(self) for _ in range(m)])
        self.employees.append([Director(self) for _ in range(d)])

    def add_call(self, call):
        self.callqueue.append(call)

    def dispatch_call(self):
        while self.callqueue:
            call = self.callqueue.popleft()
            employee = self.find_available_employee(call)
            if employee is not None:
                employee.receive_call(call)
            else:
                print("line is busy")
                self.add_call(call)
            time.sleep(.5)
    
    def find_available_employee(self, call):
        for employee in self.employees[call.get_rank()]:
            if employee.isfree():
                return employee
        return None

class Call:
    def __init__(self, caller):
        self.caller = caller
        self.duration = random.randint(1, 60)
        self.rank = Rank.RESPONDENT

    def increment_rank(self):
        if self.is_for_respondent():
            self.rank = Rank.MANAGER
        elif self.is_for_manager():
            self.rank = Rank.DIRECTOR

    def get_rank(self):
        return self.rank.value

    def is_for_respondent(self):
        return self.rank is Rank.RESPONDENT

    def is_for_manager(self):
        return self.rank is Rank.MANAGER

    def is_for_director(self):
        return self.rank is Rank.DIRECTOR

    def __str__(self):
        return f"call from {self.caller}"

class Employee:
    def __init__(self, center):
        self.call = None
        self.center = center
    
    def isfree(self):
        return self.call == None

    def receive_call(self, call):
        self.call = call
        print(f"received {call}")

    def finish_call(self):
        self.call = None
    
    def escalate_call(self):
        self.call.increment_rank()
        self.center.add_call(self.call)
        self.finish_call()

class Respondent(Employee):
    pass

class Manager(Employee):
    pass

class Director(Employee):
    pass

center = CallCenter(20, 5, 2)
for i in range(30):
    call = Call('caller-' + str(i))
    center.add_call(call)

center.dispatch_call()