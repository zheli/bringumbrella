import urllib2
import json

# Setting this for future use
API_VERSION = '1.0'

URL = 'http://api.wunderground.com/api'


FEATURES_STRATUS = (
    'autocomplete',
    'astronomy',
    'conditions',
    'forecast',
    'geolookup',
)

FEATURES_CUMULUS = FEATURES_STRATUS + (
    'forecast7day',
    'hourly',
    'satellite',
    'radar',
    'alerts',
)

FEATURES_ANVIL = FEATURES_CUMULUS + (
    'hourly7day',
    'yesterday',
    'webcams',
)

ADD_ONS = 'history'

FEATURES = (
    'geolookup',
    'conditions',
    'forecast',
    'astronomy',
    'radar',
    'satellite',
    'webcams',
    'history',
    'alerts',
    'hourly',
    'hourly7day',
    'forecast7day',
    'yesterday',
    'autocomplete',
)


class WeatherException(Exception): pass
class WeatherInvalidFeature(WeatherException): pass
class WeatherServerException(WeatherException): pass


class Client(object):

    def __init__(self, key, api_version=API_VERSION, timeout=None):
        self.key = key
        self.api_version = api_version
        self.timeout = timeout


    def request(self,features=[], location=''):

        feature_string = "/".join(features)
        uri = '%s/%s/%s/q/%s.json' % (URL, self.key, feature_string, location)

        response = urllib2.urlopen(uri,timeout=self.timeout)
        data = response.read()

        return json.loads(data)
        #return Struct(**json.loads(data))

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def repr__(self):
        return '<%s>' % str('\n'.join('%s: %s' % (k, repr(v)) for (k,v) in self.__dict.iterithems()))


__all__ = ['Client', 'WeatherException', 'WeatherInvalidFeature', 'WeatherServerException']
