class Route:

    def __init__(self):
        # Define all routes
        self.route = {
            "hello": self.hello,
            "test": self.test
        }

    # Check the availability of the route
    def exists(self, event_type):
        return True if self.route.get(event_type) else False

    # Handle route access
    def handle(self, event_type, event):
        if self.exists(event_type):
            self.route.get(event_type)(event)

    # Routes
    @staticmethod
    def hello(message):
        print(message)

    @staticmethod
    def test(message):
        print(message)
