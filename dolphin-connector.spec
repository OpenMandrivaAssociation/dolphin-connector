%define svn_version g5f75edb

Name: dolphin-connector
Summary: Dolphin Connector is a simple MySQL C API wrapper for C++. It is originally designed to be as efficient as is possible
Version: 1.2
Release: %mkrel 3
License: BSD
Group: Development/C++
Source: http://github.com/poetinha/dolphin-connector/tarball/master/poetinha-%{name}-v%{version}-1-%{svn_version}.tar.gz
URL:	http://github.com/poetinha/dolphin-connector
BuildRequires: boost-static-devel, mysql-devel
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
Dolphin Connector is a simples MySQL C API wrapper for C++, It is originally designed to be as efficient as is possible, and makes no use of exceptions

%package  devel
Summary: Development files for Dolphin Connector
Group: Development/C++
Requires: %{name} = %{version}-%{release}
Requires: mysql-devel
Requires: boost-devel

%description devel
Dolphin Connector development package

%prep
rm -rf %{buildroot}
%setup -q -n poetinha-%{name}-5f75edb 

%build
./autogen.sh

./configure --prefix=/usr/ --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

cd include/
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

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


%clean
rm -rf $RPM_BUILD_ROOT
