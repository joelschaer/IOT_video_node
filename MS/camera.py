import threading

class Camera(threading.Thread):

  def __init__(self):
    self.t_before
    self.t_after
    self.buffer_name

  def run(self):
    if("stop" == True):
      pass
    #call to script(t_before, t_after)

  def restart(self, t_before, t_after):
    pass

  def record(self):
    return 'filename_timestamp'