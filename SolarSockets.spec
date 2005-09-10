#
%define	_gccver_ix86	3.4.2
%define	_gccver_x86_64	3.4.2
Summary:	Easy network socket library
Name:		SolarSockets
Version:	0.4.0
Release:	0.1
License:	Free for non comercial use
Vendor:		Solar-OpenSource.Com
Group:		Libraries
Source0:	http://dl.sourceforge.net/solarirc/%{name}-%{version}-GCC%{_gccver_ix86}.i386.tgz
# NoSource0-md5:	b037bd7e00a788524c3669a44f3f807f
Source1:	http://dl.sourceforge.net/solarirc/%{name}-%{version}-GCC%{_gccver_x86_64}.x86_64.tgz
# NoSource1-md5:	aea57a8abb555dc6ef11f843e677debb
URL:		http://solarirc.sourceforge.net/solarsockets/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy network socket library.

Warning: this library from time to time connects to Solar OpenSource server
for track use statistics.

%package devel
Summary:	Developement files
Requires:	%{name} = %{version}-%{release}
Group:		Development/Libraries

%description devel
Developement files.

%package static
Summary:	Static library
Requires:	%{name}-devel = %{version}-%{release}
Group:		Development/Libraries

%description static
Static library.

%prep
%setup -q -T -c -a0 -a1
%ifarch %{ix86}
mv %{name}-%{version}-GCC%{_gccver_ix86}.i386/* .
%else
mv %{name}-%{version}-GCC%{_gccver_x86_64}.x86_64/* .
%endif
mv README{,.es}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}}

install lib/* $RPM_BUILD_ROOT%{_libdir}
tr "\r" "\n" < include/%{name}.h \
	> $RPM_BUILD_ROOT%{_includedir}/%{name}/%{name}.h

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.es
%attr(755,root,root) %{_libdir}/libsolarsockets.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsolarsockets.so
%{_libdir}/libsolarsockets.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libsolarsockets.a
