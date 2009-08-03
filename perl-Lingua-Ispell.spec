%define upstream_name    Lingua-Ispell
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Ispell inteface perl module
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JD/JDPORTER/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Interface to the Ispell spellchecker

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
rm -rf $RPM_BUILD_DIR/%{upstream_name}-%{upstream_version}

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*
