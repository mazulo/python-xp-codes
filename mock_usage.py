from unittest.mock import MagicMock, Mock, patch

# ------- Part 1 - difference between MagicMock and Mock
mock = Mock()
magic_mock = MagicMock()

try:
    print(mock.__or__)
except AttributeError:
    print('woops')

print(magic_mock.__or__)

# ------- Part 2 - What MagicMock can do

mock = MagicMock()
mock.method()
mock.attribute
mock.attribute.return_value = 123
mock.attribute

mock.method.called
mock.method.call_count
mock.method.call_args

mock.method(1, 2, 3)
mock.method.call_count
mock.method.call_args
mock.method.call_args_list

# ------- Part 3 - What patch can do
from my_date import get_current_datetime

my_datetime = MagicMock()
my_datetime.now.return_value = '24-06-2020'

with patch('my_date.datetime', my_datetime):
    print(get_current_datetime())
