Summary:	Nagios performance data storage and graphing
Name:		nagios-nagiosgraph
Version:	1.4.4
Release:	0.4
License:	Artistic
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/nagiosgraph/nagiosgraph-%{version}.tar.gz
# Source0-md5:	b340aa461a4c4a4621089413af729524
URL:		http://nagiosgraph.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-cgi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/nagiosgraph
%define		cgidir		%{_libdir}/nagios/cgi
%define		webdir		%{_datadir}/nagios
%define		vardir		/var/lib/nagios/nagiosgraph
%define		rrddir		%{vardir}/rrd

%description
nagiosgraph parses output and performance data from Nagios plugins,
stores the data in RRD files, and creates graphs and reports from the
data.

Graphs and reports can be embedded in Nagios. Easy to setup, highly
customizable, and few dependencies.

%prep
%setup -q -n nagiosgraph-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{cgidir},%{webdir},%{rrddir}}
cp -a etc/* $RPM_BUILD_ROOT%{_sysconfdir}
install -p lib/insert.pl $RPM_BUILD_ROOT%{_libdir}/nagios/%{name}.pl
install -p cgi/*.cgi $RPM_BUILD_ROOT%{_libdir}/nagios/cgi
cp -a share/nagiosgraph.css $RPM_BUILD_ROOT%{webdir}
cp -a share/nagiosgraph.js $RPM_BUILD_ROOT%{webdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG INSTALL README TODO
%dir %{_sysconfdir}
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/access.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/datasetdb.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/groupdb.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hostdb.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/labels.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/map
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nagiosgraph.conf
%lang(de) %attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nagiosgraph_de.conf
%lang(es) %attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nagiosgraph_es.conf
%lang(fr) %attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nagiosgraph_fr.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ngshared.pm
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rrdopts.conf
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/servdb.conf
%attr(755,root,root) %{cgidir}/show.cgi
%attr(755,root,root) %{cgidir}/showgraph.cgi
%attr(755,root,root) %{cgidir}/showgroup.cgi
%attr(755,root,root) %{cgidir}/showhost.cgi
%attr(755,root,root) %{cgidir}/showservice.cgi
%attr(755,root,root) %{cgidir}/testcolor.cgi
%attr(755,root,root) %{_libdir}/nagios/%{name}.pl
%{webdir}/nagiosgraph.css
%{webdir}/nagiosgraph.js

%dir %attr(775,root,nagios) %{vardir}
%dir %attr(775,root,nagios) %{rrddir}
