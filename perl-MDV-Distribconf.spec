%define dist	MDV-Distribconf

Summary:	Read and write config of a Mandriva Linux distribution tree
Name:		perl-%{dist}
Version:	4.03
Release:	2
License:	GPLv2+
Group:		Development/Perl
Source0:	%{dist}-%{version}.tar.xz
Url:		http://search.cpan.org/dist/%{dist}/
BuildArch:	noarch
BuildRequires:	perl perl-Config-IniFiles perl-MDV-Packdrakeng

%description
MDV::Distribconf is a module to get/write the configuration of a Mandriva Linux
distribution tree.

%package -n	mdv-distrib-tools
Summary:	Tools use to maintains Mandriva distrib tree
Group:		Development/Perl

%description -n	mdv-distrib-tools
Tools use to maintains Mandriva distrib tree.

This include:
- gendistrib (experimental)
- checkdistrib

%prep
%setup -q -n %{dist}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%makeinstall_std

%files
%doc ChangeLog
%{_mandir}/*/MDV::Distribconf.*
%dir %{perl_vendorlib}/MDV/Distribconf
%{perl_vendorlib}/MDV/Distribconf.pm

%files -n mdv-distrib-tools
%{_bindir}/*
%{perl_vendorlib}/MDV/Distribconf/*
%{_mandir}/*/MDV::Distribconf::*
