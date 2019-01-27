class Publisher(object):
    users = set()

    def register(self, user):
        self.users.add(user)

    def unregister(self, user):
        self.users.discard(user)

    def send_notification(self, message):
        for user in self.users:
            user.notify(message)


class Subscriber(object):
    def __init__(self, username):
        self.username = username

    def notify(self, message):
        print(self.username + " received message : " + message)


publisher = Publisher()

subscriber1 = Subscriber('Subscriber 1')
subscriber2 = Subscriber('Subscriber 2')

#register subscribers
publisher.register(subscriber1)
publisher.register(subscriber2)

#send notification to subscribers
publisher.send_notification("Message 1")
publisher.send_notification("Message 2")
