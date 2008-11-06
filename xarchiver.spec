Summary:	Xarchiver, a lightweight archiving/compression tool
Name:		xarchiver
Version:	0.5.0
Release:	%mkrel 1
License:	GPLv2
Group:		Archiving/Compression
URL:		http://xarchiver.xfce.org
Source0:	http://downloads.sourceforge.net/xarchiver/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
Requires:	binutils
Requires:	unzip
Requires:	zip
Suggests:	arj
Suggests:	p7zip
Suggests:	lha
Suggests:	unrar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xarchiver is a GTK+2 only frontend to 7z, zip, rar, tar, bzip2, gzip, arj,
lha, rpm and deb (open and extract only).Xarchiver allows you to create,
add, extract and delete files in the above formats. 7z, zip, rar, arj 
password protected archives are supported.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root,755)
%{_bindir}/%{name}
%{_docdir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_libdir}/thunar-archive-plugin/xarchiver.tap
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
