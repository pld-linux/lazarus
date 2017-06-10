# TODO: optflags (where possible)
Summary:	Lazarus Component Library and IDE
Summary(pl.UTF-8):	Lazarus - biblioteka komponentów i IDE
Name:		lazarus
Version:	1.6.0
Release:	2
License:	GPL v2, modified LGPL, MPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/lazarus/%{name}-%{version}-0.tar.gz
# Source0-md5:	1857ee87efa9cb0fdecf8e414f4794ca
Patch0:		%{name}-desktop.patch
URL:		http://www.lazarus.freepascal.org/
BuildRequires:	fpc >= 3.0.0
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+2-devel
%requires_eq	fpc
Requires:	fpc-src >= 3.0.0
Requires:	gdk-pixbuf >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Stabs debuginfo not supported
%define		_enable_debug_packages	0

%define		lazdir		%{_libdir}/lazarus

%description
Lazarus is a free and opensource RAD tool for freepascal using the
Lazarus Component Library (LCL), which is also included in this
package.

%description -l pl.UTF-8
Lazarus to wolnodostępne i mające otwarte źródła narzędzie RAD dla
freepascala, wykorzystujące bibliotekę komponentów LCL (Lazarus
Component Library), która jest także zawarta w tym pakiecie.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_libdir}/lazarus/docs,%{_pixmapsdir},%{_desktopdir},%{_bindir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

for i in components doceditor ide lcl units converter debugger languages startlazarus \
		designer images lazarus lazbuild packager tools ; do
	cp -a $i $RPM_BUILD_ROOT%{_libdir}/lazarus
done

cp -a docs/*.html $RPM_BUILD_ROOT%{_libdir}/lazarus/docs
cp -a docs/html $RPM_BUILD_ROOT%{_libdir}/lazarus/docs
cp -a docs/images $RPM_BUILD_ROOT%{_libdir}/lazarus/docs
cp -a docs/xml $RPM_BUILD_ROOT%{_libdir}/lazarus/docs
install docs/Contributors.txt $RPM_BUILD_ROOT%{_libdir}/lazarus/docs

install images/ide_icon48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/lazarus.png
install install/lazarus.desktop $RPM_BUILD_ROOT%{_desktopdir}/lazarus.desktop
ln -sf %{lazdir}/lazarus $RPM_BUILD_ROOT%{_bindir}/lazarus
ln -sf %{lazdir}/lazarus $RPM_BUILD_ROOT%{_bindir}/lazbuild
ln -sf %{lazdir}/startlazarus $RPM_BUILD_ROOT%{_bindir}/startlazarus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt COPYING.modifiedLGPL.txt docs/*.txt docs/*.pdf
%attr(755,root,root) %{_bindir}/lazarus
%attr(755,root,root) %{_bindir}/lazbuild
%attr(755,root,root) %{_bindir}/startlazarus
%dir %{_libdir}/lazarus
%{_libdir}/lazarus/components
%{_libdir}/lazarus/converter
%{_libdir}/lazarus/debugger
%{_libdir}/lazarus/designer
%{_libdir}/lazarus/doceditor
%{_libdir}/lazarus/docs
%{_libdir}/lazarus/ide
%{_libdir}/lazarus/images
%{_libdir}/lazarus/languages
%{_libdir}/lazarus/lcl
%{_libdir}/lazarus/packager
%{_libdir}/lazarus/tools
%{_libdir}/lazarus/units
%attr(755,root,root) %{_libdir}/lazarus/lazarus
%attr(755,root,root) %{_libdir}/lazarus/lazbuild
%attr(755,root,root) %{_libdir}/lazarus/startlazarus
%{_pixmapsdir}/lazarus.png
%{_desktopdir}/lazarus.desktop
%{_examplesdir}/%{name}-%{version}
