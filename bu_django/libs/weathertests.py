from .. import local_settings
import weather
import unittest

KEY = local_settings.WEATHERUNDERGROUND_API_KEY or ''
LOCATION = '57.659056,11.918264'

class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.client = weather.Client(key=KEY)

    def test_conditions(self):
        response = self.client.request(features=['conditions'], location=LOCATION)
        self.assertIsNotNone(response)

    def test_hourly(self):
        response = self.client.request(features=['hourly'], location=LOCATION)
        self.assertEqual(response['response']['features']['hourly'], 1)

    def test_multiple_features(self):
        response = self.client.request(features=['conditions', 'forecast'], location=LOCATION)
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
