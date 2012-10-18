%define		plugin	agility
Summary:	Agility.js JavaScript MVC library
Name:		jquery-%{plugin}
Version:	0.1.3
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/arturadib/agility/tarball/%{version}/%{plugin}-%{version}.tgz
# Source0-md5:	83e400b740f711b4e835d16bab33a024
URL:		http://agilityjs.com/
Requires:	jquery >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Agility.js is an MVC library for JavaScript that lets you write
maintainable and reusable browser code without the verbose or
infrastructural overhead found in other MVC libraries. The goal is to
enable developers to write web apps at least as quickly as with
jQuery, while simplifying long-term maintainability through MVC
objects.

%prep
%setup -qc
mv *-%{plugin}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p docs/%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p %{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE ChangeLog
%{_appdir}
