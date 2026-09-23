import unittest

from tallest_hero import get_tallest_hero


class TestGetTallestHero(unittest.TestCase):

    def test_male_with_job(self):
        hero = get_tallest_hero("Male", True)

        self.assertEqual(hero["appearance"]["gender"], "Male")
        self.assertNotEqual(hero["work"]["occupation"], "-")

    def test_male_without_job(self):
        hero = get_tallest_hero("Male", False)

        self.assertEqual(hero["appearance"]["gender"], "Male")
        self.assertEqual(hero["work"]["occupation"], "-")

    def test_female_with_job(self):
        hero = get_tallest_hero("Female", True)

        self.assertEqual(hero["appearance"]["gender"], "Female")
        self.assertNotEqual(hero["work"]["occupation"], "-")

    def test_female_without_job(self):
        hero = get_tallest_hero("Female", False)

        self.assertEqual(hero["appearance"]["gender"], "Female")
        self.assertEqual(hero["work"]["occupation"], "-")

    def test_result_is_hero(self):
        hero = get_tallest_hero("Male", True)

        self.assertTrue("name" in hero)
        self.assertTrue("appearance" in hero)
        self.assertTrue("work" in hero)

    def test_male_with_job_result_has_height(self):
        hero = get_tallest_hero("Male", True)

        self.assertTrue("height" in hero["appearance"])

    def test_female_with_job_result_has_height(self):
        hero = get_tallest_hero("Female", True)

        self.assertTrue("height" in hero["appearance"])

    def test_male_without_job_result_is_not_female(self):
        hero = get_tallest_hero("Male", False)

        self.assertNotEqual(hero["appearance"]["gender"], "Female")

    def test_female_without_job_result_is_not_male(self):
        hero = get_tallest_hero("Female", False)

        self.assertNotEqual(hero["appearance"]["gender"], "Male")


if __name__ == "__main__":
    unittest.main()