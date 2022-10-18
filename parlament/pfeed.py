# Parlament Podcast Feed

from parlament.podcastfeed import PodcastFeed

def init_feed():
    return PodcastFeed(
        title="Il-Podcast tal-Parlament",
        link="https://parlament.mdebono.com/",
        description=u"Dan il-Podcast huwa kollezzjoni ...", # TODO: handle unicode "inuffiċjali tas-seduti tal-Parlament ta' Malta. Għalissa qed inpoġġu l-ewwel seduta ta' Ottubru 2022 u 'l quddiem inżidu seduti hekk kif jinħarġu mill-Parlament. Ċaħda: Dan il-Podcast mhux ikkontrollat mill-Parlament jew il-Gvern ta' Malta u mhu bl-ebda mod jipprova jirrappreżenta l-ebda minnhom.",
        language="mt",
        image_url = "https://parlament.mt/static-images/logo_small_menu.png",
        owner="parlament@mdebono.com",
        author="Il-Parlament ta' Malta",
        category="News & Politics",
    )

def write_feed(feed, filename):
    with open(filename, 'w') as fp:
        feed.write(fp, 'utf-8')
