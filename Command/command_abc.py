import abc

class AbsCommand(object):
    __metacalss__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass
