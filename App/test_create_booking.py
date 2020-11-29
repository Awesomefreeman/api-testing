from create_booking import UserInfo
from create_booking import BookingDates
from create_booking import Request
from datetime import datetime


def test_create_booking():
    booking_dates = BookingDates("2018-01-01", "2019-01-01")
    user_info = UserInfo("Jim", "Brown", 111, True, booking_dates, "Breakfast")
    response = Request(user_info).create_booking()
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == "Jim"
    assert response.json()["booking"]["lastname"] == "Brown"
    assert response.json()["booking"]["totalprice"] == 111
    assert response.json()["booking"]["depositpaid"] == True
    assert response.json()["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response.json()["booking"]["bookingdates"]["checkout"] == "2019-01-01"
    assert response.json()["booking"]["additionalneeds"] == "Breakfast"


def test_create_booking_2():
    now = datetime.now()
    booking_dates = BookingDates(f"{now.year}-{now.month}-{now.day}", f"{now.year + 1}-{now.month}-{now.day}")
    user_info = UserInfo("LongFirstnameLongFirstnameLongFirstname",
                         "LongLastnameLongLastnameLongLastnameLongLastname", 999.99, False, booking_dates, "Breakfast")
    response = Request(user_info).create_booking()
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == "LongFirstnameLongFirstnameLongFirstname"
    assert response.json()["booking"]["lastname"] == "LongLastnameLongLastnameLongLastnameLongLastname"
    assert response.json()["booking"]["totalprice"] == 999
    assert response.json()["booking"]["depositpaid"] == False
    assert response.json()["booking"]["bookingdates"]["checkin"] == f"{now.year}-{now.month}-{now.day}"
    assert response.json()["booking"]["bookingdates"]["checkout"] == f"{now.year + 1}-{now.month}-{now.day}"
    assert response.json()["booking"]["additionalneeds"] == "Breakfast"
