
class Action:
    def __init__(self, function, *args, **kwargs):
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def execute(self):
        self._function(*self._args, **self._kwargs)

    def execute_and_return(self):
        return self._function(*self._args, **self._kwargs)

    def __eq__(self, other) -> bool:
        funciton_eq = self._function==other.function
        args_eq = self._args==other.args
        kwargs_eq = self._kwargs==other.kwargs
        return funciton_eq and args_eq and kwargs_eq

    def __str__(self):
        return 'Action for ' + self._function.__name__

    @property
    def function(self):
        return self._function
    
    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs