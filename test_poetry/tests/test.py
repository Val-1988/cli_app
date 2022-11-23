#from cli_app import make_str_list
import builtins

import mock

import cli_app


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_make_str_list():
    with mock.patch.object(builtins, "input", lambda _: "1"):
        assert cli_app.make_str_list() == ["1"]


