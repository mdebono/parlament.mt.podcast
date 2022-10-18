from parlament import papi, pfeed

def run():
    #TODO: disabling calling actual URLs for now
    leg = papi.get_leg()
    sittings = papi.get_plenary_sittings(leg)
    #sitting = sittings[0]

    feed = pfeed.init_feed()
    for sitting in sittings:
        pfeed.add_item(feed,
            title = papi.get_episode_title(leg, sitting),
            url = papi.get_sitting_audio_url(sitting),
            description = papi.get_episode_description(leg, sitting),
            pubdate = papi.get_sitting_date(sitting),
        )
    pfeed.write_feed(feed, 'test.rss')