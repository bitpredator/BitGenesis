from bitgenesis.identity.manager import IdentityManager


class IdentityQuery:

    def __init__(self, manager=None):

        self.manager = manager or IdentityManager()

    def profile(self):

        return self.manager.get()

    def field(self, name):

        profile = self.manager.get()

        return getattr(profile, name, None)

    def as_dict(self):

        return self.manager.as_dict()