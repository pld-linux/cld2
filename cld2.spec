Summary:	Compact Language Detector 2
Summary(pl.UTF-8):	Biblioteka wykrywania języka Compact Language Detector 2
Name:		cld2
Version:	0
%define	gitref	b56fa78a2fe44ac2851bae5bf4f4693a0644da7b
%define	snap	20150821
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	Apache v2.0
Group:		Libraries
Source0:	https://github.com/CLD2Owners/cld2/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	6a23d18bd8fbf50d5d85374888ee000b
# from https://github.com/cyrusimap/cld2
Patch0:		%{name}-build-cyrus.patch
Patch1:		%{name}-install.patch
URL:		https://github.com/CLD2Owners/cld2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLD2 probabilistically detects over 80 languages in Unicode UTF-8
text, either plain text or HTML/XML.

%description -l pl.UTF-8
CLD2 wykrywa probabilistycznie ponad 80 języków w tekście unikodowym
UTF-8, zarówno czystym, jak i HTML/XML.

%package devel
Summary:	Header files for CLD2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CLD2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for CLD2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CLD2.

%prep
%setup -q -n %{name}-%{gitref}
%patch -P0 -p1
%patch -P1 -p1

%build
cd internal
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags} -std=c++98" \
./compile_libs.sh

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
./install.sh \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%{_libdir}/libcld2.so
%{_libdir}/libcld2_full.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/cld2
%{_pkgconfigdir}/cld2.pc
