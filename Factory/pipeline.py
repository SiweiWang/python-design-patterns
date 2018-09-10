from feature import Feature
from master import Master

class Pipeline (object):
    """
    a pipeline factory
    """
    def __init__(self, pipeline_factory=None):
      """pipeline_factory is the abstract factory."""
      self.pipeline_factory = pipeline_factory
    
    def build(self):
      """Building a pipeline """
      pipeline = self.pipeline_factory()
      print ("this is {}".format(pipeline))
      print (pipeline.build())

if __name__ == "__main__":
    pipeline = Pipeline(Feature)
    pipeline.build()
    pipeline = Pipeline(Master)
    pipeline.build()