from rest_framework import status
from rest_framework.test import APITestCase
from rest_api.models import Car, Rate


# Create your tests here.


class ApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cars = [Car.objects.create() for _ in range(3)]
        cls.car = cls.cars[0]
        cls.civic = Car.objects.create(make='honda', model='Civic')
        cls.cars.append(cls.civic)
        for _ in range(3):
            Rate.objects.create(car_id=cls.civic, rating=5)

    def test_list_cars(self):
        response = self.client.get('/cars/')

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.cars), len(response.data))

    def test_post_car_successful(self):
        test_data = {'make': 'bmw', 'model': '525i'}
        response = self.client.post('/cars/', data=test_data)

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals(test_data, response.data)

    def test_post_car_unsuccesful(self):
        test_data = {'make': 'not_real', 'model': 'fake'}
        response = self.client.post('/cars/', data=test_data)

        self.assertEquals(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEquals({'error': 'Resource not found'}, response.data)

    def test_post_car_already_exist(self):
        test_data = {'make': 'honda', 'model': 'Civic'}
        response = self.client.post('/cars/', data=test_data)

        self.assertEquals(status.HTTP_409_CONFLICT, response.status_code)
        self.assertEquals({'error': 'Resource already exists'}, response.data)

    def test_delete_car(self):
        response = self.client.delete(f'/cars/{self.car.pk}')

        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_post_rate(self):
        test_data = {'car_id': 4, 'rating': 5}
        response = self.client.post('/rate/', data=test_data)

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals(test_data, response.data)

    def test_popular_get(self):
        response = self.client.get('/popular/')

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(Car.objects.all()), len(response.data))
