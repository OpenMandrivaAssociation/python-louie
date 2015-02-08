%define module  louie

Summary:	Louie provides dispatch signals between objects in a wide variety of contexts
Name:		python-%{module}
Version:	1.1
Release:	15
Group:		Development/Python 
License:	BSD
Url:		http://pylouie.org/
Source0:	louie_%{version}.orig.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:  pkgconfig(python2)
Provides:	Louie

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the Python
Cookbook.

%prep
%setup -qn Louie-%{version}

%build
%{__python2} setup.py build 

%install
%{__python2} setup.py install --root=%{buildroot}

%files
%doc doc/*.txt
%{py2_puresitedir}/louie
%{py2_puresitedir}/Louie*.egg-info

