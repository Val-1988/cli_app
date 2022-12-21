# This is a small application that checks if a string entered by the user is a link.
It then outputs a list of the strings entered as a list.
It then outputs a list of methods that work on the given resource.
An example of how the application works is shown below (a picture from the terminal).
The application is partially covered by pytests.


An example of how the code works:

enter link, to finish enter 0 https://python-poetry.org/docs/#installing-with-the-official-installer
enter link, to finish enter 0 no link
enter link, to finish enter 0 https://career.habr.com/vacancies?type=suitable
enter link, to finish enter 0 NO LINK LALALLA
enter link, to finish enter 0 0
{'https://python-poetry.org/docs/#installing-with-the-official-installer': {'GET': 200, 'POST': 405, 'PUT': 405, 'DELETE': 405, 'OPTIONS': 204}}
string no link is not a link
{'https://career.habr.com/vacancies?type=suitable': {'GET': 200, 'POST': 404, 'PUT': 404, 'DELETE': 404, 'OPTIONS': 404}}
string NO LINK LALALLA is not a link

Process finished with exit code 0
