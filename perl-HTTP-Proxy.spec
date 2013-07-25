%define upstream_name	 HTTP-Proxy
%define upstream_version 0.300

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.300
Release:	1

Summary:	A pure Perl HTTP proxy
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://http-proxy.mongueurs.net/
Source0:	http://www.cpan.org/modules/by-module/HTTP/HTTP-Proxy-0.300.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(HTML::Parser)
BuildArch:	noarch

%description
The HTTP::Proxy module implements a HTTP proxy, using a HTTP::Daemon to
accept client connections, and a LWP::UserAgent to ask for the requested
pages.

The most interesting feature of this proxy object is its ability to
filter the HTTP requests and responses through user-defined filters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 755 eg/*.pl

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README eg
%{perl_vendorlib}/HTTP/*
%{_mandir}/*/*

%changelog
* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.0
+ Revision: 399299
- update to 0.24
- using %%perl_convert_version
- fixed license field

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.0
+ Revision: 281103
- update to new version 0.23

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.22-2mdv2009.0
+ Revision: 268526
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.0
+ Revision: 202320
- update to new version 0.22

* Wed Apr 23 2008 Jérôme Quelin <jquelin@mandriva.org> 0.21-2mdv2009.0
+ Revision: 196892
- rebuild

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.0
+ Revision: 196140
- update to new version 0.21

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.20-1mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 17:20:37 (59608)
- 0.20

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 17:18:41 (59607)
Import perl-HTTP-Proxy

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2007.0
- new version 
- rpmbuildupdate aware
- spec cleanup

* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- 0.18

* Sat Oct 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-1mdk
- 0.17

* Mon Sep 19 2005 Pascal Terjan <pterjan@mandriva.org> 0.16-2mdk
- BuildRequires perl-Module-Build

* Thu Sep 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- 0.16

* Thu Apr 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- 0.15

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.13-2mdk
- BuildRequires

* Wed Aug 25 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.13-1mdk
- Initial MDK release.


