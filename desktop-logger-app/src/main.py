import datetime
import time
import ctypes
from ctypes import wintypes
import mysql.connector
from logger import Logger
from startup import add_to_startup
from idle_tracker import IdleTracker

print("Starting Desktop Logger Application...")

# MySQL connection setup
# ...existing code...
# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ganesh#1929",
    database="user_activity"
)
# ...existing code...
cursor = db.cursor()

def log_to_db(event, event_time):
    query = "INSERT INTO log_events (event, event_time) VALUES (%s, %s)"
    cursor.execute(query, (event, event_time))
    db.commit()

def main():
    logger = Logger()
    idle_tracker = IdleTracker()

    add_to_startup()
    
    login_time = datetime.datetime.now()
    logger.log_login(login_time)
    log_to_db("login", login_time)
    idle_tracker.start_tracking()

    user32 = ctypes.windll.user32
    WTS_SESSION_LOCK = 0x7
    WTS_SESSION_UNLOCK = 0x8

    def session_change_handler(dwSessionId, dwEventType):
        event_time = datetime.datetime.now()
        if dwEventType == WTS_SESSION_LOCK:
            logger.log_logout(event_time)
            log_to_db("lock", event_time)
        elif dwEventType == WTS_SESSION_UNLOCK:
            logger.log_login(event_time)
            log_to_db("unlock", event_time)

    WTSRegisterSessionNotification = user32.WTSRegisterSessionNotification
    WTSRegisterSessionNotification.argtypes = [wintypes.HWND, wintypes.DWORD]
    WTSRegisterSessionNotification.restype = wintypes.BOOL

    WTSUnRegisterSessionNotification = user32.WTSUnRegisterSessionNotification
    WTSUnRegisterSessionNotification.argtypes = [wintypes.HWND]
    WTSUnRegisterSessionNotification.restype = wintypes.BOOL

    try:
        while True:
            # Main application loop
            print("Application is running...")
            time.sleep(5)  # Sleep for 5 seconds to simulate work
    except KeyboardInterrupt:
        idle_tracker.stop_tracking()
        logout_time = datetime.datetime.now()
        logger.log_logout(logout_time)
        log_to_db("logout", logout_time)
        print("Application has stopped.")
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()