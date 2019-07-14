from setuptools import setup

setup(name='SlackThermometer',
      description='',
      author='Ada',
      author_email='adriana.miclos@gmail.com',
      license='MIT',
      packages=['src'],
      install_requires=[
          'requests',
          'Adafruit_DHT'
      ],
      zip_safe=False
      )
