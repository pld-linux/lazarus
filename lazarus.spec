Summary:	Lazarus Component Library and IDE.
Summary(pl):	Lazarus - komponenty biblioteki i IDE.
Name:		lazarus
Version:	0.9.2.4
%define _rel	041207
Release:	0.1
License:	LGPL2/GPL2
Group:		Development/Tools
Source0:        http://dl.sourceforge.net/lazarus/lazarus-%{_rel}.tgz
# Source0-md5:	f7572e3a94211ae063830889c64e77f1
URL:		http://www.lazarus.freepascal.org/
BuildRequires:	fpc >= 1.0.10
Requires:	fpcsrc >= 1.9.5
Requires:	gdk-pixbuf-devel >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define lazdir %{_datadir}/lazarus

%description
Lazarus is a free and opensource RAD tool for freepascal using the
lazarus component library - LCL, which is also included in this
package.


%description -l pl
Lazarus to darmowe i opensourcowe narzêdzie RAD dla freepascala
u¿ywaj±ce lazarus component library - LCL, które jest tak¿e zawarte w
tej paczce.

%prep
%setup -q -n %{name}


%build
%{__make}
  


%install
rm -rf $RPM_BUILD_ROOT
 install -d $RPM_BUILD_ROOT{%{_datadir}/%{lazarus,pixmaps,gnome/apps/Development,applications},%{_bindir},}


  cp -a lazarus/* $RPM_BUILD_ROOT%{_datadir}/lazarus/
  install  lazarus/images/ide_icon48x48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/lazarus.png
  install  lazarus/gnome.ide.desktop $RPM_BUILD_ROOT%{_applnkdir}/Development/lazarus.desktop
  install  lazarus/gnome.ide.desktop $RPM_BUILD_ROOT%{_datadir}/applications/lazarus.desktop
  ln -sf %{lazdir}/lazarus $RPM_BUILD_ROOT%{_bindir}/lazarus

%clean
  rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_datadir}/lazarus
%attr(755,root,root) %{_bindir}/lazarus
%{_datadir}/pixmaps/lazarus.png
%{_applnkdir}/Development/lazarus.desktop
%{_datadir}/applications/lazarus.desktop
