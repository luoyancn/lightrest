from pecan import hooks

class ConfigHook(hooks.PecanHook):

    def __init__(self, cfg):
        self.cfg = cfg

    def before(self, state):
        state.request.cfg = self.cfg
