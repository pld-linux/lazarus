# TODO: optflags (where possible)
Summary:	Lazarus Component Library and IDE
Summary(pl.UTF-8):	Lazarus - biblioteka komponentów i IDE
Name:		lazarus
Version:	0.9.28.2
Release:	1
License:	GPL and modified LGPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/lazarus/%{name}-%{version}-src.tar.bz2
# Source0-md5:	52dc157fa1e83e90b5331820bd616d81
URL:		http://www.lazarus.freepascal.org/
Patch0:		%{name}-desktop.patch
BuildRequires:	fpc >= 2.4.0
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+2-devel
Requires:	fpc-src >= 2.4.0
Requires:	gdk-pixbuf >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		lazdir		%{_datadir}/lazarus

%description
Lazarus is a free and opensource RAD tool for freepascal using the
Lazarus Component Library (LCL), which is also included in this
package.

%description -l pl.UTF-8
Lazarus to darmowe i opensourcowe narzędzie RAD dla freepascala,
używające biblioteki komponentów LCL (Lazarus Component Library),
która jest także zawarta w tym pakiecie.

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

for i in components doceditor ide lcl units converter debugger ideintf languages localize.bat startlazarus \
designer images lazarus localize.sh packager tools ; do
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
ln -sf %{lazdir}/startlazarus $RPM_BUILD_ROOT%{_bindir}/startlazarus
ln -s %{_libdir}/lazarus $RPM_BUILD_ROOT%{_datadir}/lazarus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt docs/*.pdf
%attr(755,root,root) %{_bindir}/lazarus
%attr(755,root,root) %{_bindir}/startlazarus
%{_datadir}/lazarus
%dir %{_libdir}/lazarus
%{_libdir}/lazarus/components
%{_libdir}/lazarus/converter
%{_libdir}/lazarus/debugger
%{_libdir}/lazarus/designer
%{_libdir}/lazarus/doceditor
%{_libdir}/lazarus/docs
%{_libdir}/lazarus/ide
%{_libdir}/lazarus/ideintf
%{_libdir}/lazarus/images
%{_libdir}/lazarus/languages
%{_libdir}/lazarus/lcl
%{_libdir}/lazarus/packager
%{_libdir}/lazarus/tools
%{_libdir}/lazarus/units
%attr(755,root,root) %{_libdir}/lazarus/lazarus
%attr(755,root,root) %{_libdir}/lazarus/startlazarus
%{_pixmapsdir}/lazarus.png
%{_desktopdir}/lazarus.desktop
%{_examplesdir}/%{name}-%{version}
