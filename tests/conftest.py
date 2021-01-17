from pathlib import Path

import pytest

from tyred.loading import PuzzleLoader
from tyred.types import Puzzle


@pytest.fixture
def simple_spec_file() -> Path:
    here = Path(__file__).parent
    return here.parent / "puzzles/sample_spec.txt"


@pytest.fixture
def simple_spec(simple_spec_file) -> str:
    with simple_spec_file.open(mode="r") as fh_in:
        return fh_in.read()


@pytest.fixture
def simple_puzzle(simple_spec) -> Puzzle:
    gl = PuzzleLoader()
    return gl.load_puzzle(simple_spec)
