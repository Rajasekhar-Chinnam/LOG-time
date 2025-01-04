import datetime
print("Starting Desktop Logger Application...")

from logger import Logger
from startup import add_to_startup
from idle_tracker import IdleTracker

def main():
    logger = Logger()
    idle_tracker = IdleTracker()

    add_to_startup()
    
    login_time = datetime.datetime.now()
    logger.log_login(login_time)
    idle_tracker.start_tracking()

    try:
        while True:
            # Main application loop
            pass
    except KeyboardInterrupt:
        idle_tracker.stop_tracking()
        logout_time = datetime.datetime.now()
        logger.log_logout(logout_time)

if __name__ == "__main__":
    main()