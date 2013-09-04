
class FakeSignal():
  """
  FakeSignal implements the methods of the signal class that 
  AppScale uses in the AppControllerClient class. The reason we
  have a FakeSignal class is because signal can only run on the
  main thread, and AppScake does not run the AppScale tools on 
  the main thread.  
  """  
  SIGALRM = 1

  @staticmethod
  def alarm(arg1):

  @staticmethod
  def signal(arg1, arg2):
