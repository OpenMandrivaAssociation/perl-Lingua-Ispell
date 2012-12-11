%define upstream_name    Lingua-Ispell
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Ispell inteface perl module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JD/JDPORTER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Interface to the Ispell spellchecker.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 407790
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.07-15mdv2009.0
+ Revision: 257538
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.07-14mdv2009.0
+ Revision: 245621
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.07-12mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-12mdv2008.0
+ Revision: 86521
- rebuild


* Thu May 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-11mdk
- Fix Build

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-10mdk
- Remove -q

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.07-9mdk
- rebuild for new auto{prov,req}

