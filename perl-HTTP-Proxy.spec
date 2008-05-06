%define module	HTTP-Proxy
%define name	perl-%{module}
%define version 0.22
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A pure Perl HTTP proxy
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://http-proxy.mongueurs.net/
Source:		http://www.cpan.org/modules/by-module/HTTP/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Module::Build)
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The HTTP::Proxy module implements a HTTP proxy, using a HTTP::Daemon to
accept client connections, and a LWP::UserAgent to ask for the requested
pages.

The most interesting feature of this proxy object is its ability to
filter the HTTP requests and responses through user-defined filters.

%prep
%setup -q -n %{module}-%{version}
chmod 755 eg/*.pl

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README eg
%{perl_vendorlib}/HTTP/*
%{_mandir}/*/*

