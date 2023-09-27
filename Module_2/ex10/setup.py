from setuptools import find_packages, setup

package_name = 'ex10_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vasya',
    maintainer_email='v.postnykh@g.nsu.ru',
    description='This was created for task ex10',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
	'console_scripts': [
		'text_to_cmd_vel = ex10_package.text_to_cmd_vel:main',
	],
    },
)
