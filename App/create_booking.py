class UserInfo(dict):
    def __init__(self, firstname, lastname, totalprice, depositpaid,
                 bookingdates, additionalneeds):
        dict.__init__(self, firstname=firstname, lastname=lastname, totalprice=totalprice,
                      depositpaid=depositpaid, bookingdates=bookingdates,
                      additionalneeds=additionalneeds)


class BookingDates(dict):
    def __init__(self, checkin, checkout):
        dict.__init__(self, checkin=checkin, checkout=checkout)


class Encoder:
    def __init__(self, data):
        self.data = data

    def create_json(self):
        return dict(self.data)
