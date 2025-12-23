import time
from plyer import notification
while(True):
    notification.notify(title="please drink some water",
                        message="its been an hour please drink some water!!!!")
    time.sleep(60*60)