import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = ['fanstatic',
            'pyramid']
tests_require = requires + ['Arche']

setup(name='arche_google_analytics',
      version='0.1b',
      description='Include Google analytics',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Intended Audience :: Developers",
        ],
      author='Robin Harms Oredsson',
      author_email='robin@betahaus.net',
      url='https//github.com/ArcheProject/arche_google_analytics',
      keywords='web pyramid pylons arche',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      test_suite="arche_google_analytics",
      entry_points = """\
      [fanstatic.libraries]
      arche_ga = arche_google_analytics:library
      """,
      )
