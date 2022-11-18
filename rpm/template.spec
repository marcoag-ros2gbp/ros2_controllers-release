%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2-controllers-test-nodes
Version:        2.14.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2_controllers_test_nodes package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rclpy
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-trajectory-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Demo nodes for showing and testing functionalities of the ros2_control
framework.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Nov 18 2022 Denis Štogl <denis@stoglrobotics.de> - 2.14.0-1
- Autogenerated by Bloom

* Wed Oct 05 2022 Denis Štogl <denis@stoglrobotics.de> - 2.13.0-1
- Autogenerated by Bloom

* Thu Sep 01 2022 Denis Štogl <denis@stoglrobotics.de> - 2.12.0-1
- Autogenerated by Bloom

* Thu Aug 04 2022 Denis Štogl <denis@stoglrobotics.de> - 2.11.0-1
- Autogenerated by Bloom

* Mon Aug 01 2022 Denis Štogl <denis@stoglrobotics.de> - 2.10.0-1
- Autogenerated by Bloom

* Thu Jul 14 2022 Denis Štogl <denis@stoglrobotics.de> - 2.9.0-1
- Autogenerated by Bloom

* Sat Jul 09 2022 Denis Štogl <denis@stoglrobotics.de> - 2.8.0-1
- Autogenerated by Bloom

* Sun Jul 03 2022 Denis Štogl <denis@stoglrobotics.de> - 2.7.0-1
- Autogenerated by Bloom

* Sat Jun 18 2022 Denis Štogl <denis@stoglrobotics.de> - 2.6.0-1
- Autogenerated by Bloom

* Fri May 13 2022 Denis Štogl <denis@stoglrobotics.de> - 2.5.0-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Denis Štogl <denis@stoglrobotics.de> - 2.4.0-1
- Autogenerated by Bloom

* Thu Apr 21 2022 Denis Štogl <denis@stoglrobotics.de> - 2.3.0-1
- Autogenerated by Bloom

* Fri Mar 25 2022 Denis Štogl <denis@stoglrobotics.de> - 2.2.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 Denis Štogl <denis@stoglrobotics.de> - 2.1.0-1
- Autogenerated by Bloom

