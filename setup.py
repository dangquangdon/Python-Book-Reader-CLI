from setuptools import setup, find_packages

setup(
    name="PyBookReader",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click==7.1.2",
        "pyttsx3==2.90",
        "SQLAlchemy==1.3.20",
        "tabulate==0.8.7",
        "pdftotext==2.1.5",
        "alembic==1.4.3",
        "keyboard==0.13.5",
        "black",
    ],
    entry_points="""
        [console_scripts]
        pybookreader=pybookreader:book_reader
    """,
)
