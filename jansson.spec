Name:       jansson 
Version:    2.12
Release:    1%{dist}
Summary:    jansson library
License:    MIT
URL:        https://jansson.readthedocs.io/en/%{version}/

Source: http://www.digip.org/jansson/releases/%{name}-%{version}.tar.bz2

%description
Jansson is a C library for encoding, decoding and manipulating JSON data.

BuildRequires: gcc
BuildRequires: make

%prep
%setup

%configure
./configure

%build
make
make check

%install
%make_install

%files
/usr/local/include/jansson.h
/usr/local/include/jansson_config.h
/usr/local/lib/pkgconfig/jansson.pc
/usr/local/lib/libjansson.so.4.11.1
/usr/local/lib/libjansson.so.4
/usr/local/lib/libjansson.so
/usr/local/lib/libjansson.la
/usr/local/lib/libjansson.a

%changelog
* Mon Mar 02 2020 Piotr Rabiega <piotrx.rabiega@intel.com> - 2.12-1
- create package with jansson
