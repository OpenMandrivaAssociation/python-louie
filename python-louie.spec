%define module  louie

Summary:	Louie provides dispatch signals between objects in a wide variety of contexts
Name:		python-%{module}
Version:	2.0
Release:	3
Group:		Development/Python 
License:	BSD
Url:		http://pylouie.org/
Source0:	https://files.pythonhosted.org/packages/f2/f8/f9dfd97003f1c120dca1ed4dc9e3e16b74b583ce5bcb2d9b013142b6bee2/Louie-2.0.tar.gz
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
%{__python} setup.py build 

%install
%{__python} setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/louie
%{py_puresitedir}/Louie*.egg-info

