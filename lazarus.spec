Summary:	Lazarus Component Library and IDE
Summary(pl):	Lazarus - biblioteka komponentów i IDE
Name:		lazarus
Version:	0.9.2.4
%define _snap	041207
Release:	0.1
License:	LGPL v2/GPL v2
Group:		Development/Tools
Source0:        http://dl.sourceforge.net/lazarus/lazarus-%{_snap}.tgz
# Source0-md5:	f7572e3a94211ae063830889c64e77f1
URL:		http://www.lazarus.freepascal.org/
BuildRequires:	fpc >= 1.0.10
# is it noarch??? if not, it's heavily broken (binaries in datadir, no optflags)
BuildRequires:	noarch-or-FHS+optflags
Requires:	fpcsrc >= 1.9.5
Requires:	gdk-pixbuf-devel >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		lazdir		%{_datadir}/lazarus

%description
Lazarus is a free and opensource RAD tool for freepascal using the
Lazarus Component Library (LCL), which is also included in this
package.

%description -l pl
Lazarus to darmowe i opensourcowe narzêdzie RAD dla freepascala
u¿ywaj±ce biblioteki komponentów LCL (Lazarus Component Library),
która jest tak¿e zawarte w tym pakiecie.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/lazarus,%{_pixmapsdir},%{_desktopdir},%{_bindir}} \
        $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{_snap}

install exampels/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{_snap}

cp -a lazarus/* $RPM_BUILD_ROOT%{_datadir}/lazarus
install lazarus/images/ide_icon48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/lazarus.png
install lazarus/gnome.ide.desktop $RPM_BUILD_ROOT%{_desktopdir}/lazarus.desktop
ln -sf %{lazdir}/lazarus $RPM_BUILD_ROOT%{_bindir}/lazarus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* README
%attr(755,root,root) %{_bindir}/lazarus
%{_datadir}/lazarus
%{_pixmapsdir}/lazarus.png
%{_desktopdir}/lazarus.desktop
%{_examplesdir}/%{name}-%{_snap}
