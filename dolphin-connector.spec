%define svn_version g5f75edb

Name: dolphin-connector
Summary: Simple MySQL C API wrapper for C++
Version: 1.2
Release: 6
License: BSD
Group: Development/C++
Source: http://github.com/poetinha/dolphin-connector/tarball/master/poetinha-%{name}-v%{version}-1-%{svn_version}.tar.gz
URL:	https://github.com/poetinha/dolphin-connector
BuildRequires: boost-static-devel, mysql-devel, automake

%description
Dolphin Connector is a simples MySQL C API wrapper for C++, It is originally
designed to be as efficient as is possible, and makes no use of exceptions

%package  devel
Summary: Development files for Dolphin Connector
Group: Development/C++
Requires: %{name} = %{version}-%{release}
Requires: mysql-devel
Requires: boost-devel

%description devel
Dolphin Connector development package

%prep
%setup -q -n poetinha-%{name}-5f75edb 

%build
./autogen.sh

########./configure --prefix=/usr/ --disable-static
%configure
%make

%install
%make_install

cd include/
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

rm -f sample/Makefile*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc sample
%{_includedir}/dolphinconn
%{_libdir}/*.so



%changelog
* Thu Sep 22 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.2-4mdv2012.0
+ Revision: 700988
- change the package license
- add devel package
- changes on spec file

* Tue Sep 06 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.2-1
+ Revision: 698382
- first mandriva version
- Created package structure for dolphin-connector.

