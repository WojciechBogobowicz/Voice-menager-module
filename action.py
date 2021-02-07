
class Action:
    def __init__(self, fucntion, *args, **kwargs):
        self.fucntion = fucntion
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        self.fucntion(*self.args, **self.kwargs)

    def execute_and_return(self):
        return self.fucntion(*self.args, **self.kwargs)

    def __eq__(self, other) -> bool:
        funciton_eq = self.fucntion==other.fucntion
        args_eq = self.args==other.args
        kwargs_eq = self.kwargs==other.kwargs
        return funciton_eq and args_eq and kwargs_eq

    def __str__(self):
        return 'Action for ' + self.fucntion.__name__