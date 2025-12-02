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


Image attribution: By Fir0002 - Own work, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=7613324

Emoji One, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
 


## Step 1: Understanding the existing code
- Spend some time reading the code, try to run it and see whether you understand what's going on.

## Step 2: Writing a unit test

- Create a new file called `test_times.py` in the same directory where `times.py` is.
- Make the `overlap_time` function accessible to that file. (*Hint*: You need to `import` the file).
- Move the content from the `if __name__ ...` block from `times.py` to a function called `test_given_input` into `test_times.py`
  and fill the gaps for `result` and `expected`. (For now, you can copy the output of the program as the expected value)
```python
def test_given_input():
    ... 
    result = ... 
    expected = ...
    assert result == expected
```

## Step 3: Running the tests
- run `pytest` on that directory and see whether the test is picked up by `pytest` and whether it passes. If the test doesn't pass, see if you can find what is going wrong.

## Step 4: Push to GitHub
- When you are happy with your solution (or want some feedback!):
    - Push your new code to your own fork.
    - On GitHub, open a pull request from your fork to the original repository.
    - In the description, include the text as required in the issue for this exercise. This will link your PR to this issue.
    - On the PR text, comment on what you found difficult or interesting, or something you learned.
- Continue with the remaining steps (7. - 9.) on the following issue in the Classwork repository.
