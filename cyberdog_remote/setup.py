from setuptools import setup

package_name = 'cyberdog_remote'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hanzx',
    maintainer_email='thefoxfoxfox@outlook.com',
    description='ROS 2 Package for Inspire Gripper',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client = cyberdog_remote.cyberdog_remote_client:main',
        ],
    },
)
