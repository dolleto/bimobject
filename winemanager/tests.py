from rest_framework.test import APITestCase
from rest_framework import status
from winemanager.models import Winemaker, WineBottle


class WinemakerViewSetTests(APITestCase):
    def setUp(self):
        self.winemaker1 = Winemaker.objects.create(name="Winemaker A", address="Address A")
        self.winemaker2 = Winemaker.objects.create(name="Winemaker B", address="Address B")

    def test_list_winemakers(self):
        url = "/api/winemakers/"
        response = self.client.get(url)
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)
        self.assertIn("name", results[0])
        self.assertIn("address", results[0])

    def test_search_winemakers(self):
        url = "/api/winemakers/?search=Winemaker B"
        response = self.client.get(url)
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Winemaker B")

    def test_order_winemakers(self):
        url = "/api/winemakers/?ordering=name"
        response = self.client.get(url)
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(results[0]["name"], "Winemaker A")
        self.assertEqual(results[1]["name"], "Winemaker B")


class WineBottleViewSetTests(APITestCase):
    def setUp(self):
        self.winemaker1 = Winemaker.objects.create(name="Winemaker A", address="Address A")
        self.winemaker2 = Winemaker.objects.create(name="Winemaker B", address="Address B")
        self.winebottle1 = WineBottle.objects.create(
            winemaker=self.winemaker1,
            name="Wine A",
            year=2020,
            size="750ml",
            taste="Sweet",
            description="Description A",
            food_pairing="Food A",
            count_in_winecellar=10,
        )
        self.winebottle2 = WineBottle.objects.create(
            winemaker=self.winemaker2,
            name="Wine B",
            year=2019,
            size="750ml",
            taste="Dry",
            description="Description B",
            food_pairing="Food B",
            count_in_winecellar=20,
        )

    def test_list_winebottles(self):
        url = "/api/winebottles/"
        response = self.client.get(url)
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)

    def test_filter_winebottles(self):
        url = "/api/winebottles/?style=dry"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_winebottles_invalid_style(self):
        url = "/api/winebottles/?style=Red"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_winebottles(self):
        url = "/api/winebottles/?search=Wine A"
        response = self.client.get(url)
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Wine A")

    def test_order_winebottles(self):
        url = "/api/winebottles/?ordering=year"
        response = self.client.get(url)
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(results[0]["year"], 2019)
        self.assertEqual(results[1]["year"], 2020)

    def test_winebottles_by_winemaker(self):
        url = "/api/winebottles/by_winemaker/?winemaker_id=" + str(self.winemaker1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["winemaker"], self.winemaker1.id)

    def test_winebottles_by_winemaker_missing_id(self):
        url = "/api/winebottles/by_winemaker/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "winemaker_id is required")
