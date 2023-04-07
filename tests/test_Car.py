import pytest
from Car import Car


@pytest.fixture
def my_car():
    my_car = Car(50)
    return my_car


def test_car_accelerate(my_car):
    my_car.accelerate()
    assert my_car.speed == 55


def test_car_brake(my_car):
    my_car.brake()
    assert my_car.speed == 45
