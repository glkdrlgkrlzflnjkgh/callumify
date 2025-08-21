from setuptools import setup, find_packages

print("callumify approches!")

setup(
    name="Callumify",
    version="0.2.0",
    packages=find_packages(),
    author="Callum",
    author_email="xcallumnicx@gmail.com",  # optional
    description="Some handy-dandy print related functions that you'll probably never use... (yes, we even have a quote of the day function)",
    long_description="Note that Callumify comes under the totally not fictional Callum-Public-Liscence (this liscense is technically canon now). Use responsibly.",
    long_description_content_type="text/plain",
    license="Callum-Public-Liscence",
    url="https://github.com/CallumDev/Callumify",  # or wherever you host it
    install_requires=["pygame-ce"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)