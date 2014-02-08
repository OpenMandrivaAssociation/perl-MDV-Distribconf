%define dist	MDV-Distribconf

Summary:	Read and write config of a Mandriva Linux distribution tree
Name:		perl-%{dist}
Version:	4.03
Release:	8
License:	GPLv2+
Group:		Development/Perl
Source0:	%{dist}-%{version}.tar.xz
Url:		http://search.cpan.org/dist/%{dist}/
BuildArch:	noarch
BuildRequires:	perl
BuildRequires:	perl-Config-IniFiles
BuildRequires:	perl-MDV-Packdrakeng
BuildRequires:	perl-devel

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
%make

%check
make test

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 4.03-4
+ Revision: 765479
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 4.03-3
+ Revision: 763973
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 4.03-2
+ Revision: 763089
- rebuild

* Fri Apr 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.03-1
+ Revision: 656592
- update license tag
- drop legacy junk
- fix incorrectly written VERSION files
- fix parsing of VERSION files

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 4.02-2mdv2011.0
+ Revision: 556991
- rebuild

  + Christophe Fergeau <cfergeau@mandriva.com>
    - drop unused perl-RPM4 BuildRequires

* Fri Feb 19 2010 Christophe Fergeau <cfergeau@mandriva.com> 4.02-1mdv2010.1
+ Revision: 508139
- 4.02:
- 4.01 tarball was bogus and didn't contain the fix that was the reason for
  the release

* Wed Sep 30 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.01-1mdv2010.0
+ Revision: 451233
- 4.01

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.00-4mdv2010.0
+ Revision: 426518
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 4.00-3mdv2009.1
+ Revision: 351852
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 4.00-2mdv2009.0
+ Revision: 223818
- rebuild

* Thu Jan 17 2008 Olivier Thauvin <nanardon@mandriva.org> 4.00-1mdv2008.1
+ Revision: 154304
- 4.00

* Sun Dec 30 2007 Olivier Thauvin <nanardon@mandriva.org> 3.14-1mdv2008.1
+ Revision: 139437
- 3.14 (fix undef warning in case of brken link, then count thoses files as missing)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Olivier Thauvin <nanardon@mandriva.org> 3.13-1mdv2008.1
+ Revision: 108607
- 3.13

* Sun Nov 11 2007 Olivier Thauvin <nanardon@mandriva.org> 3.12-1mdv2008.1
+ Revision: 107961
- 3.12

* Fri Nov 09 2007 Olivier Thauvin <nanardon@mandriva.org> 3.11-1mdv2008.1
+ Revision: 107072
- 3.11

* Fri Jul 20 2007 Olivier Thauvin <nanardon@mandriva.org> 3.10-1mdv2008.0
+ Revision: 54063
- 3.10

* Fri Jul 06 2007 Olivier Thauvin <nanardon@mandriva.org> 3.09-0.1mdv2008.0
+ Revision: 48966
- 3.09

* Tue Jul 03 2007 Olivier Thauvin <nanardon@mandriva.org> 3.08-1mdv2008.0
+ Revision: 47533
- 3.08


* Mon Feb 19 2007 Olivier Thauvin <nanardon@mandriva.org> 3.07-1mdv2007.0
+ Revision: 122735
- 3.07

* Sat Sep 09 2006 Olivier Thauvin <nanardon@mandriva.org> 3.06-1mdv2007.0
+ Revision: 60646
- 3.06

* Sat Aug 26 2006 Olivier Thauvin <nanardon@mandriva.org> 3.05-1mdv2007.0
+ Revision: 58015
- 3.05

* Fri Aug 25 2006 Olivier Thauvin <nanardon@mandriva.org> 3.04-1mdv2007.0
+ Revision: 57913
- 3.04

* Wed Aug 23 2006 Olivier Thauvin <nanardon@mandriva.org> 3.03-2mdv2007.0
+ Revision: 57513
- fix buildrequires

* Wed Aug 23 2006 Olivier Thauvin <nanardon@mandriva.org> 3.03-1mdv2007.0
+ Revision: 57490
- 3.03

* Wed Aug 23 2006 Olivier Thauvin <nanardon@mandriva.org> 3.02-1mdv2007.0
+ Revision: 57078
- 3.02

* Tue Aug 22 2006 Olivier Thauvin <nanardon@mandriva.org> 3.01-1mdv2007.0
+ Revision: 57003
- 3.01

* Tue Aug 22 2006 Olivier Thauvin <nanardon@mandriva.org> 3.00-1mdv2007.0
+ Revision: 56950
- bump release

* Tue Aug 22 2006 Olivier Thauvin <nanardon@mandriva.org> 3.00-0.1mdv2007.0
+ Revision: 56945
- 3.00

* Sun Aug 20 2006 Olivier Thauvin <nanardon@mandriva.org> 2.04-1mdv2007.0
+ Revision: 56868
- 2.04

* Sat Aug 19 2006 Olivier Thauvin <nanardon@mandriva.org> 2.03-1mdv2007.0
+ Revision: 56787
- 2.03

* Tue Jul 25 2006 Olivier Thauvin <nanardon@mandriva.org> 2.02-1mdv2007.0
+ Revision: 41983
- add sources
- 2.02

* Fri Jul 21 2006 Olivier Thauvin <nanardon@mandriva.org> 2.01-1mdv2007.0
+ Revision: 41770
- 2.01
- 2.00
- Import perl-MDV-Distribconf

* Tue Dec 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-1mdk
- 1.01

* Sat Oct 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-1mdk
- Initial MDV release

