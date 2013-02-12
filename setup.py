from setuptools import setup, find_packages

def long_description(source):
    with open(source, 'r') as f:
        return f.read()

setup(
    name = "django-color-utils",
    version = "0.1.2-sd",
    author = "Sheepdog",
    author_email = "development@sheepdoginc.ca",
    description = ("An assortment of color picking widgets"),
    license = "BSD",
    keywords = "Django color widgets",
    url = "https://github.com/SheepDogInc/django-color-utils",
    packages=find_packages(exclude=[]),
    long_description=long_description("README.md"),
    include_package_data=True,
)

