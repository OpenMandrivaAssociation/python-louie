%define module  louie

Summary:	Louie provides dispatch signals between objects in a wide variety of contexts
Name:		python-%{module}
Version:	1.1
Release:	8
Group:		Development/Python 
License:	BSD
Url:		http://pylouie.org/
Source0:	louie_%{version}.orig.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
Provides:	Louie
%py_requires -d

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the Python
Cookbook.

%prep
%setup -qn Louie-%{version}

%build
%__python setup.py build 

%install
%__python setup.py install --root=%{buildroot}

%files
%doc doc/*.txt
%{py_puresitedir}/louie
%{py_puresitedir}/Louie*.egg-info

