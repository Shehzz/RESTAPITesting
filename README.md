## REST API testing using Pytest

---

#### Requirements: 
* Python3
* Pytest
* Request libraries
* Faker

---

To run these files, please do the following commands:

1. `pip3 install pytest`, `pip3 install requests` & `pip3 install faker`
2. To run the positive scenarios, please run: `pytest -m positive -v -s --disable-pytest-warnings`
3. To run the negative scenarios, please run: `pytest -m negative -v -s --disable-pytest-warnings`

---

#### TIPS:
* Make sure to look into the `variables.py` file to customise any variable to your liking.
* When running the pytest without the `--disable-pytest-warnings` flag, it shows warnings for custom markers used such as
  `positive` & `negative` markers that are used in my code.