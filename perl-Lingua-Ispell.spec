%define name perl-Lingua-Ispell
%define realname Lingua-Ispell
%define version 0.07
%define release %mkrel 15

Name:		%{name}
Summary:	Ispell inteface perl module
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/J/JD/JDPORTER/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
Buildroot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
Interface to the Ispell spellchecker

%prep 

%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test


%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT


%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
rm -rf $RPM_BUILD_DIR/%{realname}-%{version}


%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*

