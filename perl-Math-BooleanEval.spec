#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	BooleanEval
Summary:	Math::BooleanEval Perl module - Boolean expression parser
Summary(pl.UTF-8):	Moduł Perla Math::BooleanEval - analiza wyrażeń logicznych
Name:		perl-Math-BooleanEval
Version:	1.00
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1400c67b1d3ab47a9c44d88b62c9aa3a
URL:		http://search.cpan.org/dist/Math-BooleanEval/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BooleanEval parses a boolean expression and creates an array of
elements in the expression. By setting each element to 1 or 0 you can
evaluate the expression.

%description -l pl.UTF-8
BooleanEval analizuje wyrażenie logiczne i tworzy tablicę składników
wyrażenia. Poprzez ustawienie każdego elementu na 1 lub 0 można
obliczyć wyrażenie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/BooleanEval.pm
%{_mandir}/man3/*
