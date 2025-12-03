# Sunflower Tests - A Small Repository for Exploring Test Methods

## Installation

You can use the qr tag to link to this page.

<img src="images/qr_code.png" width="200" height="200" alt="A QR tag linking to this repository."/>

We recomend using [uv](https://docs.astral.sh/uv/) to install and run this software.
If you haven't already done so please follow these [instructions](https://docs.astral.sh/uv/getting-started/installation/) to install uv.

```
git clone https://github.com/thompson318/sunflower-tests.git  # clone the repository
cd sunflower-tests                                            # enter the directory
uv venv                                                       # create a virtual environment               
source .venv/bin/activate                                     # and activate it
uv pip install -r requirements.txt                            # use uv to install necessary libraries
python sunflower_maker.py                                     # run the code.
```

Running the program should have created the file `sunflower.svg`. You should be able to view it with it with a image viewer or webrowser. 
It should look like this ...
<img src="tests/data/sunflower-expected.svg" width="200" height="200" alt="An image of a sunflower"/>

You should be able to change the size of the image by passing an extra command line parameter (an integer from 0 to 5)

```
python sunflower_maker.py 4
```

## Consider how we can test this code.

The repository is set up to allow you to use `pytest` to test your code locally ...

```
pytest
```

And a github actions [workflow](.github/workflows/pytest.yml) to enable running tests using GitHubs CI test machines. 

For the remainder of the session we will create new tests and use test driven development to add new features using those tests. 
Start by creating your own fork of the repository using GitHub's web interface. You will then add tests and code to your own fork 
before creating a pull request and observing test behavior. 

### Excercise 1. Build an end to end test.

### Excercise 2. Create a test for the fibonacci function.

### Excercise 3. Extend the test to higher (arbitrary) values of rank and use the test as you reimplement the fibonacci function to work on any rank value.


## Further Reading and tests in other languages.

[Further Reading](resources.md)

## Acknowledgements
Image attribution: By Fir0002 - Own work, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=7613324

Emoji One, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
