%define debug_package %{nil}

%define upstream_name    Lingua-Ispell
Name:		perl-%{upstream_name}
Version:	0.07
Release:	7

Summary:	Ispell inteface perl module
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Lingua-Ispell
Source0:	https://cpan.metacpan.org/authors/id/J/JD/JDPORTER/Lingua-Ispell-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Interface to the Ispell spellchecker.

%prep 
%setup -q -n %{upstream_name}-%{version}

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

