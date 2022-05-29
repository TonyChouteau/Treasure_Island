class Logger:

    __debug_mode = False

    @classmethod
    def debug_mode(cls, debug_mode):
        cls.__debug_mode = debug_mode

    @classmethod
    def debug(cls, *messages, tag=None):
        formatted_tag = (' (' + tag + ')') if tag is not None else ''
        if cls.__debug_mode:
            print(f"LOGGER{formatted_tag}: {messages}")
