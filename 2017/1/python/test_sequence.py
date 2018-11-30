import pytest

from sequence import next_in_sequence

@pytest.mark.parametrize("sequence,offset,expected",(
    ("1122", 1, 3),
    ("1111", 1, 4),
    ("1234", 1, 0),
    ("91212129", 1, 9),
    ("1212", 2, 6),
    ("1221", 2, 0),
    ("123425", 3, 4),
    ("123123", 3, 12),
    ("12131415", 4, 4)

))
def test_sequence(sequence, offset, expected):
    assert next_in_sequence(sequence, offset) == expected
