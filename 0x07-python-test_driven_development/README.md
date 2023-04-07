#0x07 Python Test Driven Development
0x07 Python test driven development is a module in ALX Software development program that teaches about testing and writing functions that can easily be tested and throw appropriate errors in case they are misued.

##Two modules for testing in python
Unittest (most popular)
Doctest (simplest method)

###Unittest
To perform a unit test, you must create a new module (file) where you declare a class for instace to test you employee class, you could have
```class TestEmployee(unittest.TestCase):
	def test_your_case(self):
		"""
		Your methods goes here
		"""
``

Then you can call your file and it will automatically run it as a unittest file by using the code
```>>> python -m unittest test_employee```

To cuase your file to run when it is called without unittest you should add this code at the end of the file.

```
if __name__ = "__main__":
	unittest.main()
```

###Doctest
Read more about doctest on the internet.
