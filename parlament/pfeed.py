# Parlament Podcast Feed

from parlament.podcastfeed import PodcastFeed
from feedgenerator import Enclosure

from lxml import etree

UTF8 = 'utf8'

def init_feed():
    return PodcastFeed(
        title="Il-Podcast tal-Parlament",
        link="https://parlament.mdebono.com/",
        description=u"Dan il-Podcast huwa kollezzjoni inuffiċjali tas-seduti tal-Parlament ta' Malta. Għalissa qed inpoġġu l-ewwel seduta ta' Ottubru 2022 u 'l quddiem inżidu seduti hekk kif jinħarġu mill-Parlament. Ċaħda: Dan il-Podcast mhux ikkontrollat mill-Parlament jew mill-Gvern ta' Malta u mhu bl-ebda mod jipprova jirrappreżenta l-ebda minnhom.",
        language="mt",
        image_url = "https://parlament.mt/static-images/logo_small_menu.png",
        owner="parlament@mdebono.com",
        author="Il-Parlament ta' Malta",
        category="News & Politics",
    )

def add_item(feed, title, description, link, audio_url, duration=None, pubdate=None):
    feed.add_item(
        title=title,
        description=description,
        link=link,
        enclosure=Enclosure(url=audio_url, length='', mime_type="audio/mpeg"),
        duration=duration,
        pubdate=pubdate,
    )

def write_feed(feed, filename):
    tmp_filename = filename + '.tmp'
    with open(tmp_filename, 'w', encoding=UTF8) as fp:
        feed.write(fp, UTF8)
    tree = etree.parse(tmp_filename)
    tree.write(filename, encoding=UTF8, pretty_print=True)
