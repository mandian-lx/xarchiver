Summary:	A lightweight archiving/compression tool
Name:		xarchiver
Version:	0.5.4.11
Release:	5
License:	GPLv2
Group:		Archiving/Compression
URL:		https://github.com/ib/%{name}/
Source0:	https://github.com/ib/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		https://github.com/ib/xarchiver/commit/79a73d46b782cf8bb93d058d00d2cb81a9b3df8a.patch

BuildRequires:	gtk+3-devel

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xsltproc


#Requires:	binutils
Requires:	unzip
Requires:	zip

Suggests:	arj
Suggests:	p7zip
Suggests:	lha
Suggests:	unrar
Suggests:	unar
Suggests:	xz

%description
Xarchiver is a GTK+2 only frontend to 7z, zip, rar, tar, bzip2, gzip, arj,
lha, rpm and deb (open and extract only).Xarchiver allows you to create,
add, extract and delete files in the above formats. 7z, zip, rar, arj 
password protected archives are supported.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libexecdir}/thunar-archive-plugin/xarchiver.tap
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}/*.png
%{_docdir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome %{name}.lang

# make the .desktop file compliant with xdg specs
desktop-file-install \
	--vendor="" \
	--remove-key="Encoding" \
	--remove-mime-type="multipart/x-zip" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/xarchiver.desktop

