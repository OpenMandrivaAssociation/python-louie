%define module  louie
%define name   	python-%{module}
%define version	1.1
%define release %mkrel 8

Name: 	       %{name}
Summary:       Louie provides dispatch signals between objects in a wide variety of contexts
Version:       %{version}
Release:       %{release}
Group: 	       Development/Python 
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 	       http://pylouie.org/
Source0:       louie_%{version}.orig.tar.gz
License:       BSD
Provides:      Louie
BuildRequires: python-setuptools
BuildArch:     noarch
%py_requires -d

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the Python
Cookbook.

%prep
%setup -q -n Louie-%version

%build
%__python setup.py build 

%install
%__rm -rf %{buildroot}

%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*.txt
%py_puresitedir/louie
%py_puresitedir/Louie*.egg-info
