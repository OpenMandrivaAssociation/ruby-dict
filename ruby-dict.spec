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


