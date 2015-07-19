Summary:	A lightweight archiving/compression tool
Name:		xarchiver
Version:	0.5.3
Release:	5
License:	GPLv2
Group:		Archiving/Compression
URL:		http://xarchiver.xfce.org
Source0:	http://downloads.sourceforge.net/xarchiver/%{name}-%{version}.tar.bz2
Patch0:		xarchiver-0.5.2-format_not_a_string_literal_and_no_format_arguments.patch
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
%apply_patches

%build
%configure
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
%{_libexecdir}/thunar-archive-plugin/xarchiver.tap
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
