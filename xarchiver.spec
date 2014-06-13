Summary:	A lightweight archiving/compression tool
Name:		xarchiver
Version:	0.5.2
Release:	18
License:	GPLv2
Group:		Archiving/Compression
URL:		http://xarchiver.xfce.org
Source0:	http://downloads.sourceforge.net/xarchiver/%{name}-%{version}.tar.bz2
Patch0:		xarchiver-0.5.2-format_not_a_string_literal_and_no_format_arguments.patch
Patch1:		xarchiver-0.5.2-fix_7z_support.patch
Patch2:		xarchiver-0.5.2-add_xz_support.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	desktop-file-utils
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
#Requires:	binutils
Requires:	unzip
Requires:	zip
Suggests:	arj
Suggests:	p7zip
Suggests:	lha
Suggests:	unrar
Suggests:	xz

%description
Xarchiver is a GTK+2 only frontend to 7z, zip, rar, tar, bzip2, gzip, arj,
lha, rpm and deb (open and extract only).Xarchiver allows you to create,
add, extract and delete files in the above formats. 7z, zip, rar, arj 
password protected archives are supported.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome %{name}.lang

# make the .desktop file compliant with xdg specs

desktop-file-install \
		--vendor="" \
		--remove-key="Encoding" \
		--remove-mime-type="multipart/x-zip" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/xarchiver.desktop


%files -f %{name}.lang
%{_bindir}/%{name}
%{_docdir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_libdir}/thunar-archive-plugin/xarchiver.tap
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg


%changelog
* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-11
+ Revision: 789811
- rebuild
- drop old stuff from spec file

* Tue Apr 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.5.2-10
+ Revision: 659348
- added p2 for xz support
- added xz as suggests
- dropped suspect requires for binutils

* Sat Mar 05 2011 Funda Wang <fwang@mandriva.org> 0.5.2-9
+ Revision: 642115
- rebuild

* Thu Feb 10 2011 ÐÐ»ÐµÐºÑÐ°Ð½Ð´Ñ€ ÐšÐ°Ð·Ð°Ð½Ñ†ÐµÐ² <kazancas@mandriva.org> 0.5.2-8
+ Revision: 637204
- 7zip crash gui fix

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-7
+ Revision: 633052
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-6mdv2011.0
+ Revision: 579640
- rebuild for new xfce 4.7.0

* Tue Mar 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.2-4mdv2010.1
+ Revision: 521985
- fix .desktop file

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.5.2-3mdv2010.0
+ Revision: 445866
- rebuild

* Sun Mar 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-2mdv2009.1
+ Revision: 353010
- Patch0: fix compiling with Werror=format-strings

* Wed Nov 12 2008 Funda Wang <fwang@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 302477
- New version 0.5.2

* Fri Nov 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 300759
- update to new version 0.5.1

* Thu Nov 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 300324
- update to new version 0.5.0

* Wed Oct 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.rc1.1mdv2009.1
+ Revision: 296559
- update to new version 0.5.0rc1

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.beta2.2mdv2009.1
+ Revision: 294928
- rebuild for new Xfce4.6 beta1

* Fri Oct 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.beta2.1mdv2009.1
+ Revision: 291556
- update to new version 0.5.0beta2

* Tue Aug 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.beta1.1mdv2009.0
+ Revision: 276256
- ressurection of xarchiver, update to new version 0.5.0beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.9-5mdv2009.0
+ Revision: 262241
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.9-4mdv2009.0
+ Revision: 256566
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.9-2mdv2008.1
+ Revision: 135444
- fix deps
- suggest some additional archivers

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.4.9-1mdv2008.1
+ Revision: 120755
- Add BR
- Add a lot of BR
- New release 4.9

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - provide patch 0 (fixes compilation)
    - drop X-MandrivaLinux from desktop file

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.6-3mdv2008.0
+ Revision: 32837
- s/imagemagick/ImageMagick

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.6-2mdv2008.0
+ Revision: 32831
- drop old menu style
- drop Source1
- spec file clean


* Fri Dec 15 2006 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.4.6-1mdv2007.0
+ Revision: 97289
- Add BuildRequires
- Push Xarchiver
- Import xarchiver

* Mon Sep 04 2006 Jerome Soyer <saispo@mandriva.org> 0.4.0-1mdv2007.0
- 0.4.0

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 0.3.9.2-0.beta2.1mdv2007.0
- 0.3.9.2beta2
- drop icon source and use included
- xdg
- cleanup

* Sat May 06 2006 Jerome Soyer <saispo@mandriva.org> 0.3.3-1mdk
- New release 0.3.3

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.2-2mdk
- Fix BuildRequires

* Wed May 03 2006 Jerome Soyer <saispo@mandriva.org> 0.3.2-1mdk
- New release 0.3.2

* Thu Apr 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.1-3mdk
- Fix BuildRequires

* Wed Apr 05 2006 Jerome Soyer <saispo@mandriva.org> 0.3.1-2mdk
* Mon Apr 03 2006 Phil <philippe-pierre@lamarelle.org> 0.3.1-2mdk
    - added menus
    - rebuild

* Mon Apr 03 2006 Jerome Soyer <saispo@mandriva.org> 0.3.1-1mdk
- RPM From :

 * Sun Apr 02 2006 Phil <philippe-pierre@lamarelle.org> 0.3.1-1mdk
   - removed NEWS (empty file) from %%doc
   - cleaned up xarchiver.spec
   - rebuild
   - xarchiver 0.3.1 initial mdk release

