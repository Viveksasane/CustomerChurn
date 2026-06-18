import setuptools


with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


__version__="0.0.0"

REPO_NAME="CustomerChurn"
AUTHOR_USER_NAME="Viveksasane"
SRC_REPO="project"
AUTHOR_EMAIL="viveksasane9978@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Customer Churn project",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)