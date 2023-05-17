# Best Practices for Automation with OpenStack SDK - OpenStack Europe Meetup May 2023
The source files for the presentation of 'Best Practices for Automation with OpenStack SDK' can be found in this repository. The presentation was held by Nils Magnus and Tino Schreiber on OpenStack Europe in May 2023.

## Installation of required packages
- switch to a directory of your choice
- Initialize a Python virtual environment

```
cd ~/
python -m venv project
source project/bin/activate
(project) ubuntu@user ~/>
```

- clone the repository and switch to the downloaded directory
```
git clone https://github.com/opentelekomcloud/best-practices-openstack-sdk.git
cd best-practices-openstack-sdk/
```

- install the requirements
```
pip install -r requirements.txt
```

## Modify Credentials

Modify the credentials in the clouds.yaml file to fit your environment.
```
cd best-practices-openstack-sdk/src/
vi clouds.yaml
```

## Run the code example

- With updated credentials you can run the code as follows:
```
cd best-practices-openstack-sdk/src/
python run.py
```
