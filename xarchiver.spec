%define oname   Xarchiver

Summary:	Xarchiver, a lightweight archiving/compression tool
Name:		xarchiver
Version:	0.4.6
Release:	%mkrel 4
License:	GPL
Group:		Archiving/Compression
URL:		http://xarchiver.xfce.org
Source0:	%{name}-%{version}.tar.bz2 
Patch0:		%{name}-0.4.6-fix-compilation.patch
BuildRequires:	pkgconfig
BuildRequires:	gtk+2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xarchiver is a lightweight GTK2 only frontend to
7zip, arj, rar, zip, bzip2, tar, gzip and RPM.

%prep
%setup -q
%patch0 -p1
%build
%configure2_5x
		
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32}/apps
convert icons/48x48/%{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert icons/48x48/%{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png

desktop-file-install \
    --remove-category="Application" \
    --add-category="Archiving" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%clean 
rm -rf %{buildroot}

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,755)
%{_datadir}/doc/xarchiver/* 
%{_bindir}/%{name}
%{_datadir}/applications/xarchiver.desktop
%{_libdir}/thunar-archive-plugin/xarchiver.tap
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/xarchiver/*.png
