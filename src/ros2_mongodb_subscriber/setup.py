from setuptools import find_packages, setup

package_name = 'ros2_mongodb_subscriber'

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
    maintainer='pi',
    maintainer_email='by.pro1001@gmail.com',
    description='simple mongodb subscriber',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mongodb_subscriber = ros2_mongodb_subscriber.mongodb_subscriber:main'
        ],
    },
)
