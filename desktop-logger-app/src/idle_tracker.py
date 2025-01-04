class IdleTracker:
    def __init__(self):
        self.idle_time = 0
        self.active = False

    def start_tracking(self):
        self.active = True
        self.idle_time = 0
        # Logic to monitor user activity and calculate idle time

    def stop_tracking(self):
        self.active = False
        # Logic to stop monitoring and finalize idle time

    def get_idle_time(self):
        return self.idle_time

    def reset_idle_time(self):
        self.idle_time = 0