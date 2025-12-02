# Sunflower Tests - A Small Repository for Exploring Test Methods

## Installation

You can use the qr tag to link to this page.

<img src="images/qr_code.png" width="200" height="200" alt="A QR tag linking to this repository."/>

We recomend using [uv](https://docs.astral.sh/uv/) to install and run this software.
If you haven't already done so please follow these [instructions](https://docs.astral.sh/uv/getting-started/installation/) to install uv.

```
git clone https://github.com/thompson318/sunflower-tests.git  # clone the repository
uv venv                                                       # create a virtual environment               
source .venv/bin/activate                                     # and activate it
uv pip install -r requirements.txt                            # use uv to install necessary libraries
```

<img src="tests/data/sunflower-expected.svg" width="200" height="200" alt="An image of a sunflower"/>

use uv
https://docs.astral.sh/uv/guides/projects/


write uv instructions here

Aim to cover
Integration / end to end testing vs unit testing

next steps: could look at mocking tests to enable us to unit test later steps


Plan: 

Installation. 

Run main program 

Look at output Discuss how we could test that it is performing as expected.

Have a look at the test_integration.py file.

Give them a fibonacci function (simple look up table) (fib_look up)
write some unit tests to make sure it works.

Then we want to add a new feature, we want to make it work for an arbitray number
Create a parametrised unit test, then modify the function to make it pass.

Create an example of an integration test. (compare sunflower images).


In this exercise, you will be given a few lines of code that perform a certain task (that you will have to understand) and then write an automated test that checks whether that task is performed correctly.


Image attribution: By Fir0002 - Own work, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=7613324

Emoji One, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
 
## Step 0

Make sure you have read the note chapters on [Testing basics](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/01testingbasics.html), [The Fields of Saskatchewan](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/02SaskatchewanFields.html) and [Test frameworks](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch03tests/03pytest.html).

If you haven't already, fork this repository and clone it on your computer.

## Step 1: Understanding the existing code
- Spend some time reading the code, try to run it and see whether you understand what's going on.
- Have you seen [`datetime`](https://docs.python.org/3.7/library/datetime.html) before?
- Play using your favourite tool (notebook, terminal, scripts) with the functions and objects used in `times.py`.

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
