#GCA in the Zeitgeist Movement
This repository will contain scripts used to help with the Global Chapter Administration, it will eventually be integrated into the main ZMGC application.

#Requirements
In addition to Python v 2.7.2 you will need the additional python packages, listed in the table bellow.

| Software                           | Home                                                                                                                           |
|:-----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| Python                             | [http://www.python.org/](http://www.python.org/)                                                                               |
| Trello-Python                      | [https://github.com/sarumont/py-trello](https://github.com/sarumont/py-trello)                                                 |
| BeautifulSoup                      | [http://www.crummy.com/software/BeautifulSoup/](http://www.crummy.com/software/BeautifulSoup/)                                 |
| dnspython                          | [http://www.dnspython.org/](http://www.dnspython.org/)                                                                         |
| chromium-compact-language-detector | [https://code.google.com/p/chromium-compact-language-detector/](https://code.google.com/p/chromium-compact-language-detector/) |
| fish                               | [https://pypi.python.org/pypi/fish](https://pypi.python.org/pypi/fish)                                                         |
| mechanize                          | [http://wwwsearch.sourceforge.net/mechanize/](http://wwwsearch.sourceforge.net/mechanize/)                                     |

#Installation
You need to get an API Key from Trello that does not expire - you can always deleted - visit [https://trello.com/1/appKey/generate](https://trello.com/1/appKey/generate)

Then setup ENV variables in your .zshrc or .bash for TRELLO_API_KEY and TRELLO_TOKEN

#Running

    ☺  python site_survey.py                                                        * master 02274c4 ✗zmgc"
            >))'>                                                                                   6%  3/49
    
    Currently we have to check 49                                                                                                     
    ==============
    Number of sites with no link back is 38 and are as follows:
    {'name': 'Argentina', 'urls': ['http://www.zeitgeistargentina.com']}
    {'name': 'Austria', 'urls': ['http://www.zeitgeist-movement.at']}
    ...

#Todo
* Work through the list of what else needs changing
* Generate a report and email directly to chapter co-ordinator with changes that needs to be made.
* Automatically update the Trello Card to say that it an email has been sent

#Further improvements
Using the python CLDR library, we can test to see in what language the site is written, for example:

    (zmgc)☺  python                                                                                                                                            * master 02274c4 ✗zmgc"
    Python 2.7.2 (default, Jan 28 2012, 14:53:22)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cld
    >>> cld.detect('Koordinatori pokreta Razumevanje Zajednica Š-Ž')
    ('SERBIAN', 'sr', True, 51, [('SERBIAN', 'sr', 100, 34.98542274052478)])
    >>>
