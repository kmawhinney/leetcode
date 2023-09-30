class Logger:

    def __init__(self):
        self.last_time = {} # message:last time printed

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_time:
            if timestamp - self.last_time[message] >= 10:
                self.last_time[message] = timestamp
                return True
            else:
                return False
        else:
            self.last_time[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
