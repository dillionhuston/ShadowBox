import datetime

class Logger:
    """Use for logging."""
    @staticmethod
    def _get_utc_time() -> str:
        return datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def Log(message: str):
        print(f"[{Logger._get_utc_time()} UTC]: {message}")

    @staticmethod
    def LogWarning(message: str):
        print(f"[{Logger._get_utc_time()} UTC] - Warning: {message}")

    @staticmethod
    def LogError(message: str):
        print(f"[{Logger._get_utc_time()} UTC] - Error: {message}")