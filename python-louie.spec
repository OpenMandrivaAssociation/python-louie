Name: python-louie
Summary: Louie provides dispatch signals between objects in a wide variety of contexts
Version: 1.1
Release: %mkrel 2
Group: Development/Python 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://pylouie.org/
Source0: louie_%{version}.orig.tar.gz
License: BSD
Provides: Louie
BuildRequires: python-setuptools
%py_requires -d

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the Python
Cookbook.

%files
%defattr(-,root,root)
%py_platsitedir/*

#------------------------------------------------------------

%prep
%setup -q -n Louie-%version

%build
python setup.py build 

%install
rm -rf %buildroot

python setup.py install --root=%buildroot --install-lib=%py_platsitedir

%clean
rm -rf %buildroot

