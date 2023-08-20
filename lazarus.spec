Summary:	Lazarus Component Library and IDE
Summary(pl.UTF-8):	Lazarus - biblioteka komponentów i IDE
Name:		lazarus
Version:	2.2.6
Release:	1
License:	GPL v2, modified LGPL, MPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/lazarus/%{name}-%{version}-0.tar.gz
# Source0-md5:	51ca9d8351c368d8c3f7e89734fc17f1
Source1:	lazarus.appdata.xml
Patch0:		%{name}-desktop.patch
Patch1:		deprecated-unit.patch
Patch2:		libdir.patch
URL:		http://www.lazarus.freepascal.org/
BuildRequires:	fpc >= 3.2.0
BuildRequires:	gtk+3-devel
%requires_eq	fpc
Requires:	fpc-src >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch1 -p1
%patch2 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+perl(\s|$),#!%{__perl}\1,' \
      docs/xml/multi_makeskel.pl \
      tools/delete_non_svn_files.pl \
      tools/install/replace_in_files.pl

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+bash(\s|$),#!/bin/bash\1,' \
      components/lazreport/tools/localize.sh \
      components/lazsvnpkg/lazsvnpkg_images.sh \
      components/projectgroups/images/pg_images.sh \
      docs/html/build_lcl_chm.sh \
      images/bookmark.sh \
      images/components_images.sh \
      images/laz_images.sh \
      tools/compile_all.sh \
      tools/copy_po_files_to_lazarus_sources.sh \
      tools/create_lazarus_deb.sh \
      tools/find_missing_lpl_files.sh \
      tools/getallpofiles.sh \
      tools/install/build_fpc_snaphot_rpm.sh \
      tools/install/check_fpc_dependencies.sh \
      tools/install/create_clean_fpcsrc_directory.sh \
      tools/install/create_clean_lazarus_directory.sh \
      tools/install/create_lazarus_deb.sh \
      tools/install/create_lazarus_snapshot_rpm.sh \
      tools/install/cross_unix/create_linux_cross_win32_deb.sh \
      tools/install/cross_unix/create_linux_cross_win32_rpm.sh \
      tools/install/cross_unix/update_cross_fpc.sh \
      tools/install/do_nothing.sh \
      tools/install/file_filter.sh \
      tools/install/get_fpc_full_version.sh \
      tools/install/get_lazarus_version.sh \
      tools/install/get_svn_revision_number.sh \
      tools/install/macosx/create_fpc-src_dmg.sh \
      tools/install/macosx/create_lazarus_dmg.sh \
      tools/install/macosx/makefpcsnapshot.sh \
      tools/install/macosx/makefpcsrcsnapshot.sh \
      tools/install/macosx/makelazsnapshot.sh \
      tools/install/macosx/uninstall.sh \
      tools/install/rpm/create_gtk1_links.sh \
      tools/install/rpm/create_lazarus_rpm.sh \
      tools/install/rpm/create_nonroot_rpmmacros.sh \
      tools/install/rpm/get_rpm_source_dir.sh \
      tools/install/smart_strip.sh \
      tools/lfm_to_lrs.sh

%build
# Re-create the Makefiles
export FPCDIR=%{_datadir}/fpcsrc/
fpcmake -Tall
cd components
fpcmake -Tall
cd ../

# Enable GDB debuginfo in DWARF format, plus some optimisations
%{__make} -j1 LCL_PLATFORM=gtk3 OPT="-k--build-id -g -gl -gw -O3"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_metainfodir},%{_examplesdir}}

%{__make} install INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} _LIB=%{_lib}

%{__mv} $RPM_BUILD_ROOT%{_libdir}/lazarus/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/lazarus/{lazarus.app,test}

find $RPM_BUILD_ROOT%{_libdir}/lazarus \( -name 'Makefile*' -o -name .gitignore \) -exec %{__rm} {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt COPYING.modifiedLGPL.txt docs/*.txt docs/*.pdf
%attr(755,root,root) %{_bindir}/lazarus-ide
%attr(755,root,root) %{_bindir}/lazbuild
%attr(755,root,root) %{_bindir}/startlazarus
%attr(755,root,root) %{_bindir}/lazres
%attr(755,root,root) %{_bindir}/lrstolfm
%attr(755,root,root) %{_bindir}/updatepofiles
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
%dir %{_libdir}/lazarus/tools
%{_libdir}/lazarus/tools/apiwizz
%{_libdir}/lazarus/tools/chmmaker
%{_libdir}/lazarus/tools/debugserver
%{_libdir}/lazarus/tools/glazres
%{_libdir}/lazarus/tools/install
%{_libdir}/lazarus/tools/jsonviewer
%{_libdir}/lazarus/tools/lazdatadesktop
%{_libdir}/lazarus/tools/snapshots
%{_libdir}/lazarus/tools/xpm_to_png
%attr(755,root,root) %{_libdir}/lazarus/tools/*.sh
%attr(755,root,root) %{_libdir}/lazarus/tools/lazres
%attr(755,root,root) %{_libdir}/lazarus/tools/lrstolfm
%attr(755,root,root) %{_libdir}/lazarus/tools/svn2revisioninc
%attr(755,root,root) %{_libdir}/lazarus/tools/updatepofiles
%{_libdir}/lazarus/tools/*.lp*
%{_libdir}/lazarus/tools/*.o
%{_libdir}/lazarus/tools/*.p*
%{_libdir}/lazarus/units
%attr(755,root,root) %{_libdir}/lazarus/lazarus
%attr(755,root,root) %{_libdir}/lazarus/lazbuild
%attr(755,root,root) %{_libdir}/lazarus/startlazarus
%{_pixmapsdir}/lazarus.png
%{_desktopdir}/lazarus.desktop
%{_examplesdir}/%{name}-%{version}
%{_iconsdir}/hicolor/*x*/mimetypes/text-lazarus-*.png
%{_iconsdir}/hicolor/*x*/mimetypes/text-x-pascal.png
%{_metainfodir}/lazarus.appdata.xml
%{_datadir}/mime/packages/lazarus.xml
%{_mandir}/man1/lazarus-ide.1*
%{_mandir}/man1/lazbuild.1*
%{_mandir}/man1/lazres.1*
%{_mandir}/man1/lrstolfm.1*
%{_mandir}/man1/startlazarus.1*
%{_mandir}/man1/svn2revisioninc.1*
%{_mandir}/man1/updatepofiles.1*
