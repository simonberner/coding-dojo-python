# Python Coding Dojo

This is my place for practicing coding in Python. Your are free to clone it and make it your own.

## Setup

- For creating a venv checkout the [docs here](https://python.land/virtual-environments/virtualenv).
- Install/Upgrade the following things as dependencies in the projects venv (virtual environment):

- `pip install -U pytest` (see [here](https://docs.pytest.org/en/8.2.x/getting-started.html#install-pytest))
- `pip install -U pytest-watch` (see [here](https://pypi.org/project/pytest-watch/))

### Update Packages

- `pip list` (List all installed packages)
- `pip list --outdated` (List all the outdated packages)
- `pip install --upgrade package_name` (Update a specific outdated package)

## Katas

### Farkle Greed

- [The Kata](https://codingdojo.org/kata/Greed/)
- [More Information (Wiki)](https://en.wikipedia.org/wiki/Farkle#)

## Approach

To solve the above coding katas I use [TDD](https://www.agilealliance.org/glossary/tdd/).

1. Write a single failing unit test
2. Write the simples possible code to make the test pass
3. Refactor the code until it conforms to
   the rule of simplicity (simplicity criteria)
4. Repeat -> accumulate more unit tests over time

### [Rules of Simplicity](https://www.agilealliance.org/glossary/rules-of-simplicity/)

A set of criteria, in priority order, proposed by Kent Beck to judge whether some source code is “simple enough”:

- The code is verified by automated tests, and all such tests pass
- The code contains no duplication
- The code expresses separately each distinct idea or responsibility
- The code is composed of the minimum number of components (classes, methods, lines) compatible with the first three
  criteria

## Learnings

### Farkle

>`array_of_dice[:] = [x for x in array_of_dice if x != dice]`

- The left side `array_of_dice[:]` is a slice of the entire list and points to all elements of the original list. It
  does not create a new list, instead it allows assignment to all elements of the original list.
- The right side `[x for x in array_of_dice if x != dice]` is the new list created by the list comprehension.
- The assignment `=` replaces the entire content of array_of_dice with the new list.
- This operation ensures that the original list object `array_of_dice` is updated in place, which is important if other
  references to this list exist elsewhere.
