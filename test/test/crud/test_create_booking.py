import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and Booking ID shouldn't be null")
    @allure.description("Create a Booking from the payload and verify that booking id should not be null")


    def test_create_booking_positive(self):
        pass