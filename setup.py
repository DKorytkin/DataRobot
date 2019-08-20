from setuptools import setup, find_packages


def long_description():
    with open("README.md", "r") as fh:
        return fh.read()


if __name__ == "__main__":
    setup(
        version="0.0.1",
        name="puzzle",
        description="Application for DataRobot test exercise only",
        long_description=long_description(),
        long_description_content_type="text/markdown",
        author="Denis Korytkin",
        author_email="dkorytkin@gmail.com",
        keywords=["DataRobot", "Exercise", "HomeWork"],
        url="https://github.com/DKorytkin/puzzle",
        packages=find_packages(exclude=["tests"]),
        include_package_data=True,
        package_data={'': ['*.txt']},
        entry_points={"console_scripts": ['puzzle = puzzle.cli:main']},
        py_modules=["puzzle", "puzzle.app", "puzzle.cli"],
        platforms=['linux'],
        license='MIT license',
        python_requires=">=3.6",
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python :: 3.6',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
        ],
    )
