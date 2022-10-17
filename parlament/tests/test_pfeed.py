import unittest

from parlament import pfeed

class TestParlamentFeed(unittest.TestCase):

    def test_init_feed(self):
        feed = pfeed.init_feed()
        self.assertEqual(feed.feed['title'], 'Il-Podcast tal-Parlament')

if __name__ == '__main__':
    unittest.main()