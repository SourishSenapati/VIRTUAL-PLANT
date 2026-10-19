from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'virtual_refinery'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools', 'numpy', 'scipy', 'pyyaml'],
    zip_safe=True,
    maintainer='Sourish Senapati',
    maintainer_email='sourishsenapati791@gmail.com',
    description='Physics-accurate Virtual Petroleum Refinery Digital Twin Simulator in ROS 2',
    license='Educational Non-Commercial with Mandatory Attribution',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cdu_vdu_simulator = virtual_refinery.cdu_vdu_simulator:main',
            'conversion_units = virtual_refinery.conversion_units:main',
            'stream_router = virtual_refinery.stream_router:main',
            'process_safety_sis = virtual_refinery.process_safety_sis:main',
            'gazebo_bridge = virtual_refinery.gazebo_bridge:main',
            'refinery_orchestrator = virtual_refinery.refinery_orchestrator:main',
        ],
    },
)
