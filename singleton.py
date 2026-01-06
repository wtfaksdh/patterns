class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message: str):
        print(f"LOG: {message}")


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Singleton работает1")
    logger2.log("Singleton работает2")

    print(logger1 is logger2)
