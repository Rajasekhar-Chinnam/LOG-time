class Logger:
    def __init__(self):
        self.login_times = []
        self.logout_times = []
        self.idle_times = []

    def log_login(self, login_time):
        self.login_times.append(login_time)
        print(f"Login Time: {login_time}")

    def log_logout(self, logout_time):
        self.logout_times.append(logout_time)
        print(f"Logout Time: {logout_time}")

    def log_idle_time(self, idle_time):
        self.idle_times.append(idle_time)
        print(f"Idle Time: {idle_time}")