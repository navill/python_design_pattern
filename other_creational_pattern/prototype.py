import copy


class Website:
    # kwargs와 setattr를 이용해 매개변수 및 속성 생성에 유연성을 제공
    def __init__(self, name, domain, description, author, **kwargs):
        '''Examples of optional attributes (kwargs):
           category, creation_date, technologies, keywords.
        '''
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author

        # kwargs = {'created':'2019-10-10'}
        for key in kwargs:
            # self.key = kwargs[key]
            # -> self.created = '2019-10-10'
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = [f'Website "{self.name}"\n', ]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')

        return ''.join(summary)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        # objects[identifier]
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f'Incorrect object identifier: {identifier}')
        obj = copy.deepcopy(found)
        # clone obj 내에 속성 생성
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


def main():
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website('ContentGardening',
                    domain='contentgardening.com',
                    description='Automation and data-driven apps',
                    author='Kamon Ayeva',
                    category='Blog',
                    keywords=keywords)

    prototype = Prototype()
    # 클론 객체를 구분하기 위한 identifier
    identifier = 'ka-cg-1'
    prototype.register(identifier, site1)
    # {'ka-cg-1': site2}
    site2 = prototype.clone(identifier,
                            name='ContentGardeningPlayground',
                            domain='play.contentgardening.com',
                            description='Experimentation for techniques featured on the blog',
                            category='Membership site',
                            creation_date='2018-08-01')

    for site in (site1, site2):
        print(site)
    print(f'ID site1 : {id(site1)} != ID site2 : {id(site2)}')


if __name__ == '__main__':
    main()
