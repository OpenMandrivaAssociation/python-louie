%define module  louie
%define name   	python-%{module}
%define version	1.1
%define release 9

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2011.0
+ Revision: 667942
- mass rebuild

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 1.1-7mdv2011.0
+ Revision: 591597
- fix file list

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdv2010.1
+ Revision: 523826
- rebuilt for 2010.1

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 1.1-5mdv2009.1
+ Revision: 319378
- rebuild for new python

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2009.0
+ Revision: 225133
- rebuild

* Wed Mar 19 2008 Lev Givon <lev@mandriva.org> 1.1-3mdv2008.1
+ Revision: 188877
- Convert to noarch package.

* Mon Feb 25 2008 Erwan Velu <erwan@mandriva.org> 1.1-2mdv2008.1
+ Revision: 175168
- Fixing url

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - fix description-line-too-long

* Sun Jan 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1.1-1mdv2008.1
+ Revision: 158794
- import python-louie


* Sun Jan 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1.1-1mdv2008.1
- First release for Mandriva.

