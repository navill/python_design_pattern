import json
import os
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


# factory method
def dataextraction_factory(filepath):
    # 입력된 파일 경로에 있는 확장자에 따라 JSON or XML 인스턴스를 반환한다.
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
        print('JSON extractor:', id(extractor))
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
        print('XML extractor:', id(extractor))
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


# extract_data_from: dataextraction_factory wrapper
def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    # Exception: Cnnot extract data from data/person.sq3
    # sqlite_factory = extract_data_from('data/person.sq3')
    print()

    json_factory = extract_data_from('../data/movies.json')
    print('json_factory', id(json_factory))
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()

    xml_factory = extract_data_from('../data/person.xml')
    print('xml_factory', id(xml_factory))
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text) for p in liar.find('phoneNumbers')]
        print()
    print()


if __name__ == '__main__':
    main()
