Summary: Ruby/DICT library
Name: ruby-dict
Version: 0.9.4
Release: %mkrel 3
License: GPLv2+
Group: Development/Ruby
Source: http://www.caliban.org/files/ruby/%{name}-%{version}.tar.gz
URL: http://www.caliban.org/ruby/
BuildRoot: /var/tmp/%{name}-%{version}
BuildArch: noarch
BuildRequires: ruby

%description
Ruby/DICT is an RFC 2229 compliant client-side library implementation of the
DICT protocol, written in the Ruby programming language. It can be used to
write clients that access dictionary definitions from a set of natural
language dictionary databases.

In addition, rdict, a dictionary client built on Ruby/DICT, is included.


%prep
%setup
make config ROOT=%{buildroot}%{_prefix}
make setup


%clean 
rm -rf %{buildroot}


%install
rm -rf %{buildroot}
make install ROOT=%{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_mandir}/man{1,3}
install doc/dict.3 %{buildroot}%{_mandir}/man3/dict.3
install doc/rdict.1 %{buildroot}%{_mandir}/man1/rdict.1


%files
%defattr(-,root,root)
%doc Changelog COPYING doc/dict.html doc/rdict.html doc/rfc2229.txt README TODO
%{_bindir}/rdict
%{ruby_sitelibdir}/dict.rb
%{_mandir}/man1/rdict.1.*
%{_mandir}/man3/dict.3.*




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9.4-3mdv2010.0
+ Revision: 433496
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.4-2mdv2009.0
+ Revision: 269232
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 13 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.9.4-1mdv2009.0
+ Revision: 218669
- import ruby-dict


* Fri Jun 13 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.9.4-1mdv2009.0
- spec ported to Mandriva

* Sun May 20 2007 Ian Macdonald <ian@caliban.org> 0.9.4-1
- 0.9.4
- Server banner handling treated capabilities string as mandatory and didn't
  allow for null message IDs.

* Thu May 26 2005 Ian Macdonald <ian@caliban.org> 0.9.3-1
- 0.9.3
- Fix bug whereby text response could be mistaken for numeric status response.

* Wed Jun 10 2003 Ian Macdonald <ian@caliban.org>
- 0.9.2
- Print a message when a non-default matching strategy is used with rdict
  and no definitions are found.
- Fix a warning when run with Ruby 1.8.

* Thu Jan  2 2003 Ian Macdonald <ian@caliban.org>
- 0.9.1
- Allow multiple words to be specified on the command line of rdict.

* Fri May 24 2002 Ian Macdonald <ian@caliban.org>
- 0.9.0
