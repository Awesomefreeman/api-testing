import requests


class Request:
    def __init__(self, body):
        self.url = "https://restful-booker.herokuapp.com/booking"
        self.body = body

    def create_booking(self):
        return requests.post(self.url, json=dict(self.body))


class UserInfo(dict):
    def __init__(self, firstname, lastname, totalprice, depositpaid,
                 bookingdates, additionalneeds):
        dict.__init__(self, firstname=firstname, lastname=lastname, totalprice=totalprice,
                      depositpaid=depositpaid, bookingdates=bookingdates,
                      additionalneeds=additionalneeds)


class BookingDates(dict):
    def __init__(self, checkin, checkout):
        dict.__init__(self, checkin=checkin, checkout=checkout)
