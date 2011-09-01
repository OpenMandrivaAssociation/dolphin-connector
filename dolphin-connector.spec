%define svn_version g5f75edb

Name: dolphin-connector
Summary: Dolphin Connector is a simple MySQL C API wrapper for C++. It is originally designed to be as efficient as is possible
Version: 1.2
Release: %mkrel 1
License: GPLv3
Group: Development/C++
Source: http://github.com/poetinha/dolphin-connector/tarball/master/poetinha-%{name}-v%{version}-1-%{svn_version}.tar.gz
URL:	http://github.com/poetinha/dolphin-connector
BuildRequires: libboost-static-devel, libmysql-devel
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
Dolphin Connector is a simples MySQL C API wrapper for C++, It is originally designed to be as efficient as is possible, and makes no use of exceptions


%prep
rm -rf %{buildroot}
%setup -q -n poetinha-%{name}-5f75edb 

%build
./autogen.sh

./configure

%install
mkdir -p %{buildroot}/usr/local/lib/
%make

make install DESTDIR=%{buildroot}/usr/local/lib/


%files
%defattr(0755,root,root)
/usr/local/lib/*

%clean
rm -rf $RPM_BUILD_ROOT
