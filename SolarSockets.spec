%define	_gccver_ix86	3.3.3
%define	_gccver_x86_64	3.4.2
%ifarch %{ix86}
%define	_gccver	%{_gccver_ix86}
%else
%define	_gccver	%{_gccver_x86_64}
%endif
Summary:	Easy network socket library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do gniazd
Name:		SolarSockets
Version:	0.4.0
%define	_rel	0.1
Release:	%{_rel}@%{_gccver}
License:	Free for non comercial use
Vendor:		Solar-OpenSource.Com
Group:		Libraries
Source0:	http://dl.sourceforge.net/solarirc/%{name}-%{version}-GCC%{_gccver_ix86}.i386.tgz
# NoSource0-md5:	45190052e0d0cafc9cf71016b4ea064d
Source1:	http://dl.sourceforge.net/solarirc/%{name}-%{version}-GCC%{_gccver_x86_64}.x86_64.tgz
# NoSource1-md5:	aea57a8abb555dc6ef11f843e677debb
NoSource:	0
NoSource:	1
URL:		http://solarirc.sourceforge.net/solarsockets/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy network socket library.

Warning: this library from time to time connects to Solar OpenSource
server for track use statistics.

%description -l pl.UTF-8
Łatwa w użyciu biblioteka do gniazd.

Uwaga: ta biblioteka od czasu do czasu łączy się z serwerem Solar
OpenSource w celu uzyskania statystyk użycia.

%package devel
Summary:	Developement files for SolarSockets library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki SolarSockets
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Developement files for SolarSockets library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki SolarSockets.

%package static
Summary:	Static SolarSockets library
Summary(pl.UTF-8):	Statyczna biblioteka SolarSockets
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SolarSockets library.

%description static -l pl.UTF-8
Statyczna biblioteka SolarSockets.

%prep
%setup -q -T -c -a0 -a1
%ifarch %{ix86}
mv %{name}-%{version}-GCC%{_gccver_ix86}.i386/* .
%else
mv %{name}-%{version}-GCC%{_gccver_x86_64}.x86_64/* .
%endif
mv README{,.es}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}}

install lib/* $RPM_BUILD_ROOT%{_libdir}
tr "\r" "\n" < include/%{name}.h \
	> $RPM_BUILD_ROOT%{_includedir}/%{name}/%{name}.h

%clean
rm -rf $RPM_BUILD_ROOT

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
