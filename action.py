
class Action:
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def execute(self):
        self._func(*self._args, **self._kwargs)

    def execute_and_return(self):
        return self._func(*self._args, **self._kwargs)

    def __eq__(self, other) -> bool:
        funciton_eq = self._func==other.func
        args_eq = self._args==other.args
        kwargs_eq = self._kwargs==other.kwargs
        return funciton_eq and args_eq and kwargs_eq

    def __str__(self):
        return 'Action for ' + self._func.__name__

    @property
    def func(self):
        return self._func
    
    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs