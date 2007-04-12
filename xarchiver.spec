%define	name	xarchiver
%define oname   Xarchiver
%define	version	0.4.6
%define pre        0
%define	rel	    1
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://xarchiver.xfce.org/
Source0:	%{name}-%{version}.tar.bz2 
Source1:	%name.png
License:	GPL
Group:		Archiving/Compression
Summary:	Xarchiver, a lightweight archiving/compression tool
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	pkgconfig
BuildRequires:  gtk+2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Xarchiver is a lightweight GTK2 only frontend to
7zip, arj, rar, zip, bzip2, tar, gzip and RPM.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure
		
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}} 
convert %SOURCE1 -geometry 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %SOURCE1 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert %SOURCE1 -geometry 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" icon="xarchiver.png" \
  needs="x11" section="System/Archiving/Compression" title="Xarchiver" \
  longtitle="Create and manage archives" startup_notify="true" xdg="true"
EOF

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="X-MandrivaLinux-System-Archiving-Compression" \
--add-category="Archiving" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%{find_lang} --with-gnome

%clean 
rm -rf $RPM_BUILD_ROOT 

%post
%{update_menus}
%{update_desktop_database}

%postun
%{clean_menus}
%{clean_desktop_database}

%files 
%defattr(-,root,root,755)
%{_datadir}/doc/xarchiver/* 
%_bindir/%{name}
%{_datadir}/applications/xarchiver.desktop
%{_libdir}/thunar-archive-plugin/xarchiver.tap
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png 
%_menudir/%name
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/xarchiver.*
%{_datadir}/icons/hicolor/48x48/apps/xarchiver.png
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/pixmaps/xarchiver/*.png


