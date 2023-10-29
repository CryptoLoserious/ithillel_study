# # # v_1
def parse(query: str) -> dict:
    if '?' in query:
        first_split = query.split('?')[1]
        second_split = first_split.split('&')
        final_dict = {}

        for parametr in second_split:
            if '=' in parametr:
                key, value = parametr.split('=')
                final_dict[key] = value
        return final_dict
    return {}


# # # v_2

from urllib.parse import parse_qs, urlparse
# def parse(query: str) -> dict:
#     parsed_url = urlparse(query)
#     raw_dict = parse_qs(parsed_url.query)
#
#     final_dict = {key: values[0] for key, values in raw_dict.items()}
#     return final_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


# def parse_cookie(query: str) -> dict:
#     if ';' in query:
#         first_split = query.split(';')
#         final_dict = {}
#
#         for parametr in first_split:
#             if '=' in parametr:
#                 key, value = parametr.split('=', 1)
#                 final_dict[key] = value
#         return final_dict
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=John;') == {'name': 'John'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
#     assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
