# Parlament API

from datetime import datetime
import json, pytz, babel.dates

from parlament import cache

LEGISLATURE_ID = '506899'
PARLAMENT_URL = 'https://parlament.mt'
PARLAMENT_MEDIA_ARCHIVE_URL = PARLAMENT_URL + '/en/menues/reference-material/archives/media-archive/'
PARLAMENT_MEDIA_ARCHIVE_API_URL = PARLAMENT_URL + '/umbraco/Api/MediaArchiveApi/GetMediaForLegislature/?lang=mt&legislatureId=' + LEGISLATURE_ID

def get_leg():
    leg_string = cache.httpPost(PARLAMENT_MEDIA_ARCHIVE_API_URL, None, None).content
    return json.loads(leg_string)

def get_leg_title(leg, lang='mt'):
    if lang == 'mt':
        return leg["TitleMT"]
    elif lang == 'en':
        return leg["Title"]
    else:
        raise Exception('unknown language ' + lang)

def get_leg_number(leg):
    return leg['Number']

def get_plenary_sittings(leg):
    # TODO: get Sittings of CommitteeType=Plenary
    return leg["Committees"][0]["Sittings"]

def get_sitting_audio_url(sitting):
    # TODO: get Url of IsVideo=false
    return PARLAMENT_URL + sitting["Media"][0]["Url"]

def get_sitting_title(sitting):
    return sitting["Title"]

def get_sitting_number(sitting):
    return sitting["Number"]

def get_sitting_date(sitting):
    local = pytz.timezone('Europe/Malta')
    naive = datetime.fromisoformat(sitting["Date"])
    local_dt = local.localize(naive)
    return local_dt

def get_episode_title(leg, sitting):
    text = '{title} S{season:02}E{episode:03}'
    return text.format(
        title = get_sitting_title(sitting),
        season = get_leg_number(leg),
        episode = get_sitting_number(sitting),
    )

def get_episode_description(leg, sitting):
    text = '{leg_title} Seduta Nru: {episode:03} - {date}'
    date = get_sitting_date(sitting)
    return text.format(
        leg_title = get_leg_title(leg),
        episode = get_sitting_number(sitting),
        date = babel.dates.format_datetime(datetime=date, format='full', locale='mt'), # TODO: remove timezone and add AM/PM
    )
