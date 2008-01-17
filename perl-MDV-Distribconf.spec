%define dist	MDV-Distribconf
%define version	4.00
%define release	%mkrel 1

Summary:	Read and write config of a Mandriva Linux distribution tree
Name:		perl-%{dist}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source0:	%{dist}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{dist}/
BuildRoot:	%{_tmppath}/%{name}-buildroot/
BuildArch:	noarch
BuildRequires:	perl perl-Config-IniFiles perl-MDV-Packdrakeng
BuildRequires:  perl(RPM4)

%description
MDV::Distribconf is a module to get/write the configuration of a Mandriva Linux
distribution tree.

%package -n mdv-distrib-tools
Summary: Tools use to maintains Mandriva distrib tree
Group: Development/Perl

%description -n mdv-distrib-tools
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/*/MDV::Distribconf.*
%dir %{perl_vendorlib}/MDV/Distribconf
%{perl_vendorlib}/MDV/Distribconf.pm

%files -n mdv-distrib-tools
%defattr(-,root,root)
%_bindir/*
%{perl_vendorlib}/MDV/Distribconf/*
%{_mandir}/*/MDV::Distribconf::*

