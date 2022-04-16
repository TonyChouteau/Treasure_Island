class Logger:

    __debug_mode = False

    @classmethod
    def debug_mode(cls, debug_mode):
        cls.__debug_mode = debug_mode

    @classmethod
    def debug(cls, **messages):
        if cls.__debug_mode:
            print(messages)
