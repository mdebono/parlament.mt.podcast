import json

from parlament import cache
from parlament.podcastfeed import PodcastFeed

LEGISLATURE = '14'
LEGISLATURE_ID = '506899'
PARLAMENT_URL = 'https://parlament.mt'
PARLAMENT_MEDIA_ARCHIVE_URL = PARLAMENT_URL + '/en/menues/reference-material/archives/media-archive/'
PARLAMENT_MEDIA_ARCHIVE_API_URL = PARLAMENT_URL + '/umbraco/Api/MediaArchiveApi/GetMediaForLegislature/?lang=mt&legislatureId=' + LEGISLATURE_ID

def get_plenary_sittings():
    media_string = cache.httpPost(PARLAMENT_MEDIA_ARCHIVE_API_URL, None, None).content
    media = json.loads(media_string)
    # TODO: get Sittings of CommitteeType=Plenary
    return media["Committees"][0]["Sittings"]

def get_audio_url(sitting):
    # TODO: get Url of IsVideo=false
    return PARLAMENT_URL + sitting["Media"][0]["Url"]

def get_title(sitting):
    return sitting["Title"]

def get_number(sitting):
    return sitting["Number"]

def run():
    sittings = get_plenary_sittings()
    audio_url = get_audio_url(sittings[0])
    print(audio_url)
    feed = PodcastFeed(
        title="Il-Podcast tal-Parlament",
        link="https://parlament.mdebono.com/",
        description=u"Dan il-Podcast huwa kollezzjoni ...", # TODO: handle unicode "inuffiċjali tas-seduti tal-Parlament ta' Malta. Għalissa qed inpoġġu l-ewwel seduta ta' Ottubru 2022 u 'l quddiem inżidu seduti hekk kif jinħarġu mill-Parlament. Ċaħda: Dan il-Podcast mhux ikkontrollat mill-Parlament jew il-Gvern ta' Malta u mhu bl-ebda mod jipprova jirrappreżenta l-ebda minnhom.",
        language="mt",
        image_url = "https://parlament.mt/static-images/logo_small_menu.png",
        owner="parlament@mdebono.com",
        author="Il-Parlament ta' Malta",
        category="News & Politics",
    )
    feed.add_item(
        title="Hello",
        link="http://example.com",
        description="Testing."
    )
    with open('test.rss', 'w') as fp:
        feed.write(fp, 'utf-8')
