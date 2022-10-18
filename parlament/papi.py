# Parlament API

import json

from parlament import cache

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