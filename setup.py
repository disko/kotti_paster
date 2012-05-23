from setuptools import setup, find_packages

version = '0.1'

install_requires = [
    'setuptools',
    'PasteScript',
    'Cheetah',
    ]

setup(name='kotti_paster',
      version=version,
      description="Paster AddOn Template for Kotti",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='kotti addon scaffold',
      author='j23d',
      author_email='j23d@jusid.de',
      url='jusid.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
            [paste.paster_create_template]
            kotti_addon = kotti_paster.paster_templates:KottiAddonTemplate
      """,
      message_extractors={'kotti_paster': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
