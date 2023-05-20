#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Chapter_16_local_api_server.py
# Gebaseerd op: isevenapi.xyz/

from typing import Union, List

import re
import json
import dataclasses
from random import choice
from http.server import HTTPServer, BaseHTTPRequestHandler

_ADS: List[str] = [
    '1995 NISSAN Maxima, green, leather, loaded, CD, auto start, sunroof, 4-door, great condtion, NOT FOR SALE',
    "Andy's hand-made Fingerboxes are built with high quality aluminum. Get yours today!",
    "Auto Repair Service: Free pick-up and delivery. "
    "Try us once, you'll never go anywhere again. Email dave57@qotmail.com",
    'Buy isEvenCoin, the hottest new cryptocurrency!',
    'CHINA CABINET, buffet, hutch solid pine, 6.5 tall x 4.5 wide, lighted windows. '
    'few cat scratches but cat has died. $700. Call 435-555-6421',
    'Drink Sprunk cola! The essence of life.',
    'FOR SALE - collection of old people call 253-555-7212',
    'FOR SALE: Complete set of Encyclopedia Britannica, 45 volumes. $1000. '
    'No longer needed. Got married, wife knows everything. Call 5435553442.',
    'FOR SALE: outdoor nativity scene. No Jesus, Mary, or Joseph. $50 OBO call 344-555-6425',
    'FULL SIZE Mattress. Royal Tonic, 20 year warranty. Like new. Slight urine smell. $40, call 818-555-2301',
    'For Sale: Slightly used headstone. Perfect gift for someone named William Peterson. '
    'Email betsy.peterson@qotmail.com',
    'For sale: human skull. Used once only. $200 OBO Dr. Scott Tyler, 454-555-6533',
    'HELP WANTED: Child Care provider. Apply in person, Jack & Kill Childcare, 1905 NW Smith. NO PHONE CALLS',
    "HONDA CIVIC '96, AM/FM/CD, low miles, Good condition. Speaks Spanish $3500 339-555-6289",
    'Looking for someone to do yard work. Must have a hoolahoop. 760-555-7562',
    'Lost- Donkey, wearing a pink halter, Monterey Center- 269-555-6234',
    'PONY FOR SALE. Looks like a small horse. $900. 480-555-6341',
    'SURGEON WANTED for a new heath clinic opening in SF. No experience needed. Must have own tools. Call 407-555-5400',
    'Scarecrow wanted for field in Saskatchewan. Must not be afraid of birds. Email buddybilly@qotmail.com',
    'TIRED OF WORKING FOR ONLY $9.75 PER HOUR? We offer profit sharing and flexible hours. '
    'Starting pay: $5-$7 per hour. Call 413-555-3451',
    'WANTED: Air Traffic Control. No Exp. Needed; we train, HS grads 17-34. Great pay, benefits. Must relocate. '
    'Call 284-555-7133',
    "WILL the person who got hit in the head with a tomato in the 1950's please contact 414-555-4536"
]


# noinspection PyPep8Naming
@dataclasses.dataclass
class regex_in:
    string: str
    match: re.Match = None

    def __eq__(self, other: Union[str, re.Pattern]) -> bool:
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        self.match = other.fullmatch(self.string)
        return self.match is not None


class IsEvenAPIServer(BaseHTTPRequestHandler):
    _ads = ['Check out isevenapi.xyz !']
    _free_tier_range: range = range(0, (999_999 + 1))

    @staticmethod
    def check_is_even(number: int) -> bool:
        return int(number) % 2 == 0  # can raise ValueError

    def _create_response(self, received: str) -> str:
        try:
            # convert given to int, also accepts negative integers
            # raises ValueError if non-int is given
            received = int(received)
        except ValueError:
            return '{"error": "what is this I don\'t even"}'

        if received in self._free_tier_range:
            iseven: bool = self.check_is_even(received)
            return json.dumps({
                'ad': choice(_ADS),
                'iseven': iseven
            })
        else:
            return '{"error":  "Number out of range. Upgrade to isEven API Premium or Enterprise."}'

    # noinspection PyPep8Naming
    def do_GET(self) -> None:
        data: str
        match regex_in(self.path):
            # GET /api/
            case r'^\/api\/?':
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                data = 'isEven API root'

            # GET /api/iseven/<number>/
            case r'^\/api\/iseven\/(?P<iseven>[\w\d]+)\/?' as _r:
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                _received = _r.match.group('iseven')
                data = self._create_response(_received)

            case _:  # catch all
                self.send_response(404)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                data = '<h1>404 Not Found</h1>'
        # serve the data
        self.wfile.write(bytes(data, "utf-8"))


if __name__ == '__main__':
    from urllib.parse import urljoin

    with HTTPServer(('localhost', 8080), IsEvenAPIServer) as server:
        url, port = server.server_address
        netloc = f'http://{url}:{port}/'
        print(netloc)
        print(urljoin(netloc, 'api/iseven/1'))
        print(urljoin(netloc, 'api/iseven/2'))
        print(urljoin(netloc, 'api/iseven/A'))
        server.serve_forever()
