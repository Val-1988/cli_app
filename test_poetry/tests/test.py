from cli_app import make_str_list, get_http_data


def test_make_str_list(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    assert make_str_list() == []


def test_get_http_data(capsys):
    str_lst = ["1", "https://github.com/"]
    get_http_data(str_lst)
    out, err = capsys.readouterr()
    assert out == "строка 1 не является ссылкой \n{'https://github.com/': {'GET': 200, 'POST': 404, 'PUT': 404, " \
                  "'DELETE': 404, 'OPTIONS': 404}}\n"

