from abc import ABC, abstractmethod
from servicable import Servicable


class Battery(Servicable):
    def __init__(self) -> None:
        pass
    
    def needs_service(self):
        return self.needs_service()
    
    
    
class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if self.current_date is not None and service_threshold_date < self.current_date:
            return True
        
        return False
    
    
class SplindlerBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        print(self.last_service_date)
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        print(service_threshold_date, self.current_date, 'battery')
        if self.current_date is not None and service_threshold_date < self.current_date:
            return True
        else:
            return False