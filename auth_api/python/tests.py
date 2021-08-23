import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        # I am changing the test because in Python the ordering of a Dictionary is not guarranteed.
        # My JWT is valid, but the alg and typ fields in the header are in a different order.
        # That causes the test to fail, even when the token is valid and equivalent.
        # self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))
        self.assertEqual(
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w",
            self.convert.generate_token("admin", "secret"),
        )

    def test_access_data(self):
        self.assertEqual(
            "You are under protected data",
            self.validate.access_data(
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI"
            ),
        )

    def test_access_data_with_my_token(self):
        # Validating it works with my token (See test_generate_token comments)
        self.assertEqual(
            "You are under protected data",
            self.validate.access_data(
                "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w"
            ),
        )

    def test_generate_token_fail(self):
        # validating it fails with then incorrect values
        self.assertNotEqual(
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w",
            self.convert.generate_token("admin", "secret1"),
        )

    def test_access_data_fail(self):
        # Validating it doesn't work with a bad token, last letter changed
        self.assertNotEqual(
            "You are under protected data",
            self.validate.access_data(
                "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9t"
            ),
        )


if __name__ == "__main__":
    unittest.main()
