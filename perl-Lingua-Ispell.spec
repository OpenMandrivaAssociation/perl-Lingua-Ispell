%define debug_package %{nil}

%define upstream_name    Lingua-Ispell
%define upstream_version 0.07
Name:		perl-%{upstream_name}
Version:	0.07
Release:	3

Summary:	Ispell inteface perl module
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Lingua-Ispell
Source0:	https://cpan.metacpan.org/authors/id/J/JD/JDPORTER/Lingua-Ispell-0.07.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Interface to the Ispell spellchecker.

%prep 
%setup -q -n Lingua-Ispell-0.07

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%check
make test || :

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/Lingua/*
%{_mandir}/*/*

