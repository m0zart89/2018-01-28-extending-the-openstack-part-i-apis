class Thing:
    def __init__(self, validator):
        self.v = validator

    def list_things(self):
        # We could use the validator to check what project the user is authenticated against,
        # or to check if the user has different roles applied
        return { 'things': ['apple', 'chair', 'banana', 'television'] }

