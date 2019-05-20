import unittest
from app.models import Source 


class SourceTest(unittest.TestCase) :
  '''
  Test class to test the behaviour of the ources class
  '''

  def setUp(self) :
    '''
    Set up method that will run before every test 
    '''
    self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

  def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_source,Source))



if __name__ == '__main__' :
  unittest.main()
