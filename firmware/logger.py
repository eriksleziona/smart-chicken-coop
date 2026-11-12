# Logging helper for the controller. This keeps all output consistent.

import utime


class Logger:
    def __init__(self, name="coop"):
        self.name = name

    def _stamp(self):
        return utime.localtime()

    def log(self, level, message):
        stamp = self._stamp()
        print("[%s] %04d-%02d-%02d %02d:%02d:%02d %s %s" % (
            self.name,
            stamp[0], stamp[1], stamp[2],
            stamp[3], stamp[4], stamp[5],
            level,
            message,
        ))

    def info(self, message):
        self.log("INFO", message)

    def warn(self, message):
        self.log("WARN", message)

    def error(self, message):
        self.log("ERROR", message)

    def debug(self, message):
        self.log("DEBUG", message)
