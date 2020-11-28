import requests
from create_booking import UserInfo
from create_booking import BookingDates
from create_booking import Encoder

url = "https://restful-booker.herokuapp.com/booking"


def test_create_booking():
    booking_dates = BookingDates("2018-01-01", "2019-01-01")
    user_info = UserInfo("Jim", "Brown", 111, True, booking_dates, "Breakfast")
    body = Encoder(user_info).create_json()
    response = requests.post(url, json=body)
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == "Jim"
    assert response.json()["booking"]["lastname"] == "Brown"
    assert response.json()["booking"]["totalprice"] == 111
    assert response.json()["booking"]["depositpaid"] == True
    assert response.json()["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response.json()["booking"]["bookingdates"]["checkout"] == "2019-01-01"
