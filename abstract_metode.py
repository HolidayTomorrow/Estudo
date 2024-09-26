from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message: str | None):
        self.message: str | None = message
        
    @abstractmethod
    def send(self) -> bool: ...
    
class NotificationEmail(Notification):
    def send(self) -> bool:
        print('E-mail: sending - ', self.message)
        return True
    
    
class NotificationSMS(Notification):
    def send(self) -> bool:
        print('SMS: sending - ', self.message)
        return True
    
def notification(notification: Notification):
    notification_sending = notification.send()
    
    if notification_sending:
        print('Notification send')
    else:
        print('Notification not send')
        
notify = NotificationEmail('Hello World!')
notification(notify)