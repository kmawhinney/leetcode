class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        # sort by contents if possible - x.split()[1:]
        # otherwise, sort by identifier - x.split()[0]
        letter_logs.sort(key = lambda x:(x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs
