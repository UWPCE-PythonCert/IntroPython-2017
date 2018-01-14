from setuptools import setup

def get_version():
    """
    Reads the version string from the package __init__ and returns it
    """
    with open(os.path.join("capitalize", "__init__.py")) as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None


setup(
   name='mailroom',
   version=get_version(),
   author='Eowyn',
   author_email='aac@example.com',
   packages=['mailroom'],
   scripts=['bin/mailroom'],
   url='https://github.com/Eowyn42/IntroPython-2017/tree/master/students/eowyn/session10',
   #license='LICENSE.txt',
   description='Donation manager',
   #long_description=open('README.txt').read(),
   install_requires=[
       "pytest",
   ],
)
