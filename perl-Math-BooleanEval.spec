#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BooleanEval
Summary:	Math::BooleanEval Perl module - Boolean expression parser
Summary(pl):	Modu� Perla Math::BooleanEval - analiza wyra�e� logicznych
Name:		perl-Math-BooleanEval
Version:	1.00
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BooleanEval parses a boolean expression and creates an array of
elements in the expression. By setting each element to 1 or 0 you can
evaluate the expression.

%description -l pl
BooleanEval analizuje wyra�enie logiczne i tworzy tablic� sk�adnik�w
wyra�enia. Poprzez ustawienie ka�dego elementu na 1 lub 0 mo�na
obliczy� wyra�enie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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