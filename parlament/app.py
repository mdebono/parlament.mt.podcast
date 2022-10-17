from parlament import papi, pfeed

def run():
    #TODO: disabling calling actual URLs for now
    #sittings = papi.get_plenary_sittings()
    #audio_url = papi.get_audio_url(sittings[0])
    #print(audio_url)

    feed = pfeed.init_feed()
    feed.add_item(
        title="Hello",
        link="http://example.com",
        description="Testing."
    )
    pfeed.write_feed(feed, 'test.rss')