Summary:	Lazarus Component Library and IDE
Summary(pl):	Lazarus - biblioteka komponentów i IDE
Name:		lazarus
Version:	0.9.14
Release:	0.1
License:	GPL and modified LGPL
Group:		Development/Tools
Source0:        http://dl.sourceforge.net/lazarus/%{name}-%{version}-1.tar.gz 
# Source0-md5:	7ee733185e5f0dc10f6c7084e1505c60
URL:		http://www.lazarus.freepascal.org/
BuildRequires:	fpc >= 2.0.2
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	glibc-devel
Requires:	fpc-src >= 2.0.2
Requires:	gdk-pixbuf >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		lazdir		%{_datadir}/lazarus

%description
Lazarus is a free and opensource RAD tool for freepascal using the
Lazarus Component Library (LCL), which is also included in this
package.

%description -l pl
Lazarus to darmowe i opensourcowe narzêdzie RAD dla freepascala,
u¿ywaj±ce biblioteki komponentów LCL (Lazarus Component Library),
która jest tak¿e zawarta w tym pakiecie.

%prep
%setup -q -n %{name}

%build

%{__make}
strip lazarus
strip startlazarus

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/lazarus,%{_pixmapsdir},%{_desktopdir},%{_bindir}} \
        $RPM_BUILD_ROOT%{_examplesdir}/%{name}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

for i in components docs doceditor ide lcl units converter debugger ideintf languages localize.bat startlazarus \
designer images lazarus localize.sh packager tools ; do
cp -a $i $RPM_BUILD_ROOT%{_datadir}/lazarus
done

install images/ide_icon48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/lazarus.png
install install/lazarus.desktop $RPM_BUILD_ROOT%{_desktopdir}/lazarus.desktop
ln -sf %{lazdir}/lazarus $RPM_BUILD_ROOT%{_bindir}/lazarus
ln -sf %{lazdir}/startlazarus $RPM_BUILD_ROOT%{_bindir}/startlazarus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* README
%attr(755,root,root) %{_bindir}/lazarus
%attr(755,root,root) %{_bindir}/startlazarus
%{_datadir}/lazarus
%attr(755,root,root) %{_datadir}/lazarus/lazarus
%attr(755,root,root) %{_datadir}/lazarus/startlazarus
%{_pixmapsdir}/lazarus.png
%{_desktopdir}/lazarus.desktop
%{_examplesdir}/%{name}
