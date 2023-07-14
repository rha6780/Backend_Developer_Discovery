#!/bin/bash

cd ../developer_discover

coverage erase

coverage run ../developer_discover/manage.py test --settings=developer_discover.settings.test

coverage xml && coverage html

mv ../developer_discover/coverage.xml ../reports/coverage

mv ../developer_discover/htmlcov/index.html ../reports/coverage/index.html

cd ..

genbadge coverage
