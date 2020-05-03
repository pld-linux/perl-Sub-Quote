#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Sub
%define		pnam	Quote
Summary:	Sub::Quote - Efficient generation of subroutines via string eval
Summary(pl.UTF-8):	Sub::Quote - wydajne generowanie podprocedur poprzez ewaluację łańcuchów znaków
Name:		perl-Sub-Quote
Version:	2.006006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1bb9caee697bcfa738f419d40505e506
URL:		https://metacpan.org/release/Sub-Quote
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Fatal >= 0.003
BuildRequires:	perl-Test-Simple >= 0.94
%endif
Conflicts:	perl-Moo < 2.003000
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides performant ways to generate subroutines from
strings.

%description -l pl.UTF-8
Ten pakiet udostępnia wydajne sposoby generowania podprocedur z
łańcuchów znaków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/Defer.pm
%{perl_vendorlib}/Sub/Quote.pm
%{_mandir}/man3/Sub::Defer.3pm*
%{_mandir}/man3/Sub::Quote.3pm*
