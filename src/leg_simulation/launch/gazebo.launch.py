from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch_ros.descriptions import ParameterValue
from launch.actions import SetEnvironmentVariable
from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros
import launch
import os


def generate_launch_description():

    pkg_share = launch_ros.substitutions.FindPackageShare(package='leg_simulation').find('leg_simulation')
    default_model_path = os.path.join(pkg_share, 'description/leg.xacro')

    # Eanble finding meshes in gazebo with "package://" in the urdf description
    # This is what gazebo search for:
    # mesh - model://leg_simulation/meshes/base_link.stl
    # model path is stored in the GAZEBO_MODEL_PATH environment variable
    pkg_install_path = get_package_share_directory('leg_simulation')
    pkg_install_path_parent = os.path.dirname(pkg_install_path)
    if 'GAZEBO_MODEL_PATH' in os.environ:
        model_path =  os.environ['GAZEBO_MODEL_PATH'] + ':' + pkg_install_path_parent
    else:
        model_path =  pkg_install_path_parent
    print('-' * 50)
    print(f'Package install path: {pkg_install_path}')
    print(f'Parent path: {pkg_install_path_parent}')
    print(f'Model path: {model_path}')
    print('-' * 50)

    # Launch Gazebo
    gazebo_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        [os.path.join(get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py'])
    )

    # Store the xacro urdf robot description
    robot_description = Command(['xacro ', LaunchConfiguration('model')])

    # Launch robot state publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': ParameterValue(robot_description, value_type=str)}],
        output='screen'
    )

    # Spawn the robot into Gazebo
    robot_spawn_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'leg'           
        ],
        output='screen'
    )

    return LaunchDescription([

        SetEnvironmentVariable(name='GAZEBO_MODEL_PATH', value=model_path),
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),

        gazebo_launch,
        robot_state_publisher_node,
        robot_spawn_node,
    ])
